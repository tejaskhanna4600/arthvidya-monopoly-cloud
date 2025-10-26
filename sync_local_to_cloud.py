#!/usr/bin/env python3
"""
Local Game Sync Script
This script syncs JSON files with GitHub for Streamlit Cloud integration
"""

import json
import os
import time
import subprocess
import shutil
from datetime import datetime

def sync_to_github():
    """Sync JSON files to GitHub"""
    try:
        # Check if git is initialized
        if not os.path.exists('.git'):
            print("Initializing git repository...")
            subprocess.run(['git', 'init'], check=True)
        
        # Add JSON files to git
        json_files = ['game_state.json', 'player_actions.json', 'control_commands.json']
        
        for file in json_files:
            if os.path.exists(file):
                subprocess.run(['git', 'add', file], check=True)
                print(f"Added {file} to git")
        
        # Commit changes
        subprocess.run(['git', 'commit', '-m', f'Sync game state - {datetime.now()}'], check=True)
        print("Committed changes to git")
        
        # Push to GitHub (if remote exists)
        try:
            subprocess.run(['git', 'push', 'origin', 'main'], check=True)
            print("Pushed changes to GitHub")
        except:
            print("No remote repository configured. Please set up GitHub remote.")
        
        return True
    except Exception as e:
        print(f"Error syncing to GitHub: {e}")
        return False

def sync_from_github():
    """Sync JSON files from GitHub"""
    try:
        # Pull latest changes
        subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
        print("Pulled latest changes from GitHub")
        return True
    except Exception as e:
        print(f"Error syncing from GitHub: {e}")
        return False

def setup_github_remote(repo_url):
    """Setup GitHub remote repository"""
    try:
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        print(f"Added GitHub remote: {repo_url}")
        return True
    except Exception as e:
        print(f"Error setting up GitHub remote: {e}")
        return False

if __name__ == "__main__":
    print("🔄 Local Game Sync Script")
    print("=" * 30)
    
    # Check if JSON files exist
    json_files = ['game_state.json', 'player_actions.json', 'control_commands.json']
    missing_files = [f for f in json_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"Missing files: {missing_files}")
        print("Please run the game first to create these files.")
        exit(1)
    
    # Sync to GitHub
    if sync_to_github():
        print("✅ Sync to GitHub successful!")
    else:
        print("❌ Sync to GitHub failed!")
    
    print("🔄 Sync complete!")
