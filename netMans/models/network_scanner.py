import subprocess
import socket

def get_local_ip_range():
    # Get the IP address of the current machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()

    # Extract network prefix (subnet mask) from the local IP address
    network_prefix = local_ip.rsplit('.', 1)[0] + '.0/24'

    return network_prefix

def scan_network(ip):
    nmap_output = subprocess.run(["nmap", "-A", ip], capture_output=True, text=True)
    devices_list = []
    current_device = None
    for line in nmap_output.stdout.split('\n'):
        if "Nmap scan report for" in line:
            if current_device:
                devices_list.append(current_device)
            current_device = {"ip": line.split()[-1], "details": []}
        elif "MAC Address" in line:
            current_device["mac"] = line.split()[2]
        elif "Host is up" in line:
            current_device["status"] = "Up"
        elif "Host seems down" in line:
            current_device["status"] = "Down"
        elif "OS details" in line:
            try:
                current_device["os"] = line.split(": ")[1].strip()
            except IndexError:
                current_device["os"] = "Unknown"
        elif "Service Info" in line:
            current_device["services"] = line.split(": ")[1].strip()
        elif "Device type" in line:
            current_device["type"] = line.split(": ")[1].strip()
    if current_device:
        devices_list.append(current_device)
    return devices_list

