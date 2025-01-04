# index.py
from scanning import perform_scan
from exploitation import exploit_vulnerability
from post_exp import post_exploitation
from report import generate_report

# Global variable for target IP
global_target_ip = ""

def main():
    global global_target_ip
    global_target_ip = input("Enter your Target IP: ")
    if not global_target_ip:
        print("Target IP is required.")
        return

    # Perform scanning
    scan_results = perform_scan(global_target_ip)

    # Exploitation
    exploit_results = exploit_vulnerability(global_target_ip, scan_results)

    # Post-Exploitation
    post_exp_results = post_exploitation(global_target_ip, exploit_results)

    # Generate report
    generate_report(global_target_ip, scan_results, exploit_results, post_exp_results)

if __name__ == "__main__":
    main()

