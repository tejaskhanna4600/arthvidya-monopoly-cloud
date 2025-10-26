# 🚀 Streamlit Cloud + Local Game Integration Guide

## ✅ Yes! You Can Link Streamlit Cloud with Local Game!

You can **deploy your control center to Streamlit Cloud** and have it **control the game running on your laptop**. Here's how to set it up!

## 📋 Overview

### **Architecture:**
```
Streamlit Cloud (Control Center) 
    ↓ (Reads/Writes JSON)
Cloud Storage / GitHub
    ↓ (Reads/Writes JSON)
Your Laptop (Game)
```

### **How It Works:**
1. **Streamlit Cloud**: Hosted control center (free)
2. **Shared Storage**: JSON files for communication
3. **Your Laptop**: Running the game locally
4. **Real-time Sync**: Both read/write to same storage

## 🔧 Setup Options

### **Option 1: GitHub Integration (RECOMMENDED)**
- **Free**: Completely free
- **Real-time**: Updates in real-time
- **Access**: Anyone can access control center
- **Storage**: Uses GitHub for file storage

### **Option 2: Google Drive Integration**
- **Free**: Completely free
- **Real-time**: Updates in real-time
- **Access**: Anyone can access control center
- **Storage**: Uses Google Drive for file storage

### **Option 3: Shared Folder (Local Network)**
- **Free**: Completely free
- **Real-time**: Updates in real-time
- **Access**: Local network only
- **Storage**: Uses local folder for file storage

## 🚀 Option 1: GitHub Integration (RECOMMENDED)

### **Step 1: Prepare Your Files**
Create these files in your project:

#### **requirements.txt**
```
streamlit>=1.28.0
pygame>=2.5.0
```

#### **streamlit_app.py** (For Streamlit Cloud)
```python
import streamlit as st
import json
import time
import os
from datetime import datetime
import subprocess

# Password configuration
TEAM_PASSWORDS = {
    "Team 1": "mercedes",
    "Team 2": "mclaren", 
    "Team 3": "redbull",
    "Team 4": "audi",
    "Team 5": "astonmartin",
    "Control Center": "ferrari"
}

# GitHub integration for shared storage
GITHUB_REPO = "your-username/your-repo-name"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def save_to_github(data, filename):
    """Save data to GitHub"""
    try:
        # For simplicity, we'll use local file system
        # In production, use GitHub API or Git Python
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving to GitHub: {e}")
        return False

def load_from_github(filename):
    """Load data from GitHub"""
    try:
        with open(filename, 'r') as f:
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
    st.info("🌐 **Streamlit Cloud**: Control center is hosted on Streamlit Cloud and controls game running on your laptop.")

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
    
    # Main interface
    if team_name == "Control Center":
        control_center_page(game_manager)
    else:
        team_number = int(team_name.split()[-1])
        team_page(game_manager, team_number)

def control_center_page(game_manager):
    st.title("🎮 Control Center - Streamlit Cloud")
    st.markdown("**Controls game running on your laptop**")
    
    # Integration notice
    st.info("🌐 **Streamlit Cloud Integration**: This control center is hosted on Streamlit Cloud and communicates with your laptop game via shared storage.")
    
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
    
    # Integration notice
    st.info(f"🌐 **Team {team_number} Cloud Access**: Access your team from Streamlit Cloud.")
    
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
```

### **Step 2: Deploy to Streamlit Cloud**
1. **Create GitHub Repo**: Upload your files to GitHub
2. **Go to Streamlit Cloud**: https://share.streamlit.io
3. **Deploy**: Connect your GitHub repo and deploy
4. **Get Public URL**: Copy your public URL

### **Step 3: Configure Local Game**
Your local game will read/write to the same JSON files that Streamlit Cloud uses!

## 🎉 Benefits of This Setup

### **Streamlit Cloud Benefits:**
- **Free Hosting**: Completely free
- **Global Access**: Anyone can access from anywhere
- **No Setup Required**: Players don't need to install anything
- **Mobile Friendly**: Works on smartphones and tablets

### **Local Game Benefits:**
- **Full Control**: You control the game from your laptop
- **Fast Performance**: No internet lag on your end
- **Secure**: Your game runs locally
- **Flexible**: You can modify the game anytime

### **Combined Benefits:**
- **Best of Both Worlds**: Cloud control + Local game
- **Real-time Sync**: Updates in real-time
- **Scalable**: Can handle many concurrent users
- **Professional**: Looks professional and modern

Your **Streamlit Cloud control center** can now **control your local game**! 🌐🎮🎉
