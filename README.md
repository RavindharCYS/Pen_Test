# VAPT Automation Tool (Vulnerability Assessment and Penetration Testing)

This project is a Python-based tool designed to perform Vulnerability Assessment and Penetration Testing (VAPT) on a Windows 7 target system. The tool scans for vulnerabilities, exploits the EternalBlue vulnerability (`MS17-010`), performs post-exploitation activities, and generates a comprehensive assessment report.

## Features

* **Scanning:** Scans the target system for vulnerabilities using `nmap` with detailed output.
* **Exploitation:** Exploits the EternalBlue vulnerability in Windows 7 (SMBv1 enabled) using Metasploit.
* **Post-Exploitation:** Collects system data and simulates persistence setup.
* **Reporting:** Generates a detailed report including scanned ports, vulnerabilities, exploitation details, and remediation techniques.

## Requirements

1. **Operating System:** Linux (tested on Ubuntu/Debian).
2. **Tools:**
   * `nmap` for scanning.
   * `metasploit-framework` for exploitation.
3. **Python Packages:** Python 3.x and `nmap` library.
4. **Target System:** Windows 7 with SMBv1 enabled and vulnerable to EternalBlue.

## Installation

1. Update the system:
```bash
sudo apt-get update
```

2. Install the required tools:
```bash
sudo apt-get install nmap metasploit-framework python3
```

3. Clone this repository:
```bash
git clone <repository_url>
cd vapt-tool
```

## Usage

1. Run the tool using the entry script `index.py`:
```bash
python3 index.py
```

2. Enter the target IP address when prompted.

## File Structure

```
vapt-tool/
│
├── index.py        # Entry point for the tool.
├── scanning.py     # Performs vulnerability scanning using Nmap.
├── exploitation.py # Exploits the EternalBlue vulnerability.
├── post_exp.py     # Handles post-exploitation tasks.
├── report.py       # Generates a detailed VAPT report.
├── README.md       # Documentation for the project.
```

## Workflow

1. **Input Target IP:** Start by providing the IP address of the Windows 7 target system.
2. **Scanning:** The tool scans all ports using Nmap to detect open ports and vulnerabilities.
3. **Exploitation:** If EternalBlue (`MS17-010`) is detected, the tool exploits the vulnerability using Metasploit.
4. **Post-Exploitation:** Simulates data collection and persistence setup.
5. **Report Generation:** A detailed report is generated as `VAPT_Report.txt`.

## Output

* **Command-Line Interface:** Displays vulnerabilities, exploitation status, and post-exploitation information.
* **Report File:** A detailed report (`VAPT_Report.txt`) is generated with:
   * Targeted IP
   * List of scanned ports
   * Detected vulnerabilities
   * Exploitation details
   * Post-exploitation data
   * Remediation techniques

## Example

Input:
```mathematica
Enter your Target IP: "Target IP"
```

Output:

CLI Example:
```vbnet
Scanning target "Target IP" for vulnerabilities...
Available Vulnerabilities:
- SMBv1 is enabled and vulnerable to MS17-010.
Exploiting EternalBlue on 192.168.1.100...
Exploit completed successfully.
Performing post-exploitation tasks...
Post-exploitation completed.
Generating detailed report...
Report saved as VAPT_Report.txt
```

Report File:
```plaintext
VAPT Report
===========
Targeted IP: "Target IP"
------------------------
Ports Scanned: 445, 139
Vulnerabilities Found: SMBv1 is enabled and vulnerable to MS17-010.
Exploitation:
  Status: Success
  Details: EternalBlue exploited successfully with Meterpreter payload.
Post-Exploitation:
  Persistence: True
  Data Collected: System information, List of user accounts, Extracted sensitive files.
Remediation:
  - Disable SMBv1 on Windows systems.
  - Apply the latest patches and updates.
```

## Notes

* This tool is for educational purposes only. Use it only on systems you own or have explicit permission to test.
* Unauthorized use of this tool is illegal.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
