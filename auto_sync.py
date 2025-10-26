#!/usr/bin/env python3
"""
Automatic Sync Script for Git Integration
This script automatically syncs JSON files with GitHub
"""

import subprocess
import json
import os
import time
from datetime import datetime

def sync_json_files():
    """Sync JSON files to GitHub"""
    try:
        json_files = ['game_state.json', 'player_actions.json', 'control_commands.json']
        
        # Check if files exist
        existing_files = [f for f in json_files if os.path.exists(f)]
        if not existing_files:
            print("❌ No JSON files found")
            return False
        
        print(f"🔄 Syncing {len(existing_files)} files to GitHub...")
        
        # Add JSON files to git
        for file in existing_files:
            subprocess.run(['git', 'add', file], check=True)
            print(f"✅ Added {file}")
        
        # Commit changes
        commit_message = f"Auto-sync game state - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print("✅ Committed changes")
        
        # Push to GitHub
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print("✅ Pushed to GitHub")
        
        print(f"🎉 Successfully synced {len(existing_files)} files to GitHub!")
        return True
    except Exception as e:
        print(f"❌ Error syncing to GitHub: {e}")
        return False

def pull_from_github():
    """Pull latest changes from GitHub"""
    try:
        print("🔄 Pulling latest changes from GitHub...")
        subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
        print("✅ Pulled latest changes from GitHub")
        return True
    except Exception as e:
        print(f"❌ Error pulling from GitHub: {e}")
        return False

def check_git_status():
    """Check Git status"""
    try:
        print("🔄 Checking Git status...")
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if result.stdout.strip():
            print("📋 Files to be committed:")
            print(result.stdout)
        else:
            print("ℹ️ No changes to commit")
        return True
    except Exception as e:
        print(f"❌ Error checking Git status: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Automatic Sync Script for Git Integration")
    print("=" * 50)
    
    while True:
        print("\\nOptions:")
        print("1. Sync to GitHub (Push changes)")
        print("2. Pull from GitHub (Get latest changes)")
        print("3. Check Git status")
        print("4. Exit")
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            sync_json_files()
        elif choice == "2":
            pull_from_github()
        elif choice == "3":
            check_git_status()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-4.")
        
        print("\\n" + "="*50)

if __name__ == "__main__":
    main()
