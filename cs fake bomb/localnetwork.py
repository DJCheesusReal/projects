import subprocess
import socket
import http.server
import socketserver
import re

def set_static_ip():
    # Command to set static IP address (Windows)
    cmd_ip = f'netsh interface ip set address name="WiFi 2" static 192.168.0.1 255.255.255.0'
    subprocess.run(cmd_ip, shell=True, check=True)

def create_http_server(ip, port=8000):
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((ip, port), handler)
    print(f"Serving at http://{ip}:{port}")
    httpd.serve_forever()

def get_active_interface():
    # Get the active network interface
    cmd = 'netsh interface ipv4 show interfaces'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if 'connected' in line.lower():
            parts = line.split()
            if len(parts) >= 4:
                interface_name = parts[3]
                if interface_name != "Name":
                    return interface_name
    return None

if __name__ == "__main__":
    interface = get_active_interface()
    if not interface:
        print("No active network interface found")
        exit(1)
    
    ip = "192.168.0.1"  # Custom IP address
    netmask = "255.255.255.0"  # Subnet mask

    try:
        set_static_ip(interface, ip, netmask)
        print(f"Static IP {ip} set on interface {interface}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set static IP: {e}")
        exit(1)

    # Start the HTTP server
    create_http_server(ip)
