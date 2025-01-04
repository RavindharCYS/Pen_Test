# report.py
def generate_report(target_ip, scan_results, exploit_results, post_exp_results):
    print("Generating detailed report...")

    report_content = f"""
    VAPT Report
    ===========
    Targeted IP: {target_ip}
    ------------------------
    Ports Scanned: {', '.join(scan_results.get('open_ports', []))}
    
    Vulnerabilities Found:
    {'; '.join(scan_results.get('vulnerabilities', []))}

    Exploitation:
    Status: {exploit_results.get('status')}
    Details: {exploit_results.get('details')}

    Post-Exploitation:
    Persistence: {post_exp_results.get('persistence')}
    Data Collected: {', '.join(post_exp_results.get('data_collected', []))}

    Remediation:
    - Disable SMBv1 on Windows systems.
    - Apply the latest patches and updates.
    """

    with open("VAPT_Report.txt", "w") as file:
        file.write(report_content)

    print("Report saved as VAPT_Report.txt")

