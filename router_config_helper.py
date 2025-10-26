#!/usr/bin/env python3
"""
Step-by-Step Router Configuration Script
This script guides you through configuring your router for port forwarding
"""

import socket
import subprocess
import sys
import platform
import urllib.request
import webbrowser
import time

def get_local_ip():
    """Get the local IP address"""
    try:
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
            result = subprocess.run(['ipconfig'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'Default Gateway' in line:
                    return line.split(':')[-1].strip()
        else:
            result = subprocess.run(['route', '-n', 'get', 'default'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'gateway' in line.lower():
                    return line.split(':')[-1].strip()
    except:
        pass
    
    return "192.168.1.1"  # Default fallback

def open_router_admin():
    """Open router admin panel in browser"""
    gateway_ip = get_gateway_ip()
    router_url = f"http://{gateway_ip}"
    
    print(f"🌐 Opening router admin panel: {router_url}")
    print("If this doesn't work, try these common router IPs:")
    print("• 192.168.1.1")
    print("• 192.168.0.1")
    print("• 192.168.2.1")
    print("• 10.0.0.1")
    
    try:
        webbrowser.open(router_url)
        print("✅ Router admin panel opened in browser")
    except:
        print("❌ Could not open browser automatically")
        print(f"Please manually open: {router_url}")

def display_port_forwarding_info():
    """Display port forwarding configuration information"""
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    
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

def guide_router_configuration():
    """Guide user through router configuration"""
    print("\n🔧 Router Configuration Steps:")
    print("=" * 35)
    
    steps = [
        "1. Login to your router admin panel",
        "2. Find 'Port Forwarding' or 'Virtual Server' section",
        "3. Click 'Add' or 'Create New' rule",
        "4. Fill in the port forwarding details (shown above)",
        "5. Save the configuration",
        "6. Restart router if required",
        "7. Test access from another device/network"
    ]
    
    for step in steps:
        print(step)
        input("Press Enter to continue to next step...")
    
    print("\n✅ Router configuration complete!")

def test_access():
    """Test if port forwarding is working"""
    print("\n🧪 Testing Port Forwarding...")
    print("=" * 30)
    
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    
    print("To test port forwarding:")
    print(f"1. Start your Monopoly game")
    print(f"2. Try accessing: http://{local_ip}:8501 (from your laptop)")
    print(f"3. Try accessing: http://{public_ip}:8501 (from another device/network)")
    print("4. If both work, port forwarding is configured correctly!")
    
    test_choice = input("\nWould you like to test now? (y/n): ").strip().lower()
    
    if test_choice == 'y':
        print("\n🌐 Opening test URLs...")
        try:
            webbrowser.open(f"http://{local_ip}:8501")
            print(f"✅ Local test URL opened: http://{local_ip}:8501")
        except:
            print(f"❌ Could not open local test URL")
        
        print(f"📱 Public test URL: http://{public_ip}:8501")
        print("Try accessing this URL from another device/network")

def main():
    """Main function"""
    print("🔧 Router Configuration Helper")
    print("=" * 40)
    
    # Get network information
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    gateway_ip = get_gateway_ip()
    
    print(f"🏠 Your Laptop's IP: {local_ip}")
    print(f"🌍 Your Public IP: {public_ip}")
    print(f"🔌 Your Router's IP: {gateway_ip}")
    
    # Display port forwarding info
    display_port_forwarding_info()
    
    # Open router admin panel
    print("\n🌐 Opening Router Admin Panel...")
    open_router_admin()
    
    # Guide through configuration
    guide_choice = input("\nWould you like step-by-step guidance? (y/n): ").strip().lower()
    
    if guide_choice == 'y':
        guide_router_configuration()
    
    # Test access
    test_access()
    
    print("\n🎉 Configuration Complete!")
    print("=" * 30)
    print("Your Monopoly game should now be accessible from anywhere!")
    print(f"Share this URL with players: http://{public_ip}:8501")
    
    print("\n🛡️ Security Reminders:")
    print("=" * 25)
    print("• Change default passwords before going public")
    print("• Monitor access and game activity")
    print("• Only share URLs with authorized players")
    print("• Consider using VPN for extra security")
    print("• Close access when done playing")

if __name__ == "__main__":
    main()
