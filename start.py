#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
import re
import time
import logging
from typing import Dict, List, Optional, Tuple
from pathlib import Path
from datetime import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sas_cam.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\033[35m'

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"
]

class CameraViewer:
    
    SOURCES = {
        'insecam': {
            'countries_url': 'http://www.insecam.org/en/jsoncountries/',
            'camera_url': 'http://www.insecam.org/en/bycountry/',
        },
        'bing': {
            'camera_url': 'https://www.bing.com/videos/search?q=ip+camera+',
        },
        'zoomeye': {
            'camera_url': 'https://www.zoomeye.org/search?q=',
        },
        'fofa': {
            'camera_url': 'https://fofa.info/result?qbase64=',
        },
        'censys': {
            'camera_url': 'https://censys.io/ipv4?q=',
        },
        'shodan': {
            'camera_url': 'https://www.shodan.io/search?query=',
        }
    }
    
    def __init__(self, timeout: int = 10):
    
        self.timeout = timeout
        self.session = self._create_session()
        self.countries = {}
        self.all_cameras = []
        
    def _create_session(self) -> requests.Session:
      
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "HEAD"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session
    
    def _get_headers(self) -> Dict[str, str]:
      
        import random
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random.choice(USER_AGENTS)
        }
        return headers
    
    def fetch_countries(self) -> bool:
   
        try:
            logger.info("Fetching country list from SAS-CAM...")
            response = self.session.get(
                self.SOURCES['insecam']['countries_url'],
                headers=self._get_headers(),
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            self.countries = data.get('countries', {})
            logger.info(f"Successfully fetched {len(self.countries)} countries")
            return True
            
        except requests.RequestException as e:
            logger.error(f"Failed to fetch countries: {e}")
            return False
    
    def display_countries(self) -> None:

        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*75}")
        print(f"  AVAILABLE COUNTRIES")
        print(f"{'='*75}{Colors.ENDC}\n")
        
        if not self.countries:
            print(f"{Colors.RED}No countries available.{Colors.ENDC}")
            return
        
        sorted_countries = sorted(
            self.countries.items(),
            key=lambda x: x[1].get('count', 0),
            reverse=True
        )
        
        print(f"{Colors.BOLD}{'CODE':<6} {'COUNTRY':<45} {'CAMERAS':<15}{Colors.ENDC}")
        print(f"{Colors.CYAN}{'-'*75}{Colors.ENDC}")
        
        for code, info in sorted_countries:
            country_name = info.get('country', 'Unknown')
            count = info.get('count', 0)
            
            print(f"{Colors.GREEN}{code:<6}{Colors.ENDC} {country_name:<45} {Colors.YELLOW}{count:<15}{Colors.ENDC}")
        
        print(f"\n{Colors.CYAN}{'='*75}{Colors.ENDC}\n")
    
    def get_cameras_by_country(self, country_code: str) -> List[Dict]:

        cameras = []
        
        try:
            logger.info(f"Fetching ALL cameras for {country_code}...")

            try:
                response = self.session.get(
                    f"{self.SOURCES['insecam']['camera_url']}{country_code}",
                    headers=self._get_headers(),
                    timeout=self.timeout
                )
                response.raise_for_status()

                page_match = re.findall(r'pagenavigator\("\?page=", (\d+)', response.text)
                total_pages = int(page_match[0]) if page_match else 1
                logger.info(f"Found {total_pages} pages for {country_code}")

                ips = re.findall(r'http://(\d+\.\d+\.\d+\.\d+:\d+)', response.text)
                if not ips:
                    ips = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)', response.text)
                
                for ip in ips:
                    if ip not in [cam['ip'] for cam in cameras]:
                        cameras.append({
                            'ip': ip,
                            'url': f'http://{ip}'
                        })
                
                logger.info(f"Page 1/{total_pages}: Found {len(ips)} cameras")

                for page in range(1, total_pages):
                    try:
                        page_response = self.session.get(
                            f"{self.SOURCES['insecam']['camera_url']}{country_code}/?page={page}",
                            headers=self._get_headers(),
                            timeout=self.timeout
                        )
                        page_response.raise_for_status()

                        page_ips = re.findall(r'http://(\d+\.\d+\.\d+\.\d+:\d+)', page_response.text)
                        if not page_ips:
                            page_ips = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)', page_response.text)
                        
                        for ip in page_ips:
                            if ip not in [cam['ip'] for cam in cameras]:
                                cameras.append({
                                    'ip': ip,
                                    'url': f'http://{ip}'
                                })
                        
                        logger.info(f"Page {page+1}/{total_pages}: Found {len(page_ips)} cameras (Total: {len(cameras)})")

                        time.sleep(0.5)
                        
                    except Exception as e:
                        logger.warning(f"Error on page {page}: {e}")
                        continue
                
                logger.info(f"TOTAL cameras found in {country_code}: {len(cameras)}")
                return cameras
                
            except Exception as e:
                logger.error(f"Error fetching from SAS-CAM: {e}")
                return cameras
            
        except Exception as e:
            logger.error(f"Failed to fetch cameras for {country_code}: {e}")
            return cameras
    
    def display_cameras(self, cameras: List[Dict], country_name: str = "") -> None:

        if not cameras:
            print(f"{Colors.RED}No cameras found.{Colors.ENDC}")
            return
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*85}")
        print(f"  {country_name.upper()} - {len(cameras)} CAMERAS")
        print(f"{'='*85}{Colors.ENDC}\n")
        
        print(f"{Colors.BOLD}{'IP:PORT':<30} {'LINK':<55}{Colors.ENDC}")
        print(f"{Colors.CYAN}{'-'*85}{Colors.ENDC}")
        
        for idx, camera in enumerate(cameras, 1):
            ip = camera.get('ip', 'N/A')
            url = camera.get('url', 'N/A')
            
            print(f"{Colors.GREEN}{ip:<30}{Colors.ENDC} {Colors.MAGENTA}{url:<55}{Colors.ENDC}")
            
            if idx % 10 == 0:
                print()
        
        print(f"\n{Colors.CYAN}{'='*85}{Colors.ENDC}\n")
    
    def copy_cameras_to_clipboard(self, cameras: List[Dict]) -> None:

        try:
            import subprocess
            urls = '\n'.join([cam['url'] for cam in cameras])
            
            try:
                process = subprocess.Popen(['clip'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                process.communicate(urls.encode())
                print(f"{Colors.GREEN}✓ {len(cameras)} IPs copied to clipboard!{Colors.ENDC}")
            except:
                try:
                    process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                    process.communicate(urls.encode())
                    print(f"{Colors.GREEN}✓ {len(cameras)} IPs copied to clipboard!{Colors.ENDC}")
                except:
                    print(f"{Colors.YELLOW}⚠ Clipboard not available{Colors.ENDC}")
        except Exception as e:
            logger.error(f"Clipboard error: {e}")

def print_banner() -> None:
    banner = f"""
{Colors.BOLD}{Colors.CYAN}
  █████████    █████████    █████████               █████████    █████████   ██████   ██████
 ███▒▒▒▒▒███  ███▒▒▒▒▒███  ███▒▒▒▒▒███             ███▒▒▒▒▒███  ███▒▒▒▒▒███ ▒▒██████ ██████ 
▒███    ▒▒▒  ▒███    ▒███ ▒███    ▒▒▒             ███     ▒▒▒  ▒███    ▒███  ▒███▒█████▒███ 
▒▒█████████  ▒███████████ ▒▒█████████  ██████████▒███          ▒███████████  ▒███▒▒███ ▒███ 
 ▒▒▒▒▒▒▒▒███ ▒███▒▒▒▒▒███  ▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒ ▒███          ▒███▒▒▒▒▒███  ▒███ ▒▒▒  ▒███ 
 ███    ▒███ ▒███    ▒███  ███    ▒███           ▒▒███     ███ ▒███    ▒███  ▒███      ▒███ 
▒▒█████████  █████   █████▒▒█████████             ▒▒█████████  █████   █████ █████     █████
 ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒               ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒     ▒▒▒▒▒

{Colors.GREEN}═══════════════════════════════════════════════════════════════════════════{Colors.ENDC}
{Colors.YELLOW}               SKILL ALL SHOW : DEVELOPER : ЦПKПӨЩM 69                    {Colors.ENDC}
{Colors.GREEN}═══════════════════════════════════════════════════════════════════════════{Colors.ENDC}

{Colors.CYAN}Version: 1.0 | Python 3.6 | Python 3.11{Colors.ENDC}

{Colors.RED} DISCORD : https://discord.gg/mzXMpC9g9S{Colors.ENDC}

{Colors.ENDC}
"""
    print(banner)

def main():

    print_banner()
    
    viewer = CameraViewer()
    
    if not viewer.fetch_countries():
        print(f"{Colors.RED}Failed to initialize camera. Exiting.{Colors.ENDC}")
        sys.exit(1)
    
    print(f"\n{Colors.GREEN}✓ Camera database loaded successfully!{Colors.ENDC}")
    
    while True:
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*75}")
        print(f"  MENU")
        print(f"{'='*75}{Colors.ENDC}")
        print(f"{Colors.GREEN}1.{Colors.ENDC} View Countries")
        print(f"{Colors.GREEN}2.{Colors.ENDC} Get Cameras by Country")
        print(f"{Colors.GREEN}3.{Colors.ENDC} Get Cameras by Region")
        print(f"{Colors.GREEN}4.{Colors.ENDC} Search Cameras")
        print(f"{Colors.GREEN}5.{Colors.ENDC} Exit")
        print(f"{Colors.CYAN}{'='*75}{Colors.ENDC}\n")
        
        choice = input(f"{Colors.BOLD}Select option (1-5): {Colors.ENDC}").strip()
        
        if choice == '1':
           
            viewer.display_countries()
            
        elif choice == '2':
           
            viewer.display_countries()
            
            print(f"{Colors.YELLOW}Enter country code (e.g., 'US', 'GB', 'DE', 'CN'):{Colors.ENDC}")
            country_code = input(f"{Colors.BOLD}Country Code: {Colors.ENDC}").upper().strip()
            
            if country_code not in viewer.countries:
                print(f"{Colors.RED}Invalid country code!{Colors.ENDC}")
                continue
            
            country_name = viewer.countries[country_code]['country']
            print(f"\n{Colors.CYAN}Getting cameras for {country_name}...{Colors.ENDC}")
            
            cameras = viewer.get_cameras_by_country(country_code)
            
            if cameras:
                viewer.display_cameras(cameras, country_name)
                
          
                print(f"{Colors.BOLD}Copy options:{Colors.ENDC}")
                print(f"{Colors.GREEN}1.{Colors.ENDC} Copy all URLs to clipboard")
                print(f"{Colors.GREEN}2.{Colors.ENDC} Skip")
                
                copy_choice = input(f"{Colors.BOLD}Select (1-2): {Colors.ENDC}").strip()
                
                if copy_choice == '1':
                    viewer.copy_cameras_to_clipboard(cameras)
            else:
                print(f"{Colors.RED}No cameras found for {country_name}.{Colors.ENDC}")
        
        elif choice == '3':
          
            regions = {
                '1': {
                    'name': 'Europe',
                    'countries': ['GB', 'DE', 'FR', 'IT', 'ES', 'NL', 'BE', 'CH', 'SE', 'NO', 'DK', 'PL', 'RU', 'UA', 'RO', 'PT', 'GR', 'CZ', 'AT', 'HU']
                },
                '2': {
                    'name': 'Asia',
                    'countries': ['CN', 'JP', 'KR', 'IN', 'TH', 'VN', 'MY', 'SG', 'ID', 'PH', 'TW', 'HK', 'KZ', 'PK', 'BD', 'IR']
                },
                '3': {
                    'name': 'Americas',
                    'countries': ['US', 'CA', 'MX', 'BR', 'AR', 'CL', 'CO', 'VE', 'PE', 'EC']
                },
                '4': {
                    'name': 'Africa',
                    'countries': ['ZA', 'EG', 'NG', 'KE', 'MA', 'TN', 'DZ', 'GH', 'ET', 'UG']
                },
                '5': {
                    'name': 'Oceania',
                    'countries': ['AU', 'NZ', 'FI', 'PH']
                }
            }
            
            print(f"\n{Colors.BOLD}{Colors.CYAN}Select Region:{Colors.ENDC}")
            for key, region in regions.items():
                print(f"{Colors.GREEN}{key}.{Colors.ENDC} {region['name']}")
            
            region_choice = input(f"{Colors.BOLD}Select region (1-5): {Colors.ENDC}").strip()
            
            if region_choice not in regions:
                print(f"{Colors.RED}Invalid region!{Colors.ENDC}")
                continue
            
            region_info = regions[region_choice]
            region_name = region_info['name']
            all_cameras = []
            
            print(f"\n{Colors.CYAN}Getting cameras from {region_name}...{Colors.ENDC}")
            
            for country_code in region_info['countries']:
                if country_code in viewer.countries:
                    cameras = viewer.get_cameras_by_country(country_code)
                    if cameras:
                        all_cameras.extend(cameras)
            
            if all_cameras:
                viewer.display_cameras(all_cameras, f"{region_name} Region")
                
                print(f"{Colors.BOLD}Copy options:{Colors.ENDC}")
                print(f"{Colors.GREEN}1.{Colors.ENDC} Copy all URLs to clipboard")
                print(f"{Colors.GREEN}2.{Colors.ENDC} Skip")
                
                copy_choice = input(f"{Colors.BOLD}Select (1-2): {Colors.ENDC}").strip()
                
                if copy_choice == '1':
                    viewer.copy_cameras_to_clipboard(all_cameras)
            else:
                print(f"{Colors.RED}No cameras found in {region_name}.{Colors.ENDC}")
        
        elif choice == '4':
        
            print(f"\n{Colors.YELLOW}Search by IP pattern (e.g., '192.168', '10.0'):{Colors.ENDC}")
            search_pattern = input(f"{Colors.BOLD}IP Pattern: {Colors.ENDC}").strip()
            
            if not search_pattern:
                print(f"{Colors.RED}No search pattern provided!{Colors.ENDC}")
                continue
            
            print(f"\n{Colors.CYAN}Searching for '{search_pattern}'...{Colors.ENDC}")
            
            results = []
            for country_code in list(viewer.countries.keys())[:10]: 
                cameras = viewer.get_cameras_by_country(country_code)
                for camera in cameras:
                    if search_pattern in camera['ip']:
                        results.append(camera)
            
            if results:
                print(f"\n{Colors.GREEN}Found {len(results)} cameras matching '{search_pattern}'{Colors.ENDC}\n")
                
                for camera in results[:50]:  
                    print(f"{Colors.MAGENTA}{camera['ip']:<25}{Colors.ENDC} {Colors.GREEN}{camera['url']}{Colors.ENDC}")
                
                if len(results) > 50:
                    print(f"\n{Colors.YELLOW}... and {len(results) - 50} more results{Colors.ENDC}")
                
                if len(results) <= 50:
                    print(f"\n{Colors.BOLD}Copy options:{Colors.ENDC}")
                    print(f"{Colors.GREEN}1.{Colors.ENDC} Copy all URLs to clipboard")
                    print(f"{Colors.GREEN}2.{Colors.ENDC} Skip")
                    
                    copy_choice = input(f"{Colors.BOLD}Select (1-2): {Colors.ENDC}").strip()
                    
                    if copy_choice == '1':
                        viewer.copy_cameras_to_clipboard(results)
            else:
                print(f"{Colors.RED}No cameras found matching '{search_pattern}'.{Colors.ENDC}")
        
        elif choice == '5':
            print(f"\n{Colors.GREEN}Goodbye!{Colors.ENDC}\n")
            sys.exit(0)
        
        else:
            print(f"{Colors.RED}Invalid option. Please try again.{Colors.ENDC}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Cancelled.{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        print(f"{Colors.RED}Error: {e}{Colors.ENDC}")
        sys.exit(1)
