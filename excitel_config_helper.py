#!/usr/bin/env python3
"""
Excitel Router Configuration Helper
This script helps you configure your Excitel router for port forwarding
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
    
    return "192.168.1.1"  # Default fallback for Excitel

def open_excitel_router_admin():
    """Open Excitel router admin panel in browser"""
    gateway_ip = get_gateway_ip()
    
    # Common Excitel router IPs
    excitel_ips = ['192.168.1.1', '192.168.0.1', '192.168.2.1', '10.0.0.1']
    
    print(f"🌐 Opening Excitel router admin panel...")
    print(f"Primary IP: {gateway_ip}")
    print("If this doesn't work, try these common Excitel router IPs:")
    for ip in excitel_ips:
        print(f"• {ip}")
    
    # Try primary IP first
    try:
        webbrowser.open(f"http://{gateway_ip}")
        print(f"✅ Router admin panel opened: http://{gateway_ip}")
    except:
        print(f"❌ Could not open browser automatically")
        print(f"Please manually open: http://{gateway_ip}")
    
    # Also try common Excitel IPs
    for ip in excitel_ips:
        if ip != gateway_ip:
            try:
                webbrowser.open(f"http://{ip}")
                print(f"✅ Also opened: http://{ip}")
            except:
                pass

def display_excitel_port_forwarding_info():
    """Display Excitel port forwarding configuration information"""
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    
    print("\n📋 Excitel Port Forwarding Configuration:")
    print("=" * 45)
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
    
    print("\n🔐 Excitel Router Default Credentials:")
    print("=" * 40)
    print("Username: admin")
    print("Password: admin (or password)")
    print("If these don't work, check router label or contact Excitel support")

def guide_excitel_router_configuration():
    """Guide user through Excitel router configuration"""
    print("\n🔧 Excitel Router Configuration Steps:")
    print("=" * 40)
    
    steps = [
        "1. Login to your Excitel router admin panel",
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
    
    print("\n✅ Excitel router configuration complete!")

def test_excitel_access():
    """Test if Excitel port forwarding is working"""
    print("\n🧪 Testing Excitel Port Forwarding...")
    print("=" * 35)
    
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    
    print("To test Excitel port forwarding:")
    print(f"1. Start your Monopoly game")
    print(f"2. Try accessing: http://{local_ip}:8501 (from your laptop)")
    print(f"3. Try accessing: http://{public_ip}:8501 (from another device/network)")
    print("4. If both work, Excitel port forwarding is configured correctly!")
    
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

def excitel_troubleshooting():
    """Excitel-specific troubleshooting tips"""
    print("\n🔍 Excitel Troubleshooting Tips:")
    print("=" * 35)
    
    tips = [
        "• Try different router IPs: 192.168.1.1, 192.168.0.1, 192.168.2.1",
        "• Check if you're connected to Excitel WiFi",
        "• Try different browsers: Chrome, Firefox, Edge",
        "• Check router label for admin credentials",
        "• Contact Excitel support if needed",
        "• Restart router if configuration doesn't work",
        "• Make sure laptop IP address is correct",
        "• Check Windows/Mac firewall settings"
    ]
    
    for tip in tips:
        print(tip)
    
    print("\n📞 Excitel Support:")
    print("=" * 20)
    print("• Contact Excitel customer support")
    print("• Check Excitel's website for help")
    print("• Ask on Excitel community forums")

def main():
    """Main function"""
    print("🌐 Excitel Router Configuration Helper")
    print("=" * 45)
    
    # Get network information
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    gateway_ip = get_gateway_ip()
    
    print(f"🏠 Your Laptop's IP: {local_ip}")
    print(f"🌍 Your Public IP: {public_ip}")
    print(f"🔌 Your Excitel Router's IP: {gateway_ip}")
    
    # Display port forwarding info
    display_excitel_port_forwarding_info()
    
    # Open Excitel router admin panel
    print("\n🌐 Opening Excitel Router Admin Panel...")
    open_excitel_router_admin()
    
    # Guide through configuration
    guide_choice = input("\nWould you like step-by-step guidance? (y/n): ").strip().lower()
    
    if guide_choice == 'y':
        guide_excitel_router_configuration()
    
    # Test access
    test_excitel_access()
    
    # Show troubleshooting tips
    excitel_troubleshooting()
    
    print("\n🎉 Excitel Configuration Complete!")
    print("=" * 35)
    print("Your Monopoly game should now be accessible from anywhere!")
    print(f"Share this URL with players: http://{public_ip}:8501")
    
    print("\n🛡️ Security Reminders:")
    print("=" * 25)
    print("• Change default passwords before going public")
    print("• Monitor access and game activity")
    print("• Only share URLs with authorized players")
    print("• Consider using VPN for extra security")
    print("• Close access when done playing")
    
    print("\n📞 Need Help?")
    print("=" * 15)
    print("• Check EXCITEL_ROUTER_GUIDE.md for detailed instructions")
    print("• Contact Excitel support for router issues")
    print("• Try common router IPs if you can't access admin panel")
    print("• Make sure you're connected to Excitel WiFi")

if __name__ == "__main__":
    main()
