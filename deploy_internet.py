#!/usr/bin/env python3
"""
Internet Deployment Script for Arthvidya Monopoly
This script helps deploy the game for internet access
"""

import subprocess
import sys
import time
import socket
import os
import json
from pathlib import Path

class InternetDeployment:
    def __init__(self):
        self.game_process = None
        self.streamlit_process = None
        self.local_ip = None
        self.public_ip = None
        
    def get_local_ip(self):
        """Get the local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except:
            return "127.0.0.1"
    
    def get_public_ip(self):
        """Get the public IP address"""
        try:
            import urllib.request
            with urllib.request.urlopen('https://api.ipify.org') as response:
                return response.read().decode('utf-8')
        except:
            return "Unable to determine"
    
    def find_free_port(self):
        """Find a free port for Streamlit"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.listen(1)
            port = s.getsockname()[1]
        return port
    
    def start_game(self):
        """Start the pygame game"""
        try:
            print("🎮 Starting Pygame Monopoly Game...")
            self.game_process = subprocess.Popen([
                sys.executable, "main.py"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("✅ Pygame game started successfully!")
            return True
        except Exception as e:
            print(f"❌ Failed to start pygame game: {e}")
            return False
    
    def start_internet_streamlit(self):
        """Start Streamlit with internet access enabled"""
        print("🌐 Starting Internet Streamlit Interface...")
        
        try:
            # Check if mobile client exists
            if not Path("streamlit_mobile.py").exists():
                print("❌ streamlit_mobile.py not found!")
                print("📋 Using secure client instead...")
                client_file = "streamlit_client_secure.py"
            else:
                client_file = "streamlit_mobile.py"
                print("📱 Mobile-optimized interface enabled!")
            
            port = self.find_free_port()
            print(f"🔌 Using port {port}")
            
            # Start Streamlit with internet access
            process = subprocess.Popen([
                sys.executable, "-m", "streamlit", "run", client_file,
                "--server.port", str(port),
                "--server.address", "0.0.0.0",  # Allow external connections
                "--server.headless", "true",
                "--server.enableCORS", "false",
                "--server.enableXsrfProtection", "false"
            ])
            
            # Wait for startup
            print("⏳ Waiting for Streamlit to start...")
            time.sleep(5)
            
            if process.poll() is None:
                print(f"✅ Internet Streamlit started successfully!")
                return process, port
            else:
                print("❌ Streamlit failed to start")
                return None, None
                
        except Exception as e:
            print(f"❌ Error starting Streamlit: {e}")
            return None, None
    
    def create_deployment_config(self, port):
        """Create deployment configuration"""
        config = {
            "local_access": f"http://{self.local_ip}:{port}",
            "public_access": f"http://{self.public_ip}:{port}",
            "port": port,
            "mobile_optimized": True,
            "internet_access": True,
            "deployment_time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open("deployment_config.json", 'w') as f:
                json.dump(config, f, indent=2)
            print("✅ Deployment configuration saved")
            return True
        except Exception as e:
            print(f"❌ Error saving deployment config: {e}")
            return False
    
    def display_deployment_info(self, port):
        """Display deployment information"""
        print("\n🌐 INTERNET DEPLOYMENT INFORMATION:")
        print("=" * 60)
        
        print(f"📱 Access URLs:")
        print(f"   • Local Network: http://{self.local_ip}:{port}")
        print(f"   • Public Internet: http://{self.public_ip}:{port}")
        
        print(f"\n🔑 Login Information:")
        print(f"   • Control Center: ferrari")
        print(f"   • Team 1: mercedes")
        print(f"   • Team 2: mclaren")
        print(f"   • Team 3: redbull")
        print(f"   • Team 4: audi")
        print(f"   • Team 5: astonmartin")
        
        print(f"\n📋 Deployment Instructions:")
        print(f"   1. Share the public URL with remote teams")
        print(f"   2. Teams can access from anywhere with internet")
        print(f"   3. Use Control Center password for game management")
        print(f"   4. Each team uses their own password")
        
        print(f"\n🛡️ Security Notes:")
        print(f"   • Change default passwords before deployment")
        print(f"   • Only share URLs with authorized players")
        print(f"   • Monitor access and game activity")
        print(f"   • Close access when done playing")
        
        print(f"\n🔧 Port Forwarding Required:")
        print(f"   • Forward port {port} to your laptop")
        print(f"   • Configure router settings")
        print(f"   • Allow Python/Streamlit through firewall")
    
    def run(self):
        """Main run method"""
        print("🌐 Arthvidya Monopoly - Internet Deployment")
        print("=" * 60)
        
        # Get network information
        self.local_ip = self.get_local_ip()
        self.public_ip = self.get_public_ip()
        
        print(f"🏠 Local IP: {self.local_ip}")
        print(f"🌍 Public IP: {self.public_ip}")
        
        # Check required files
        required_files = ["main.py"]
        optional_files = ["streamlit_mobile.py", "streamlit_client_secure.py", "streamlit_client.py"]
        
        for file in required_files:
            if not Path(file).exists():
                print(f"❌ Required file not found: {file}")
                return False
        
        # Check for Streamlit client
        streamlit_client = None
        for file in optional_files:
            if Path(file).exists():
                streamlit_client = file
                break
        
        if not streamlit_client:
            print("❌ No Streamlit client found!")
            return False
        
        # Start pygame game
        if not self.start_game():
            return False
        
        # Start internet Streamlit
        streamlit_process, port = self.start_internet_streamlit()
        
        if streamlit_process:
            # Create deployment config
            self.create_deployment_config(port)
            
            # Display deployment information
            self.display_deployment_info(port)
            
            print("\n🎉 Internet deployment running!")
            print("🌐 Remote teams can now access the game!")
            
            # Set up signal handler
            import signal
            def signal_handler(signum, frame):
                print("\n🛑 Shutting down...")
                if self.game_process:
                    self.game_process.terminate()
                if streamlit_process:
                    streamlit_process.terminate()
                sys.exit(0)
            
            signal.signal(signal.SIGINT, signal_handler)
            
            try:
                while True:
                    time.sleep(5)
                    # Check if processes are still running
                    if self.game_process.poll() is not None:
                        print("⚠️ Pygame game process ended")
                        break
                    if streamlit_process.poll() is not None:
                        print("⚠️ Streamlit process ended")
                        break
            except KeyboardInterrupt:
                pass
            
            # Cleanup
            if self.game_process:
                self.game_process.terminate()
                self.game_process.wait()
                print("✅ Pygame game stopped")
            
            if streamlit_process:
                streamlit_process.terminate()
                streamlit_process.wait()
                print("✅ Streamlit interface stopped")
            
            print("✅ Shutdown complete")
        else:
            print("\n⚠️ Streamlit failed, but pygame is running")
            print("🎮 You can still play using the pygame window")
        
        return True

def main():
    """Main function"""
    deployment = InternetDeployment()
    success = deployment.run()
    
    if success:
        print("✅ Internet deployment shutdown complete")
    else:
        print("❌ Internet deployment startup failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
