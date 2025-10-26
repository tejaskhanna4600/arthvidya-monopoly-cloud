import streamlit as st
import json
import time
import threading
import queue
import os
import hashlib
from datetime import datetime
import subprocess
import sys

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
    """Display mobile-optimized login page"""
    st.title("🔐 Monopoly Mobile")
    st.markdown("**Secure Team Access**")
    
    # Mobile-friendly login form
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
    
    # Mobile optimization notice
    st.markdown("---")
    st.info("📱 **Mobile Optimized**: This interface is designed for mobile devices and remote access.")

def logout_button():
    """Display mobile-friendly logout button"""
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
        page_title="Monopoly Mobile",
        page_icon="📱",
        layout="wide",
        initial_sidebar_state="collapsed"  # Mobile-friendly sidebar
    )
    
    game_manager = get_game_manager()
    
    # Check authentication
    if not check_authentication():
        login_page()
        return
    
    # User is authenticated, show the main interface
    team_name = st.session_state.get('team_name', 'Unknown')
    team_id = st.session_state.get('team_id', 'UNKNOWN')
    
    # Mobile-friendly sidebar
    with st.sidebar:
        st.title(f"🔐 {team_name}")
        st.markdown(f"**Team ID:** {team_id}")
        logout_button()
        st.markdown("---")
    
    # Main interface based on team
    if team_name == "Control Center":
        mobile_control_center_page(game_manager)
    else:
        team_number = int(team_name.split()[-1])
        mobile_team_page(game_manager, team_number)

def mobile_control_center_page(game_manager):
    st.title("🎮 Control Center")
    st.markdown("**Mobile Game Master Interface**")
    
    # Mobile optimization notice
    st.info("📱 **Mobile Control**: You can control the game from your mobile device!")
    
    # Load current game state
    game_state = game_manager.load_game_state()
    if not game_state:
        st.error("Failed to load game state")
        return
    
    # Mobile-friendly game status
    st.subheader("📊 Game Status")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Current Player", f"Team {game_state['current_player'] + 1}")
        st.metric("Game Phase", game_state['game_phase'].title())
    
    with col2:
        st.metric("Dice Rolled", "Yes" if game_state['dice_rolled'] else "No")
        st.metric("Current Position", game_state['current_position'])
    
    st.markdown("---")
    
    # Mobile-friendly team status
    st.subheader("👥 Team Status")
    
    for i, team in enumerate(game_state['teams']):
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.markdown(f"**{team['name']}**")
        
        with col2:
            st.markdown(f"💰 ₹{team['balance']:,}")
        
        with col3:
            st.markdown(f"📍 {team['pos']}")
        
        # Highlight current player
        if i == game_state['current_player']:
            st.success("🎯 Current Turn")
        
        st.markdown("---")
    
    # Mobile-friendly game controls
    st.subheader("🎮 Game Controls")
    
    # Primary controls
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎲 Roll Dice", type="primary", use_container_width=True):
            send_command(game_manager, "roll_dice")
            st.success("Dice roll command sent!")
    
    with col2:
        if st.button("⏭️ Next Turn", use_container_width=True):
            send_command(game_manager, "next_turn")
            st.success("Next turn command sent!")
    
    # Secondary controls
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏠 Buy Property", use_container_width=True):
            send_command(game_manager, "buy_property")
            st.success("Buy property command sent!")
    
    with col2:
        if st.button("💰 Sell Property", use_container_width=True):
            send_command(game_manager, "sell_property")
            st.success("Sell property command sent!")
    
    # Special actions
    st.subheader("🎯 Special Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎲 Test Chance", use_container_width=True):
            send_command(game_manager, "test_chance")
            st.success("Test chance command sent!")
    
    with col2:
        if st.button("🔮 Test Mystery", use_container_width=True):
            send_command(game_manager, "test_mystery")
            st.success("Test mystery command sent!")
    
    with col3:
        if st.button("🤝 Start Trading", use_container_width=True):
            send_command(game_manager, "start_trading")
            st.success("Start trading command sent!")
    
    # Reset game
    st.subheader("🔄 Game Management")
    
    if st.button("🔄 Reset Game", type="secondary", use_container_width=True):
        if st.button("⚠️ Confirm Reset", type="secondary", use_container_width=True):
            send_command(game_manager, "reset_game")
            st.success("Reset command sent!")
    
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
        for log_entry in reversed(game_state['game_log'][-5:]):  # Show last 5 entries
            timestamp = log_entry.get('timestamp', '')
            message = log_entry.get('message', '')
            st.text(f"[{timestamp}] {message}")
    else:
        st.info("No game log entries yet")
    
    # Auto-refresh
    if st.checkbox("🔄 Auto-refresh (5s)"):
        time.sleep(5)
        st.rerun()

def mobile_team_page(game_manager, team_number):
    st.title(f"👥 Team {team_number}")
    
    # Mobile optimization notice
    st.info(f"📱 **Team {team_number} Mobile Access**: Control your team from your mobile device!")
    
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
    
    # Mobile-friendly team info
    st.subheader("📊 Your Status")
    
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
        
        # Mobile-friendly action buttons
        st.subheader("🎮 Your Actions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎲 Roll Dice", type="primary", use_container_width=True):
                send_player_action(game_manager, team_id, "roll_dice")
                st.success("Dice roll requested!")
        
        with col2:
            if st.button("⏭️ End Turn", use_container_width=True):
                send_player_action(game_manager, team_id, "end_turn")
                st.success("End turn requested!")
        
        # Property actions
        st.subheader("🏠 Property Actions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🏠 Buy Property", use_container_width=True):
                send_player_action(game_manager, team_id, "buy_property")
                st.success("Buy property requested!")
        
        with col2:
            if st.button("💰 Sell Property", use_container_width=True):
                send_player_action(game_manager, team_id, "sell_property")
                st.success("Sell property requested!")
        
        # Special actions
        st.subheader("🎯 Special Actions")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎲 Take Chance", use_container_width=True):
                send_player_action(game_manager, team_id, "take_chance")
                st.success("Take chance requested!")
        
        with col2:
            if st.button("🔮 Spin Mystery", use_container_width=True):
                send_player_action(game_manager, team_id, "spin_mystery")
                st.success("Spin mystery requested!")
        
        with col3:
            if st.button("🤝 Start Trading", use_container_width=True):
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
        for message in reversed(messages[-3:]):  # Show last 3 messages
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
