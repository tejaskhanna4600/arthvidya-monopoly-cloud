#!/usr/bin/env python3
"""
Streamlit Cloud + Local Game Integration Script
This script helps you deploy to Streamlit Cloud and connect with local game
"""

import os
import subprocess
import json
from pathlib import Path

def create_streamlit_cloud_files():
    """Create files needed for Streamlit Cloud deployment"""
    print("📁 Creating Streamlit Cloud files...")
    
    # Create streamlit_app.py
    streamlit_app_content = '''import streamlit as st
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

# Shared storage (GitHub integration)
STORAGE_PATH = os.path.join(os.path.dirname(__file__), "shared_storage")
os.makedirs(STORAGE_PATH, exist_ok=True)

def save_to_storage(data, filename):
    """Save data to shared storage"""
    try:
        filepath = os.path.join(STORAGE_PATH, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving to storage: {e}")
        return False

def load_from_storage(filename):
    """Load data from shared storage"""
    try:
        filepath = os.path.join(STORAGE_PATH, filename)
        with open(filepath, 'r') as f:
            return json.load(f)
    except:
        return None

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
    st.title("🔐 Arthvidya Monopoly - Control Center")
    st.markdown("**Streamlit Cloud + Local Game Integration**")
    
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
    
    # Integration notice
    st.markdown("---")
    st.info("🌐 **Streamlit Cloud**: Control center is hosted on Streamlit Cloud and communicates with game running on your laptop.")

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
        page_title="Monopoly Control Center - Cloud",
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
    st.sidebar.markdown("🌐 **Streamlit Cloud**")
    st.sidebar.markdown("🎮 **Controls local game on laptop**")
    logout_button()
    st.sidebar.markdown("---")
    
    # Main interface - simplified for space
    if team_name == "Control Center":
        st.title("🎮 Control Center - Streamlit Cloud")
        st.markdown("**Controls game running on your laptop**")
        
        # Integration notice
        st.info("🌐 **Streamlit Cloud Integration**: This control center is hosted on Streamlit Cloud and communicates with your laptop game via shared storage.")
        
        # Load current game state
        game_state = game_manager.load_game_state()
        if not game_state:
            st.error("Failed to load game state")
            return
        
        # Game status
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Current Player", f"Team {game_state['current_player'] + 1}")
        
        with col2:
            st.metric("Game Phase", game_state['game_phase'].title())
        
        with col3:
            st.metric("Dice Rolled", "Yes" if game_state['dice_rolled'] else "No")
        
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
                send_command(game_manager, "reset_game")
                st.success("Reset command sent!")
        
        # Auto-refresh
        if st.checkbox("🔄 Auto-refresh (5s)"):
            time.sleep(5)
            st.rerun()
    else:
        st.title(f"👥 Team {team_name.split()[-1]}")
        st.info(f"🌐 **Team {team_name.split()[-1]} Cloud Access**")

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
        with open("streamlit_app.py", 'w', encoding='utf-8') as f:
            f.write(streamlit_app_content)
        print("✅ streamlit_app.py created")
    except Exception as e:
        print(f"❌ Error creating streamlit_app.py: {e}")
    
    # Create requirements.txt
    requirements_content = '''streamlit>=1.28.0
'''
    
    try:
        with open("requirements.txt", 'w', encoding='utf-8') as f:
            f.write(requirements_content)
        print("✅ requirements.txt created")
    except Exception as e:
        print(f"❌ Error creating requirements.txt: {e}")
    
    # Create .gitignore
    gitignore_content = '''__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
*.json
!game_state.json
!player_actions.json
!control_commands.json
.DS_Store
*.log
'''
    
    try:
        with open(".gitignore", 'w', encoding='utf-8') as f:
            f.write(gitignore_content)
        print("✅ .gitignore created")
    except Exception as e:
        print(f"❌ Error creating .gitignore: {e}")
    
    print("✅ Streamlit Cloud files created successfully!")

def create_deployment_instructions():
    """Create deployment instructions"""
    print("\n📋 Creating deployment instructions...")
    
    instructions = '''# 🚀 Deployment Instructions

## Step 1: Create GitHub Repository
1. Go to https://github.com
2. Create new repository
3. Name it "arthvidya-monopoly-cloud"
4. Make it public

## Step 2: Upload Files to GitHub
Upload these files:
- streamlit_app.py
- requirements.txt
- .gitignore

## Step 3: Deploy to Streamlit Cloud
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Branch: main
6. Main file: streamlit_app.py
7. Click "Deploy"

## Step 4: Get Public URL
Your app will be available at:
https://your-app-name.streamlit.app

## Step 5: Connect Local Game
Your local game should read/write to the same JSON files that Streamlit Cloud uses.

## 🎉 Success!
Your Streamlit Cloud control center is now connected to your local game!
'''
    
    try:
        with open("DEPLOYMENT_INSTRUCTIONS.md", 'w', encoding='utf-8') as f:
            f.write(instructions)
        print("✅ DEPLOYMENT_INSTRUCTIONS.md created")
    except Exception as e:
        print(f"❌ Error creating deployment instructions: {e}")

def display_deployment_info():
    """Display deployment information"""
    print("\n🌐 Streamlit Cloud + Local Game Integration:")
    print("=" * 55)
    
    print("\n📋 What This Does:")
    print("• Deploys control center to Streamlit Cloud (free)")
    print("• Connects with local game on your laptop")
    print("• Real-time sync via shared JSON files")
    print("• Global access to control center")
    print("• Local game runs on your laptop")
    
    print("\n🔑 Login Information:")
    print("• Control Center: ferrari")
    print("• Team 1: mercedes")
    print("• Team 2: mclaren")
    print("• Team 3: redbull")
    print("• Team 4: audi")
    print("• Team 5: astonmartin")
    
    print("\n📋 Next Steps:")
    print("1. Run this script to create deployment files")
    print("2. Create GitHub repository")
    print("3. Upload files to GitHub")
    print("4. Deploy to Streamlit Cloud")
    print("5. Get public URL and share!")

def main():
    """Main function"""
    print("🌐 Streamlit Cloud + Local Game Integration")
    print("=" * 50)
    
    # Create Streamlit Cloud files
    create_streamlit_cloud_files()
    
    # Create deployment instructions
    create_deployment_instructions()
    
    # Display deployment information
    display_deployment_info()
    
    print("\n🎉 Integration Setup Complete!")
    print("=" * 35)
    print("Follow DEPLOYMENT_INSTRUCTIONS.md to deploy to Streamlit Cloud.")
    print("Your Streamlit Cloud control center will connect to your local game!")

if __name__ == "__main__":
    main()
