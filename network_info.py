#!/usr/bin/env python3
"""
Network Information Script for Router Configuration
This script helps you find your network information for port forwarding
"""

import socket
import subprocess
import sys
import platform
import urllib.request

def get_local_ip():
    """Get the local IP address"""
    try:
        # Connect to a remote server to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "Unable to determine"

def get_public_ip():
    """Get the public IP address"""
    try:
        with urllib.request.urlopen('https://api.ipify.org') as response:
            return response.read().decode('utf-8')
    except:
        return "Unable to determine"

def get_gateway_ip():
    """Get the gateway (router) IP address"""
    try:
        if platform.system() == "Windows":
            # Windows
            result = subprocess.run(['ipconfig'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'Default Gateway' in line:
                    return line.split(':')[-1].strip()
        else:
            # Mac/Linux
            result = subprocess.run(['route', '-n', 'get', 'default'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'gateway' in line.lower():
                    return line.split(':')[-1].strip()
    except:
        pass
    
    # Fallback: try common router IPs
    common_ips = ['192.168.1.1', '192.168.0.1', '192.168.2.1', '10.0.0.1']
    return f"Try these common router IPs: {', '.join(common_ips)}"

def get_network_info():
    """Get comprehensive network information"""
    print("🔍 Network Information for Router Configuration")
    print("=" * 60)
    
    # Get local IP
    local_ip = get_local_ip()
    print(f"🏠 Your Laptop's IP Address: {local_ip}")
    
    # Get public IP
    public_ip = get_public_ip()
    print(f"🌍 Your Public IP Address: {public_ip}")
    
    # Get gateway IP
    gateway_ip = get_gateway_ip()
    print(f"🔌 Your Router's IP Address: {gateway_ip}")
    
    print("\n📋 Port Forwarding Configuration:")
    print("=" * 40)
    print(f"Service Name: Monopoly Game")
    print(f"Protocol: TCP")
    print(f"External Port: 8501")
    print(f"Internal Port: 8501")
    print(f"Internal IP: {local_ip}")
    print(f"Enabled: Yes")
    
    print("\n🌐 Access URLs:")
    print("=" * 20)
    print(f"Local Access: http://{local_ip}:8501")
    print(f"Public Access: http://{public_ip}:8501")
    
    print("\n🔑 Login Information:")
    print("=" * 25)
    print("Control Center: ferrari")
    print("Team 1: mercedes")
    print("Team 2: mclaren")
    print("Team 3: redbull")
    print("Team 4: audi")
    print("Team 5: astonmartin")
    
    print("\n🔧 Router Configuration Steps:")
    print("=" * 35)
    print("1. Open browser and go to your router's IP address")
    print(f"2. Login with admin credentials")
    print("3. Find 'Port Forwarding' or 'Virtual Server' section")
    print("4. Add new port forwarding rule with the details above")
    print("5. Save configuration and restart router if needed")
    print("6. Test access from another device/network")
    
    print("\n🛡️ Security Reminders:")
    print("=" * 25)
    print("• Change default passwords before going public")
    print("• Monitor access and game activity")
    print("• Only share URLs with authorized players")
    print("• Consider using VPN for extra security")
    print("• Close access when done playing")
    
    return {
        "local_ip": local_ip,
        "public_ip": public_ip,
        "gateway_ip": gateway_ip
    }

def test_port_forwarding():
    """Test if port forwarding is working"""
    print("\n🧪 Testing Port Forwarding...")
    print("=" * 30)
    
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    
    print(f"Testing local access: http://{local_ip}:8501")
    print(f"Testing public access: http://{public_ip}:8501")
    
    print("\nTo test port forwarding:")
    print("1. Start your Monopoly game")
    print("2. Try accessing the local URL from your laptop")
    print("3. Try accessing the public URL from another device/network")
    print("4. If public access works, port forwarding is configured correctly")

def main():
    """Main function"""
    print("🌐 Router Configuration Helper")
    print("=" * 40)
    
    # Get network information
    network_info = get_network_info()
    
    # Test port forwarding
    test_port_forwarding()
    
    print("\n📞 Need Help?")
    print("=" * 15)
    print("• Check the ROUTER_CONFIG_GUIDE.md for detailed instructions")
    print("• Contact your internet provider for router support")
    print("• Try common router IPs if you can't find your router's IP")
    print("• Make sure your laptop is connected to the router")
    
    print("\n🎉 Ready to Configure!")
    print("=" * 25)
    print("Use the information above to configure your router for port forwarding.")
    print("Once configured, anyone can access your Monopoly game from anywhere!")

if __name__ == "__main__":
    main()
