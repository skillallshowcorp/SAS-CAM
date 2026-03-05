# 🎥 SAS-CAM - Global IP Camera 

![SAS-CAM Logo](./logo.png)

![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.6+-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Termux-lightblue)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Legal Notice](#legal-notice)
- [System Requirements](#system-requirements)
- [Installation](#installation)
  - [Windows Installation](#windows-installation)
  - [Linux Installation](#linux-installation)
  - [Termux Installation (Android)](#termux-installation-android)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Advanced Options](#advanced-options)
- [Output Formats](#output-formats)
- [Troubleshooting](#troubleshooting)
- [Security & Privacy](#security--privacy)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

---

## 📖 Overview

**SAS-CAM** is a professional-grade IP camera viewer and discovery tool for authorized security research. This application displays publicly accessible IP cameras from multiple global sources in real-time, without storing or saving any data. It's designed for security researchers, penetration testers, and IT professionals to quickly view camera infrastructure across different countries and regions.

The application provides:
- **Real-time Display**: View publicly accessible IP cameras from multiple sources
- **Country-Based Viewing**: Browse and display cameras organized by country
- **Regional Filtering**: View cameras grouped by geographic region
- **Search & Filter**: Find specific cameras by IP pattern
- **Clipboard Integration**: Quick copy of camera URLs for verification
- **No Data Storage**: Pure viewer tool - displays results without saving files

### ⚠️ CRITICAL DISCLAIMER

**This tool is designed EXCLUSIVELY for authorized security research and penetration testing with proper authorization.**

Unauthorized access to computer systems, networks, or surveillance devices is **ILLEGAL** and may result in:
- Criminal prosecution
- Civil liability
- Imprisonment
- Heavy fines

**By using SAS-CAM, you acknowledge and accept full responsibility for your actions. The developers and contributors are not responsible for any illegal use or damage caused by misuse of this software.**

---

## ✨ Features

### Core Functionality
- ✅ **Global Camera Database**: Access publicly available IP cameras worldwide  
- ✅ **Multi-Source Support**: View cameras from multiple global sources
- ✅ **Country-Based Display**: Browse cameras organized by country code
- ✅ **Regional Filtering**: View cameras by geographic region (Europe, Asia, Americas, Africa, Oceania)
- ✅ **IP Search**: Find cameras by IP address patterns
- ✅ **Real-Time Viewing**: Display camera URLs instantly without saving
- ✅ **Cross-Platform**: Works on Windows, Linux, and Termux
- ✅ **Color-Coded Output**: Beautiful terminal colors for all platforms

### Security & Anonymity
- ✅ **User-Agent Rotation**: Automatic randomization across 6+ browser identities
- ✅ **Resilient Connections**: Automatic retry with exponential backoff
- ✅ **Rate Limiting**: Built-in delays to avoid server restrictions
- ✅ **Session Management**: Persistent HTTP sessions with connection pooling

### Advanced Features
- ✅ **Comprehensive Logging**: Operations logged to `sas_cam.log`
- ✅ **Clipboard Integration**: Copy camera URLs to clipboard directly
- ✅ **Formatted Display**: Beautiful table-formatted camera listings
- ✅ **Error Handling**: Graceful error recovery with detailed messages
- ✅ **No Data Storage**: Pure viewer - no files or data persistence

### Developer-Friendly
- ✅ **Clean Architecture**: Object-oriented design (CameraViewer class)
- ✅ **Type Hints**: Full Python type annotations
- ✅ **Modular Code**: Easy to customize and extend
- ✅ **Documentation**: Comprehensive inline comments

---

## 🔧 System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Python Version** | 3.6 | 3.10+ |
| **RAM** | 256 MB | 512 MB+ |
| **Disk Space** | 50 MB | 100 MB+ |
| **Internet** | Required | Stable connection |
| **OS** | Windows 7+ / Linux / Termux | Windows 10+ / Modern Linux |

### Required Libraries
- `requests` >= 2.31.0
- `urllib3` >= 2.0.0
- `colorama` >= 0.4.6 (for Windows color support)

---

## 📦 Installation

### Windows Installation

#### Method 1: Using Batch Script (Recommended)
1. Download or clone the repository to your desired location
2. Navigate to the project folder
3. Double-click `install_requirements.bat`
4. Wait for installation to complete

```batch
install_requirements.bat
```

#### Method 2: Manual Installation
1. Open **Command Prompt** or **PowerShell**
2. Navigate to project directory:
   ```powershell
   cd C:\Path\To\SAS-CAM
   ```
3. Create virtual environment (optional but recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
4. Install requirements:
   ```powershell
   pip install -r requirements.txt
   ```
5. Run the application:
   ```powershell
   python start.py
   ```

#### Troubleshooting Windows
- **"python not found"**: Add Python to PATH or use full path `C:\Python311\python.exe`
- **Cannot execute scripts**: Run PowerShell as Administrator
- **Colors not displaying**: Install colorama: `pip install colorama`

---

### Linux Installation

#### Ubuntu/Debian
```bash
# Update package manager
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Clone/navigate to project
cd ~/SAS-CAM

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run application
python3 start.py
```

#### Fedora/RHEL/CentOS
```bash
# Install Python and pip
sudo dnf install python3 python3-pip

# Navigate to project directory
cd ~/SAS-CAM

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run application
python3 start.py
```

#### Arch Linux
```bash
# Install Python
sudo pacman -S python python-pip

# Navigate and setup
cd ~/SAS-CAM
python3 -m venv venv
source venv/bin/activate

# Install requirements and run
pip install -r requirements.txt
python3 start.py
```

#### Generic Linux Installation
```bash
# Ensure Python 3.6+ is installed
python3 --version

# Navigate to project
cd ~/SAS-CAM

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install and run
pip install -r requirements.txt
python3 start.py
```

---

### Termux Installation (Android)

Termux is a powerful Android terminal emulator that allows running Linux commands and Python scripts on Android devices.

#### Step 1: Install Termux
- Download from [F-Droid](https://f-droid.org/packages/com.termux/) (recommended)
#### Step 2: Update Termux and Install Dependencies
```bash
# Update packages
pkg update && pkg upgrade

# Install Python and essential tools
pkg install python3 python3-pip git

# Install text editor (optional but recommended)
pkg install nano
```

#### Step 3: Clone/Download Project
```bash
# Clone the repository (if using git)
git clone https://github.com/UNKNOWN2069/SAS-CAM.git
cd SAS-CAM

# OR navigate if already downloaded
cd storage/downloads/SAS-CAM
```

#### Step 4: Setup Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

#### Step 5: Install Requirements
```bash
# Install Python dependencies
pip install -r requirements.txt --upgrade
```

#### Step 6: Run the Application
```bash
# Execute Camera Scanner
python3 start.py
```

#### Termux-Specific Tips
- **Storage Access**: To access phone storage: `termux-setup-storage`
- **Run at Startup**: Create alias in `.bashrc`:
  ```bash
  echo "alias camera='cd ~/SAS-CAM && python3 start.py'" >> ~/.bashrc
  source ~/.bashrc
  ```
- **Background Execution**: Use `nohup` to run in background
  ```bash
  nohup python3 start.py > scanner.log 2>&1 &
  ```
- **Persistent Connection**: Install and use `tmux` for persistent sessions
  ```bash
  pkg install tmux
  tmux new-session -d -s camera 'python3 start.py'
  ```

---

## 🚀 Quick Start

### Basic Usage (Interactive Menu)
```bash
python3 start.py
```

The SAS-CAM application launches an interactive menu with the following options:

1. **View All Available Countries** - Displays all countries with camera counts
2. **Display Cameras by Country** - Shows cameras from a specific country
3. **Display Cameras by Region** - Shows cameras grouped by geographic region
4. **Search/Filter Cameras** - Finds cameras by IP pattern
5. **Exit** - Closes the application

### Typical Workflow

```
1. Start application
   $ python3 start.py

2. Select "View All Available Countries" (Option 1)
   - Displays list of all countries with camera counts
   - Sorted by number of cameras (most to least)

3. Select "Display Cameras by Country" (Option 2)
   - Choose a country from the list (e.g., 'US', 'GB', 'DE')
   - View all camera IP addresses from that country
   - Optionally copy URLs to clipboard

4. OR Select "Display Cameras by Region" (Option 3)
   - Choose region: Europe, Asia, Americas, Africa, or Oceania
   - View all cameras from all countries in that region
   - Optionally copy URLs to clipboard

5. Optional: Search/Filter (Option 4)
   - Search by IP pattern (e.g., '192.168' or '10.0')
   - View matching cameras across countries
   - Real-time results display

6. Exit or repeat
   - No data saved to disk
   - All results are displayed in terminal
```

---

## 📖 Usage

### Interactive Menu

#### Option 1: View All Available Countries
Lists all countries with publicly accessible cameras, sorted by count:

```
═══════════════════════════════════════════════════════════════════════════
  SAS-CAM - GLOBAL PUBLIC & PRIVATE CAMERA DATABASE
  All Accessible IP Cameras Worldwide
═══════════════════════════════════════════════════════════════════════════

CODE   COUNTRY                    CAMERAS      TYPE           
────────────────────────────────────────────────────────────────────────────
US     United States              12453        Public        
CN     China                      8934         Public        
RU     Russia                     7621         Public        
DE     Germany                    5234         Public        
GB     United Kingdom             4123         Public        
```

#### Option 2: Display Cameras by Country

```
═══════════════════════════════════════════════════════════════════════════
  PUBLIC IP CAMERAS - UNITED STATES
  Total: 247 cameras found
═══════════════════════════════════════════════════════════════════════════

IP:PORT                  TYPE              URL                           
────────────────────────────────────────────────────────────────────────────
192.168.1.100:8080       PUBLIC           http://192.168.1.100:8080    
10.0.0.50:80             PUBLIC           http://10.0.0.50:80          
172.16.5.30:8888         PUBLIC           http://172.16.5.30:8888      

═══════════════════════════════════════════════════════════════════════════

Copy options:
1. Copy all URLs to clipboard
2. Skip
```

#### Option 3: Display Cameras by Region

```
═══════════════════════════════════════════════════════════════════════════
  PUBLIC IP CAMERAS - EUROPE REGION
  Total: 1,847 cameras found
═══════════════════════════════════════════════════════════════════════════

[Displays all cameras from Europe in table format]

Copy all EU region camera URLs to clipboard?
```

#### Option 4: Search/Filter Cameras

```
Search by IP pattern (e.g., '192.168', '10.0'):
IP Pattern: 192.168

Searching all countries for '192.168'...

Found 423 cameras matching '192.168'

192.168.1.1:8080         192.168.2.100:80         192.168.5.50:8888
192.168.10.1:80          192.168.100.200:9000     [... more results]
```

---

## 📁 Project Structure

```
SAS-CAM/
├── start.py                      # Main application (CameraViewer)
├── d.py                          # Original reference script (legacy)
├── requirements.txt              # Python dependencies
├── install_requirements.bat      # Windows installation script
├── start.sh                      # Linux/Termux launcher
├── config.json                   # Configuration settings
├── README.md                     # This file
├── LICENSE                       # MIT License
├── CHANGELOG.md                  # Version history
├── SECURITY.md                   # Security information
├── CONTRIBUTING.md               # Contribution guidelines
├── .gitignore                    # Git ignore patterns
└── sas_cam.log                   # Log file (auto-created on first run)
```

### Key Files Explained

- **start.py** - Main application with CameraViewer class for displaying IP cameras
- **d.py** - Original simple viewer script (legacy reference)
- **requirements.txt** - Python package dependencies (requests, colorama, urllib3)
- **config.json** - Viewer configuration (timeout, rate limits, API endpoints)
- **sas_cam.log** - Automatic logging of all viewer operations

---

## 🔧 Advanced Options

### Custom Timeout

To modify timeout settings, edit `start.py`:

```python
# Change timeout (in seconds)
viewer = CameraViewer(timeout=15)  # Default is 10
```

### Modify Clipboard Behavior

To use a different clipboard method, modify the `copy_cameras_to_clipboard()` method.

### Add Custom User-Agents

Extend the USER_AGENTS list in `start.py` to add additional browser strings for better anonymity:

```python
USER_AGENTS = [
    # ... existing agents ...
    "Your custom user agent here",
    "Another browser string"
]
```

### Filter by Port

Modify the `get_cameras_by_country()` method to filter specific ports:

```python
# Filter only cameras on port 8080
cameras = [cam for cam in cameras if ':8080' in cam['ip']]
```

---

## 📊 Data Display

### Real-Time Terminal Display

All results are displayed in real-time in the terminal with formatted tables:

```
═══════════════════════════════════════════════════════════════════════════
  PUBLIC IP CAMERAS - UNITED STATES
  Total: 1,247 cameras found
═══════════════════════════════════════════════════════════════════════════

IP:PORT                  TYPE             URL
────────────────────────────────────────────────────────────────────────────
192.168.1.100:8080       PUBLIC          http://192.168.1.100:8080
10.0.0.50:80             PUBLIC          http://10.0.0.50:80
172.16.5.30:8888         PUBLIC          http://172.16.5.30:8888
203.45.67.89:9000        PUBLIC          http://203.45.67.89:9000
210.123.45.67:8081       PUBLIC          http://210.123.45.67:8081

═══════════════════════════════════════════════════════════════════════════
```

### Clipboard Copy Feature

All displayed cameras can be copied to clipboard in URL format:

```
Selected: Copy all URLs to clipboard

✓ 1,247 camera URLs copied to clipboard!
```

Each URL is formatted as: `http://{IP}:{PORT}`

---

## 🐛 Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'requests'"
**Solution**: Install missing module
```bash
pip install requests
```

#### "Connection timeout" or "Connection refused"
**Causes**: 
- No internet connection
- Firewall blocking requests
- Camera database temporarily unavailable

**Solutions**:
- Check internet connection
- Disable firewall/VPN temporarily
- Wait and retry later
- Increase timeout: `CameraViewer(timeout=20)`

#### "No countries found"
**Cause**: Website structure may have changed

**Solution**: 
- Check log file: `sas_cam.log`
- Verify internet connection
- Website may require updated API endpoints

#### Colors not displaying (Windows)
**Solution**:
```powershell
pip install colorama --upgrade
```

#### "Permission denied" on Linux/Termux
**Solution**:
```bash
chmod +x start.py
python3 start.py
```

#### Clipboard not working
**Causes**: System-specific clipboard integration not available

**Solutions**:
- Windows: Ensure `clip` command is available
- Linux: Install `xclip`: `sudo apt install xclip`
- Termux: Limited clipboard support (data still displayed in terminal)
- Alternative: Manually copy from terminal output

#### Application crashes on Termux
**Solution**:
```bash
pkg install openssl libssl  # Install missing dependencies
pip install --upgrade requests
```

### Debug Mode

Enable detailed logging by modifying `start.py`:

```python
# Change line 18:
logging.basicConfig(
    level=logging.DEBUG,  # Changed from INFO
    # ... rest of config
)
```

Then check `camera_scanner.log` for detailed error messages.

---

## 🔒 Security & Privacy

### Best Practices

1. **Always Use Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Use VPN for Enhanced Privacy**
   - Consider using a VPN before running scans
   - Multiple User-Agent rotation included in tool

3. **Secure Your Results**
   - Move `scan_results/` directory to secure location
   - Don't share results publicly without authorization
   - Delete results after completing security assessment

4. **Monitor Logs**
   - Regularly check `camera_scanner.log` for anomalies
   - Report suspicious activity

### Legal Considerations

- **Verify Authorization**: Ensure you have written permission for all scans
- **Documentation**: Keep detailed records of when, where, and why scans were conducted
- **Jurisdiction**: Know the cyber laws in your location
- **Data Protection**: Comply with GDPR, CCPA, and other privacy regulations

### Ethical Use

This tool is provided for:
- ✅ Authorized penetration testing with signed agreements
- ✅ Security research by institutions and professionals
- ✅ Identifying vulnerable infrastructure for remediation
- ✅ Educational purposes in controlled environments

This tool is NOT provided for:
- ❌ Unauthorized access to any systems
- ❌ Privacy violation or surveillance
- ❌ Criminal activity of any kind
- ❌ Malicious purposes

---

## 🤝 Contributing

Contributions are welcome from the security research community!

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/UNKNOWN2069/SAS-CAM.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation as needed

4. **Test Thoroughly**
   ```bash
   python3 start.py
   ```

5. **Submit Pull Request**
   - Clear description of changes
   - Reference any related issues

### Code Style Guidelines

- Follow PEP 8 conventions
- Use type hints for functions
- Write descriptive variable names
- Include docstrings for classes and methods
- Maintain backward compatibility

---

## 📞 Support

### Getting Help

- **Documentation**: Refer to [README.md](README.md) and inline code comments
- **Logs**: Check `camera_scanner.log` for detailed error information
- **Issues**: Report bugs through GitHub Issues section
- **Community**: Join security research forums and communities

### Reporting Issues

When reporting issues, include:
1. Operating system and version
2. Python version (`python3 --version`)
3. Error message and stack trace
4. Steps to reproduce
5. Expected vs actual behavior

### Contact

- **Security Issues**: For security vulnerabilities, please contact responsibly
- **General Support**: GitHub Discussions or Issues

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

```
MIT License

Copyright (c) 2024 SAS-CAM Development Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
```

---

## ⚖️ Legal Disclaimer

**IMPORTANT - PLEASE READ CAREFULLY**

This software is provided "AS-IS" for educational and authorized security research purposes only. By downloading, installing, or using this software, you agree to:

1. Use this tool ONLY for authorized security assessments
2. Obtain written permission before scanning any systems
3. Comply with all applicable laws and regulations
4. Take full responsibility for your actions
5. Hold the developers harmless from any illegal use

**Unauthorized computer access is a serious crime** and may result in federal charges under:
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act 1990 - UK
- StGB § 202 - Germany
- Similar laws in other jurisdictions

Criminal penalties include:
- Up to **10 years imprisonment**
- Fines up to **$250,000+**
- Civil liability
- Permanent criminal record

**The developers and contributors assume NO LIABILITY for misuse of this tool.**

---

## 🙏 Acknowledgments

Special thanks to:
- Security research community
- Contributors and testers
- Open-source projects: requests, colorama, urllib3

---

**Last Updated**: March 5, 2024  
**Version**: 1.0.0  
**Status**: Active Development

---

### Quick Reference Card

| Task | Command |
|------|---------|
| Install (Windows) | `install_requirements.bat` |
| Install (Linux/Termux) | `pip install -r requirements.txt` |
| Run Application | `python3 start.py` |
| View Logs | `cat camera_scanner.log` |
| Update Dependencies | `pip install -r requirements.txt --upgrade` |
| Create Virtual Env | `python3 -m venv venv` |
| Activate Venv (Linux) | `source venv/bin/activate` |
| Activate Venv (Windows) | `venv\Scripts\activate` |
| Check Python Version | `python3 --version` |
| Get Help | See [Troubleshooting](#troubleshooting) section |

---

**For the latest updates, visit the project repository and check the Wiki for advanced topics.**
