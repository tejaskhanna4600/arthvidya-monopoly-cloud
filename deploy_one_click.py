#!/usr/bin/env python3
"""
One-Click Public Deployment for Arthvidya Monopoly
This script sets up everything needed for public internet access
"""

import subprocess
import sys
import time
import socket
import os
import json
from pathlib import Path

class OneClickDeployment:
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
    
    def create_requirements_file(self):
        """Create requirements.txt for deployment"""
        requirements = """streamlit>=1.28.0
pygame>=2.5.0
"""
        try:
            with open("requirements.txt", 'w') as f:
                f.write(requirements)
            print("✅ requirements.txt created")
            return True
        except Exception as e:
            print(f"❌ Error creating requirements.txt: {e}")
            return False
    
    def create_streamlit_config(self):
        """Create .streamlit/config.toml"""
        config_dir = Path(".streamlit")
        config_dir.mkdir(exist_ok=True)
        
        config_content = """[server]
port = 8501
address = "0.0.0.0"
headless = true
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false
"""
        try:
            with open(".streamlit/config.toml", 'w') as f:
                f.write(config_content)
            print("✅ Streamlit config created")
            return True
        except Exception as e:
            print(f"❌ Error creating Streamlit config: {e}")
            return False
    
    def create_streamlit_app(self):
        """Create streamlit_app.py for cloud deployment"""
        app_content = '''import streamlit as st
import json
import time
import os
from datetime import datetime

# Password configuration
TEAM_PASSWORDS = {
    "Team 1": "mercedes",
    "Team 2": "mclaren", 
    "Team 3": "redbull",
    "Team 4": "audi",
    "Team 5": "astonmartin",
    "Control Center": "ferrari"
}

# Game state management
class GameStateManager:
    def __init__(self):
        self.game_state_file = "game_state.json"
        self.player_actions_file = "player_actions.json"
        self.control_commands_file = "control_commands.json"
        self.init_files()
    
    def init_files(self):
        """Initialize the JSON files for game state and communication"""
        if not os.path.exists(self.game_state_file):
            self.save_game_state({
                "current_player": 0,
                "game_phase": "waiting",
                "dice_rolled": False,
                "current_position": 0,
                "properties": {},
                "teams": [
                    {"id": "T1", "name": "Team 1", "color": "#D32F2F", "balance": 10000000, "pos": 0},
                    {"id": "T2", "name": "Team 2", "color": "#1976D2", "balance": 10000000, "pos": 0},
                    {"id": "T3", "name": "Team 3", "color": "#388E3C", "balance": 10000000, "pos": 0},
                    {"id": "T4", "name": "Team 4", "color": "#F57C00", "balance": 10000000, "pos": 0},
                    {"id": "T5", "name": "Team 5", "color": "#7B1FA2", "balance": 10000000, "pos": 0}
                ],
                "messages": [],
                "pending_actions": {},
                "game_log": []
            })
        
        if not os.path.exists(self.player_actions_file):
            self.save_player_actions({})
        
        if not os.path.exists(self.control_commands_file):
            self.save_control_commands({})
    
    def save_game_state(self, state):
        """Save game state to JSON file"""
        with open(self.game_state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_game_state(self):
        """Load game state from JSON file"""
        try:
            with open(self.game_state_file, 'r') as f:
                return json.load(f)
        except:
            return None
    
    def save_player_actions(self, actions):
        """Save player actions to JSON file"""
        with open(self.player_actions_file, 'w') as f:
            json.dump(actions, f, indent=2)
    
    def load_player_actions(self):
        """Load player actions from JSON file"""
        try:
            with open(self.player_actions_file, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def save_control_commands(self, commands):
        """Save control commands to JSON file"""
        with open(self.control_commands_file, 'w') as f:
            json.dump(commands, f, indent=2)
    
    def load_control_commands(self):
        """Load control commands from JSON file"""
        try:
            with open(self.control_commands_file, 'r') as f:
                return json.load(f)
        except:
            return {}

# Authentication functions
def authenticate_user(team_name, password):
    """Authenticate a user with team name and password"""
    if team_name in TEAM_PASSWORDS:
        return password == TEAM_PASSWORDS[team_name]
    return False

def check_authentication():
    """Check if user is authenticated"""
    return st.session_state.get('authenticated', False)

def login_page():
    """Display login page"""
    st.title("🔐 Arthvidya Monopoly")
    st.markdown("**Public Internet Access**")
    
    # Login form
    with st.form("login_form"):
        team_name = st.selectbox(
            "Select Your Team",
            ["Control Center", "Team 1", "Team 2", "Team 3", "Team 4", "Team 5"]
        )
        
        password = st.text_input("Enter Password", type="password")
        
        submitted = st.form_submit_button("🔓 Login", type="primary")
        
        if submitted:
            if authenticate_user(team_name, password):
                st.session_state['authenticated'] = True
                st.session_state['team_name'] = team_name
                st.session_state['team_id'] = team_name.replace("Team ", "T") if team_name.startswith("Team") else "ADMIN"
                st.success(f"✅ Successfully logged in as {team_name}!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Invalid password. Please try again.")
    
    # Public access notice
    st.markdown("---")
    st.info("🌐 **Public Access**: This game is accessible from anywhere on the internet!")

def logout_button():
    """Display logout button"""
    if st.button("🚪 Logout", type="secondary"):
        st.session_state['authenticated'] = False
        st.session_state['team_name'] = None
        st.session_state['team_id'] = None
        st.rerun()

# Initialize the game state manager
@st.cache_resource
def get_game_manager():
    return GameStateManager()

def main():
    st.set_page_config(
        page_title="Arthvidya Monopoly - Public Access",
        page_icon="🌐",
        layout="wide"
    )
    
    game_manager = get_game_manager()
    
    # Check authentication
    if not check_authentication():
        login_page()
        return
    
    # User is authenticated, show the main interface
    team_name = st.session_state.get('team_name', 'Unknown')
    team_id = st.session_state.get('team_id', 'UNKNOWN')
    
    # Sidebar
    st.sidebar.title(f"🔐 {team_name}")
    st.sidebar.markdown(f"**Team ID:** {team_id}")
    logout_button()
    st.sidebar.markdown("---")
    
    # Main interface based on team
    if team_name == "Control Center":
        control_center_page(game_manager)
    else:
        team_number = int(team_name.split()[-1])
        team_page(game_manager, team_number)

def control_center_page(game_manager):
    st.title("🎮 Control Center")
    st.markdown("**Public Game Master Interface**")
    
    # Public access notice
    st.info("🌐 **Public Control**: You can control the game from anywhere on the internet!")
    
    # Load current game state
    game_state = game_manager.load_game_state()
    if not game_state:
        st.error("Failed to load game state")
        return
    
    # Game status overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Player", f"Team {game_state['current_player'] + 1}")
    
    with col2:
        st.metric("Game Phase", game_state['game_phase'].title())
    
    with col3:
        st.metric("Dice Rolled", "Yes" if game_state['dice_rolled'] else "No")
    
    st.markdown("---")
    
    # Team status
    st.subheader("👥 Team Status")
    teams_cols = st.columns(5)
    
    for i, team in enumerate(game_state['teams']):
        with teams_cols[i]:
            st.markdown(f"**{team['name']}**")
            st.markdown(f"💰 ₹{team['balance']:,}")
            st.markdown(f"📍 Position: {team['pos']}")
            
            # Highlight current player
            if i == game_state['current_player']:
                st.success("🎯 Current Turn")
    
    st.markdown("---")
    
    # Game controls
    st.subheader("🎮 Game Controls")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎲 Roll Dice", type="primary"):
            send_command(game_manager, "roll_dice")
            st.success("Dice roll command sent!")
    
    with col2:
        if st.button("⏭️ Next Turn"):
            send_command(game_manager, "next_turn")
            st.success("Next turn command sent!")
    
    with col3:
        if st.button("🔄 Reset Game"):
            if st.button("⚠️ Confirm Reset", type="secondary"):
                send_command(game_manager, "reset_game")
                st.success("Reset command sent!")
    
    # Property management
    st.subheader("🏠 Property Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏠 Buy Property"):
            send_command(game_manager, "buy_property")
            st.success("Buy property command sent!")
    
    with col2:
        if st.button("💰 Sell Property"):
            send_command(game_manager, "sell_property")
            st.success("Sell property command sent!")
    
    # Special actions
    st.subheader("🎯 Special Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎲 Test Chance"):
            send_command(game_manager, "test_chance")
            st.success("Test chance command sent!")
    
    with col2:
        if st.button("🔮 Test Mystery"):
            send_command(game_manager, "test_mystery")
            st.success("Test mystery command sent!")
    
    with col3:
        if st.button("🤝 Start Trading"):
            send_command(game_manager, "start_trading")
            st.success("Start trading command sent!")
    
    # Player actions monitoring
    st.subheader("📋 Player Actions")
    
    player_actions = game_manager.load_player_actions()
    
    if player_actions:
        for team_id, action in player_actions.items():
            team_name = next((t['name'] for t in game_state['teams'] if t['id'] == team_id), team_id)
            st.info(f"**{team_name}**: {action}")
    else:
        st.info("No pending player actions")
    
    # Game log
    st.subheader("📜 Game Log")
    
    if game_state['game_log']:
        for log_entry in reversed(game_state['game_log'][-10:]):  # Show last 10 entries
            timestamp = log_entry.get('timestamp', '')
            message = log_entry.get('message', '')
            st.text(f"[{timestamp}] {message}")
    else:
        st.info("No game log entries yet")
    
    # Auto-refresh
    if st.checkbox("🔄 Auto-refresh (5s)"):
        time.sleep(5)
        st.rerun()

def team_page(game_manager, team_number):
    st.title(f"👥 Team {team_number}")
    
    # Public access notice
    st.info(f"🌐 **Team {team_number} Public Access**: Access your team from anywhere on the internet!")
    
    # Load current game state
    game_state = game_manager.load_game_state()
    if not game_state:
        st.error("Failed to load game state")
        return
    
    team_id = f"T{team_number}"
    team = next((t for t in game_state['teams'] if t['id'] == team_id), None)
    
    if not team:
        st.error(f"Team {team_number} not found")
        return
    
    # Team info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("💰 Balance", f"₹{team['balance']:,}")
    
    with col2:
        st.metric("📍 Position", team['pos'])
    
    with col3:
        is_current = game_state['current_player'] == (team_number - 1)
        st.metric("🎯 Status", "Your Turn" if is_current else "Waiting")
    
    # Current player actions
    if is_current:
        st.success("🎯 It's your turn!")
        
        # Action buttons
        st.subheader("🎮 Your Actions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎲 Roll Dice", type="primary"):
                send_player_action(game_manager, team_id, "roll_dice")
                st.success("Dice roll requested!")
        
        with col2:
            if st.button("⏭️ End Turn"):
                send_player_action(game_manager, team_id, "end_turn")
                st.success("End turn requested!")
        
        # Property actions
        st.subheader("🏠 Property Actions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🏠 Buy Property"):
                send_player_action(game_manager, team_id, "buy_property")
                st.success("Buy property requested!")
        
        with col2:
            if st.button("💰 Sell Property"):
                send_player_action(game_manager, team_id, "sell_property")
                st.success("Sell property requested!")
        
        # Special actions
        st.subheader("🎯 Special Actions")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎲 Take Chance"):
                send_player_action(game_manager, team_id, "take_chance")
                st.success("Take chance requested!")
        
        with col2:
            if st.button("🔮 Spin Mystery"):
            send_player_action(game_manager, team_id, "spin_mystery")
            st.success("Spin mystery requested!")
        
        with col3:
            if st.button("🤝 Start Trading"):
                send_player_action(game_manager, team_id, "start_trading")
                st.success("Start trading requested!")
    
    else:
        st.info(f"⏳ Waiting for Team {game_state['current_player'] + 1}'s turn")
    
    # Team properties
    st.subheader("🏠 Your Properties")
    st.info("Property list will be implemented based on game state")
    
    # Game messages
    st.subheader("💬 Game Messages")
    
    messages = game_state.get('messages', [])
    if messages:
        for message in reversed(messages[-5:]):  # Show last 5 messages
            timestamp = message.get('timestamp', '')
            text = message.get('message', '')
            st.text(f"[{timestamp}] {text}")
    else:
        st.info("No messages yet")
    
    # Auto-refresh
    if st.checkbox("🔄 Auto-refresh (3s)"):
        time.sleep(3)
        st.rerun()

def send_command(game_manager, command):
    """Send a command from the control center"""
    commands = game_manager.load_control_commands()
    commands[datetime.now().isoformat()] = {
        "command": command,
        "timestamp": datetime.now().isoformat(),
        "source": "control_center"
    }
    game_manager.save_control_commands(commands)

def send_player_action(game_manager, team_id, action):
    """Send a player action"""
    actions = game_manager.load_player_actions()
    actions[team_id] = {
        "action": action,
        "timestamp": datetime.now().isoformat(),
        "team_id": team_id
    }
    game_manager.save_player_actions(actions)

if __name__ == "__main__":
    main()
'''
        try:
            with open("streamlit_app.py", 'w') as f:
                f.write(app_content)
            print("✅ streamlit_app.py created")
            return True
        except Exception as e:
            print(f"❌ Error creating streamlit_app.py: {e}")
            return False
    
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
    
    def start_public_streamlit(self):
        """Start Streamlit with public internet access"""
        print("🌐 Starting Public Streamlit Interface...")
        
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
            
            # Start Streamlit with public access
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
                print(f"✅ Public Streamlit started successfully!")
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
            "public_access": True,
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
        print("\n🌐 PUBLIC INTERNET DEPLOYMENT:")
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
        print(f"   1. Share the public URL with anyone")
        print(f"   2. Anyone can access from anywhere with internet")
        print(f"   3. Use Control Center password for game management")
        print(f"   4. Each team uses their own password")
        
        print(f"\n🛡️ Security Notes:")
        print(f"   • Change default passwords before public deployment")
        print(f"   • Only share URLs with authorized players")
        print(f"   • Monitor access and game activity")
        print(f"   • Close access when done playing")
        
        print(f"\n🔧 Port Forwarding Required:")
        print(f"   • Forward port {port} to your laptop")
        print(f"   • Configure router settings")
        print(f"   • Allow Python/Streamlit through firewall")
        
        print(f"\n📱 Mobile Access:")
        print(f"   • Optimized for mobile devices")
        print(f"   • Works on any smartphone/tablet")
        print(f"   • Touch-friendly interface")
        print(f"   • Responsive design")
    
    def run(self):
        """Main run method"""
        print("🌐 Arthvidya Monopoly - One-Click Public Deployment")
        print("=" * 60)
        
        # Get network information
        self.local_ip = self.get_local_ip()
        self.public_ip = self.get_public_ip()
        
        print(f"🏠 Local IP: {self.local_ip}")
        print(f"🌍 Public IP: {self.public_ip}")
        
        # Create deployment files
        print("\n📁 Creating deployment files...")
        self.create_requirements_file()
        self.create_streamlit_config()
        self.create_streamlit_app()
        
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
        
        # Start public Streamlit
        streamlit_process, port = self.start_public_streamlit()
        
        if streamlit_process:
            # Create deployment config
            self.create_deployment_config(port)
            
            # Display deployment information
            self.display_deployment_info(port)
            
            print("\n🎉 Public deployment running!")
            print("🌐 Anyone can now access the game from anywhere!")
            
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
    deployment = OneClickDeployment()
    success = deployment.run()
    
    if success:
        print("✅ One-click deployment shutdown complete")
    else:
        print("❌ One-click deployment startup failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
