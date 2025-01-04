# scanning.py
import subprocess

def perform_scan(target_ip):
    print(f"Scanning target {target_ip} for vulnerabilities...")
    scan_results = {"host": target_ip, "open_ports": [], "vulnerabilities": []}

    # Run Nmap scan with vuln script
    try:
        result = subprocess.check_output(
            ["nmap", "-p", "1-65535", "-sV", "--script", "vuln", target_ip],
            universal_newlines=True
        )
        scan_results["raw_output"] = result

        # Parse open ports and vulnerabilities from Nmap output
        for line in result.split("\n"):
            if "open" in line and "/tcp" in line:
                port = line.split("/")[0].strip()
                scan_results["open_ports"].append(port)
            if "|_" in line or "VULNERABLE:" in line:
                scan_results["vulnerabilities"].append(line.strip())

        # Display vulnerabilities
        print("Available Vulnerabilities:")
        for vuln in scan_results["vulnerabilities"]:
            print(vuln)
    except Exception as e:
        print(f"Error during scanning: {e}")

    return scan_results

