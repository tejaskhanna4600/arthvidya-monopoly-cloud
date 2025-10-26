#!/usr/bin/env python3
"""
GitHub Integration for Streamlit Cloud
This script helps Streamlit Cloud read/write JSON files via GitHub
"""

import json
import os
import time
import subprocess
from datetime import datetime

def read_from_github(filename):
    """Read JSON file from GitHub"""
    try:
        # For Streamlit Cloud, we'll use local files that are synced
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return None
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

def write_to_github(data, filename):
    """Write JSON file to GitHub"""
    try:
        # Write to local file (will be synced to GitHub)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        # Commit and push to GitHub
        subprocess.run(['git', 'add', filename], check=True)
        subprocess.run(['git', 'commit', '-m', f'Update {filename} - {datetime.now()}'], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        
        return True
    except Exception as e:
        print(f"Error writing {filename}: {e}")
        return False

def sync_game_state():
    """Sync game state between local and cloud"""
    try:
        # Read current game state
        game_state = read_from_github('game_state.json')
        if game_state:
            print(f"Current game state: Player {game_state.get('current_player', 0) + 1}")
            return game_state
        return None
    except Exception as e:
        print(f"Error syncing game state: {e}")
        return None

if __name__ == "__main__":
    print("🔄 GitHub Integration for Streamlit Cloud")
    print("=" * 45)
    
    # Test reading game state
    game_state = sync_game_state()
    if game_state:
        print("✅ Game state sync successful!")
    else:
        print("❌ Game state sync failed!")
    
    print("🔄 GitHub integration complete!")
