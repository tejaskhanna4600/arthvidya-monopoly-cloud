import streamlit as st
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
