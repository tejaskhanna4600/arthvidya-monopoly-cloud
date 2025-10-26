#!/usr/bin/env python3
"""
Automated Sync for Streamlit Cloud + Local Game
This script automatically syncs JSON files between local game and Streamlit Cloud
"""

import json
import os
import time
import subprocess
import shutil
from datetime import datetime
import threading

class GameSync:
    def __init__(self):
        self.json_files = ['game_state.json', 'player_actions.json', 'control_commands.json']
        self.sync_interval = 5  # seconds
        self.running = False
        
    def check_git_status(self):
        """Check if git is initialized"""
        if not os.path.exists('.git'):
            print("Initializing git repository...")
            subprocess.run(['git', 'init'], check=True)
            return False
        return True
    
    def setup_github_remote(self, repo_url):
        """Setup GitHub remote repository"""
        try:
            subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
            print(f"Added GitHub remote: {repo_url}")
            return True
        except:
            try:
                subprocess.run(['git', 'remote', 'set-url', 'origin', repo_url], check=True)
                print(f"Updated GitHub remote: {repo_url}")
                return True
            except Exception as e:
                print(f"Error setting up GitHub remote: {e}")
                return False
    
    def sync_to_github(self):
        """Sync JSON files to GitHub"""
        try:
            if not self.check_git_status():
                return False
            
            # Add JSON files to git
            for file in self.json_files:
                if os.path.exists(file):
                    subprocess.run(['git', 'add', file], check=True)
            
            # Commit changes
            subprocess.run(['git', 'commit', '-m', f'Auto-sync - {datetime.now()}'], check=True)
            
            # Push to GitHub
            subprocess.run(['git', 'push', 'origin', 'main'], check=True)
            
            print(f"✅ Synced to GitHub at {datetime.now()}")
            return True
        except Exception as e:
            print(f"❌ Error syncing to GitHub: {e}")
            return False
    
    def sync_from_github(self):
        """Sync JSON files from GitHub"""
        try:
            if not self.check_git_status():
                return False
            
            # Pull latest changes
            subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
            
            print(f"✅ Synced from GitHub at {datetime.now()}")
            return True
        except Exception as e:
            print(f"❌ Error syncing from GitHub: {e}")
            return False
    
    def start_auto_sync(self):
        """Start automatic sync"""
        self.running = True
        print("🔄 Starting automatic sync...")
        
        while self.running:
            try:
                # Sync to GitHub
                self.sync_to_github()
                
                # Wait for next sync
                time.sleep(self.sync_interval)
            except KeyboardInterrupt:
                print("\n🛑 Stopping automatic sync...")
                self.running = False
                break
    
    def stop_auto_sync(self):
        """Stop automatic sync"""
        self.running = False
        print("🛑 Automatic sync stopped")

def main():
    """Main function"""
    print("🔄 Automated Sync for Streamlit Cloud + Local Game")
    print("=" * 55)
    
    sync = GameSync()
    
    # Check if JSON files exist
    missing_files = [f for f in sync.json_files if not os.path.exists(f)]
    if missing_files:
        print(f"Missing files: {missing_files}")
        print("Please run the game first to create these files.")
        return
    
    # Setup GitHub remote
    repo_url = input("Enter your GitHub repository URL: ").strip()
    if not repo_url:
        print("No repository URL provided. Using manual sync.")
        return
    
    if not sync.setup_github_remote(repo_url):
        print("Failed to setup GitHub remote. Using manual sync.")
        return
    
    # Start automatic sync
    try:
        sync.start_auto_sync()
    except KeyboardInterrupt:
        sync.stop_auto_sync()
    
    print("🔄 Automated sync complete!")

if __name__ == "__main__":
    main()
