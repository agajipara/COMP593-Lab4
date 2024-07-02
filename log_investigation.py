"""
Description:
 Generates various reports from a gateway log file.

Usage:
 python log_investigation.py log_path

Parameters:
 log_path = "C:\Users\ayush\Downloads\gateway.log"
"""
import log_analysis_lib
import pandas as pd

# Get the log file path from the command line
# Because this is outside of any function, log_path is a global variable
log_path = log_analysis_lib.get_file_path_from_cmd_line()

def main():
    # Determine how much traffic is on each port
    port_traffic = tally_port_traffic()

    # Per step 9, generate reports for ports that have 100 or more records
    for port, count in port_traffic.items():
        if count >= 100:
            generate_port_traffic_report(port)

    # Generate report of invalid user login attempts
    generate_invalid_user_report()

    # Generate log of records from source IP 220.195.35.40
    generate_source_ip_log('220.195.35.40')

def tally_port_traffic(log_path):
    """Produces a dictionary of destination port numbers (key) that appear in a 
    specified log file and a count of how many times they appear (value)

    Returns:
        dict: Dictionary of destination port number counts
    """
    # TODO: Complete function body per step 7
    port_traffic = {}
    with open(log_path, 'r') as log_file:
        for line in log_file:
            match = re.search(r'DPT=(\d+)', line)
            if match:
                port = match.group(1)
                if port in port_traffic:
                    port_traffic[port] += 1
                else:
                    port_traffic[port] = 1
    return(port_traffic)


def generate_port_traffic_report(port_number):
    """Produces a CSV report of all network traffic in a log file for a specified 
    destination port number.

    Args:
        port_number (str or int): Destination port number
    """
    # TODO: Complete function body per step 8
    report_data = []
    with open(log_path, 'r') as log_file:
        for line in log_file:
            if f'DPT={port}' in line:
                match = re.search(r'(\w+ \d+ \d+:\d+:\d+) .* SRC=(.*?) DST=(.*?) SPT=(\d+)', line)
                if match:
                    date_time, src_ip, dst_ip, src_port = match.groups()
                    report_data.append([date, time, src_ip, dst_ip, src_port, port])

    df = pd.DataFrame(report_data, columns=['Date', 'Time', 'Source IP Address', 'Destination IP Address', 'Source Port Address', 'Destination Port Address'])
    df.to_csv(f'destination_port_{port}_report.csv', index=False)

    # Get data from records that contain the specified destination port
    # Generate the CSV report
    return

def generate_invalid_user_report():
    """Produces a CSV report of all network traffic in a log file that show
    an attempt to login as an invalid user.
    """
    # TODO: Complete function body per step 10
    report_data = []
    with open(log_path, 'r') as log_file:
        for line in log_file:
            match = re.search(r'(\w+ \d+ \d+:\d+:\d+).*Invalid user (\w+) from (.*?)$', line)
            if match:
                date_time, username, ip_address = match.groups()
                report_data.append([date, time, username, ip_address])

    df = pd.DataFrame(report_data, columns=['Date', 'Time', 'Username', 'IPAddress'])
    df.to_csv('invalid_users.csv', index=False)
    # Get data from records that show attempted invalid user login
    # Generate the CSV report
    return

def generate_source_ip_log(ip_address):
    """Produces a plain text .log file containing all records from a source log
    file that contain a specified source IP address.

    Args:
        ip_address (str): Source IP address
    """
    # TODO: Complete function body per step 11
    
    # Get all records that have the specified sourec IP address
    # Save all records to a plain text .log file
    return

if __name__ == '__main__':
    main()