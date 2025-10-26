#!/usr/bin/env python3
"""
Port Forwarding Finder for Excitel Routers
This script helps you locate port forwarding options on your router
"""

import webbrowser
import time

def display_port_forwarding_names():
    """Display all possible names for port forwarding"""
    print("🔍 Port Forwarding Alternative Names:")
    print("=" * 45)
    
    names = [
        "Port Forwarding",
        "Virtual Server",
        "NAT Forwarding",
        "Port Mapping",
        "Port Redirection",
        "Firewall Rules",
        "Security Rules",
        "Advanced Rules",
        "Network Rules",
        "WAN Settings",
        "Internet Settings"
    ]
    
    for i, name in enumerate(names, 1):
        print(f"{i:2}. {name}")
    
    print("\n💡 Look for these names in your router's interface!")

def display_search_locations():
    """Display where to search for port forwarding"""
    print("\n🔍 Where to Search for Port Forwarding:")
    print("=" * 40)
    
    locations = [
        "Advanced or Advanced Settings",
        "Network or Network Settings",
        "Security or Security Settings",
        "Firewall or Firewall Settings",
        "NAT or NAT Settings",
        "WAN or WAN Settings",
        "Internet or Internet Settings"
    ]
    
    for i, location in enumerate(locations, 1):
        print(f"{i}. {location}")
    
    print("\n💡 Check each of these sections in your router!")

def display_router_specific_instructions():
    """Display router-specific instructions"""
    print("\n🔧 Router-Specific Instructions:")
    print("=" * 35)
    
    routers = {
        "TP-Link": "Advanced → NAT Forwarding → Port Forwarding",
        "D-Link": "Advanced → Port Forwarding or Virtual Server",
        "Netgear": "Advanced → Port Forwarding or Port Triggering",
        "Linksys": "Smart Wi-Fi Tools → Port Forwarding",
        "ASUS": "Advanced Settings → WAN → Port Forwarding"
    }
    
    for router, path in routers.items():
        print(f"• {router}: {path}")
    
    print("\n💡 Follow the path for your router type!")

def open_router_admin_panels():
    """Open common router admin panel IPs"""
    print("\n🌐 Opening Router Admin Panels:")
    print("=" * 35)
    
    common_ips = ['192.168.1.1', '192.168.0.1', '192.168.2.1', '10.0.0.1']
    
    for ip in common_ips:
        try:
            webbrowser.open(f"http://{ip}")
            print(f"✅ Opened: http://{ip}")
            time.sleep(1)
        except:
            print(f"❌ Could not open: http://{ip}")
    
    print("\n💡 Try each IP address to find your router!")

def display_search_process():
    """Display step-by-step search process"""
    print("\n📋 Step-by-Step Search Process:")
    print("=" * 35)
    
    steps = [
        "1. Login to your router admin panel",
        "2. Look for 'Advanced' or 'Advanced Settings'",
        "3. Check all options in Advanced section",
        "4. Look for 'Port Forwarding' or 'Virtual Server'",
        "5. If not found, check 'Network' section",
        "6. If not found, check 'Security' section",
        "7. If not found, check 'Firewall' section",
        "8. If not found, check 'NAT' section",
        "9. If not found, check 'WAN' section",
        "10. If still not found, contact Excitel support"
    ]
    
    for step in steps:
        print(step)
        input("Press Enter to continue to next step...")
    
    print("\n✅ Search process complete!")

def display_alternative_solutions():
    """Display alternative solutions if port forwarding not found"""
    print("\n🚨 Alternative Solutions:")
    print("=" * 25)
    
    alternatives = [
        "1. Use DMZ (Demilitarized Zone)",
        "2. Use UPnP (Universal Plug and Play)",
        "3. Use Port Triggering",
        "4. Contact Excitel support",
        "5. Check router manual",
        "6. Update router firmware",
        "7. Try different router IPs",
        "8. Use mobile app if available"
    ]
    
    for alternative in alternatives:
        print(alternative)
    
    print("\n💡 Try these alternatives if port forwarding is not available!")

def display_troubleshooting_tips():
    """Display troubleshooting tips"""
    print("\n🔧 Troubleshooting Tips:")
    print("=" * 25)
    
    tips = [
        "• Check router model number",
        "• Update router firmware",
        "• Try different browsers",
        "• Clear browser cache",
        "• Try incognito/private mode",
        "• Check admin access level",
        "• Try different devices",
        "• Contact Excitel support"
    ]
    
    for tip in tips:
        print(tip)
    
    print("\n💡 Try these tips if you're still having trouble!")

def display_contact_information():
    """Display contact information for help"""
    print("\n📞 Contact Information:")
    print("=" * 25)
    
    contacts = [
        "• Excitel Customer Support",
        "• Router Manufacturer Support",
        "• Online Router Manuals",
        "• YouTube Tutorials",
        "• Router Forums",
        "• Excitel Community Forums"
    ]
    
    for contact in contacts:
        print(contact)
    
    print("\n💡 Contact these sources for additional help!")

def main():
    """Main function"""
    print("🔍 Port Forwarding Finder for Excitel Routers")
    print("=" * 50)
    
    # Display port forwarding names
    display_port_forwarding_names()
    
    # Display search locations
    display_search_locations()
    
    # Display router-specific instructions
    display_router_specific_instructions()
    
    # Open router admin panels
    open_choice = input("\nWould you like to open router admin panels? (y/n): ").strip().lower()
    if open_choice == 'y':
        open_router_admin_panels()
    
    # Display search process
    search_choice = input("\nWould you like step-by-step search guidance? (y/n): ").strip().lower()
    if search_choice == 'y':
        display_search_process()
    
    # Display alternative solutions
    display_alternative_solutions()
    
    # Display troubleshooting tips
    display_troubleshooting_tips()
    
    # Display contact information
    display_contact_information()
    
    print("\n🎉 Port Forwarding Search Complete!")
    print("=" * 40)
    print("Follow the instructions above to find port forwarding on your router.")
    print("If you still can't find it, contact Excitel support for help.")
    
    print("\n🛡️ Security Reminders:")
    print("=" * 25)
    print("• Change default passwords before going public")
    print("• Monitor access and game activity")
    print("• Only share URLs with authorized players")
    print("• Consider using VPN for extra security")
    print("• Close access when done playing")

if __name__ == "__main__":
    main()
