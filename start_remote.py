#!/usr/bin/env python3
"""
Remote Access Setup for Arthvidya Monopoly
This script configures the game for mobile/remote access via internet
"""

import subprocess
import sys
import time
import socket
import os
import json
from pathlib import Path

class RemoteGameManager:
    def __init__(self):
        self.game_process = None
        self.streamlit_process = None
        self.local_ip = None
        self.public_ip = None
        
    def get_local_ip(self):
        """Get the local IP address"""
        try:
            # Connect to a remote server to get local IP
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
    
    def start_remote_streamlit(self):
        """Start Streamlit with remote access enabled"""
        print("🌐 Starting Remote Streamlit Interface...")
        
        try:
            # Check if secure client exists
            if not Path("streamlit_client_secure.py").exists():
                print("❌ streamlit_client_secure.py not found!")
                print("📋 Using regular client instead...")
                client_file = "streamlit_client.py"
            else:
                client_file = "streamlit_client_secure.py"
                print("🛡️ Password protection enabled!")
            
            port = self.find_free_port()
            print(f"🔌 Using port {port}")
            
            # Start Streamlit with remote access
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
                print(f"✅ Remote Streamlit started successfully!")
                return process, port
            else:
                print("❌ Streamlit failed to start")
                return None, None
                
        except Exception as e:
            print(f"❌ Error starting Streamlit: {e}")
            return None, None
    
    def create_mobile_config(self, port):
        """Create mobile-optimized configuration"""
        config = {
            "local_access": f"http://{self.local_ip}:{port}",
            "public_access": f"http://{self.public_ip}:{port}",
            "port": port,
            "mobile_optimized": True,
            "remote_access": True
        }
        
        try:
            with open("mobile_config.json", 'w') as f:
                json.dump(config, f, indent=2)
            print("✅ Mobile configuration saved")
            return True
        except Exception as e:
            print(f"❌ Error saving mobile config: {e}")
            return False
    
    def display_access_info(self, port):
        """Display access information"""
        print("\n🌐 REMOTE ACCESS INFORMATION:")
        print("=" * 50)
        
        print(f"📱 Mobile Access URLs:")
        print(f"   • Local Network: http://{self.local_ip}:{port}")
        print(f"   • Public Internet: http://{self.public_ip}:{port}")
        
        print(f"\n🔑 Login Information:")
        print(f"   • Control Center: ferrari")
        print(f"   • Team 1: mercedes")
        print(f"   • Team 2: mclaren")
        print(f"   • Team 3: redbull")
        print(f"   • Team 4: audi")
        print(f"   • Team 5: astonmartin")
        
        print(f"\n📋 Instructions:")
        print(f"   1. Connect your mobile to the same WiFi network")
        print(f"   2. Open browser on mobile")
        print(f"   3. Go to: http://{self.local_ip}:{port}")
        print(f"   4. Login with Control Center password: ferrari")
        print(f"   5. Control the game from your mobile!")
        
        print(f"\n🛡️ Security Notes:")
        print(f"   • Only share URLs with authorized players")
        print(f"   • Use strong passwords")
        print(f"   • Close access when done playing")
    
    def run(self):
        """Main run method"""
        print("🌐 Arthvidya Monopoly - Remote Mobile Access")
        print("=" * 60)
        
        # Get network information
        self.local_ip = self.get_local_ip()
        self.public_ip = self.get_public_ip()
        
        print(f"🏠 Local IP: {self.local_ip}")
        print(f"🌍 Public IP: {self.public_ip}")
        
        # Check required files
        required_files = ["main.py"]
        optional_files = ["streamlit_client_secure.py", "streamlit_client.py"]
        
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
        
        # Start remote Streamlit
        streamlit_process, port = self.start_remote_streamlit()
        
        if streamlit_process:
            # Create mobile config
            self.create_mobile_config(port)
            
            # Display access information
            self.display_access_info(port)
            
            print("\n🎉 Remote system running!")
            print("📱 You can now control the game from your mobile device!")
            
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
    manager = RemoteGameManager()
    success = manager.run()
    
    if success:
        print("✅ Remote system shutdown complete")
    else:
        print("❌ Remote system startup failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
