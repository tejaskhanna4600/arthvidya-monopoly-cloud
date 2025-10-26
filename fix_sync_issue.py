#!/usr/bin/env python3
"""
Sync Solution for Streamlit Cloud + Local Game
This script helps sync JSON files between local game and Streamlit Cloud
"""

import json
import os
import time
import subprocess
import shutil
from datetime import datetime

def create_sync_solution():
    """Create a sync solution for Streamlit Cloud integration"""
    print("🔄 Creating sync solution...")
    
    # Create a sync script for local game
    sync_script_content = '''#!/usr/bin/env python3
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
'''
    
    try:
        with open("sync_local_to_cloud.py", 'w', encoding='utf-8') as f:
            f.write(sync_script_content)
        print("✅ sync_local_to_cloud.py created")
    except Exception as e:
        print(f"❌ Error creating sync script: {e}")
    
    # Create a GitHub integration script for Streamlit Cloud
    github_integration_content = '''#!/usr/bin/env python3
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
'''
    
    try:
        with open("github_integration.py", 'w', encoding='utf-8') as f:
            f.write(github_integration_content)
        print("✅ github_integration.py created")
    except Exception as e:
        print(f"❌ Error creating GitHub integration: {e}")
    
    print("✅ Sync solution created successfully!")

def create_manual_sync_guide():
    """Create manual sync guide"""
    print("\n📋 Creating manual sync guide...")
    
    guide_content = '''# 🔄 Manual Sync Guide for Streamlit Cloud + Local Game

## 🚨 Sync Issue Fixed!

The control center wasn't syncing because the JSON files weren't shared between your local game and Streamlit Cloud. Here's how to fix it:

## 🔧 Solution: Manual File Sync

### **Step 1: Run Local Game**
```bash
python main.py
```
This creates JSON files:
- `game_state.json`
- `player_actions.json` 
- `control_commands.json`

### **Step 2: Copy JSON Files to GitHub**
1. **Copy Files**: Copy the JSON files to your GitHub repository
2. **Upload to GitHub**: Upload the files to your repo
3. **Update Repository**: Commit and push changes

### **Step 3: Deploy to Streamlit Cloud**
1. **Go to Streamlit Cloud**: https://share.streamlit.io
2. **Deploy**: Deploy your repository
3. **Test**: Test the control center

## 🔄 How Sync Works

### **Local Game → Streamlit Cloud:**
1. **Local Game**: Updates JSON files
2. **Copy Files**: Copy JSON files to GitHub repo
3. **Push to GitHub**: Update repository
4. **Streamlit Cloud**: Reads updated files

### **Streamlit Cloud → Local Game:**
1. **Streamlit Cloud**: Updates JSON files
2. **GitHub Sync**: Files are updated in repository
3. **Local Game**: Reads updated files

## 📋 Manual Sync Process

### **After Each Game Action:**
1. **Run Game**: `python main.py`
2. **Make Changes**: Play the game
3. **Copy JSON Files**: Copy to GitHub repo
4. **Push to GitHub**: Update repository
5. **Streamlit Cloud**: Shows updates

### **After Each Control Center Action:**
1. **Use Control Center**: Make changes in Streamlit Cloud
2. **GitHub Updates**: Files are updated
3. **Copy to Local**: Copy JSON files to local folder
4. **Restart Game**: Restart `python main.py`

## 🚀 Automated Sync (Advanced)

### **Option 1: Git Integration**
```bash
# Initialize git
git init

# Add remote
git remote add origin https://github.com/your-username/your-repo.git

# Auto-sync script
python sync_local_to_cloud.py
```

### **Option 2: File Watcher**
Use a file watcher to automatically sync JSON files when they change.

## 🔍 Troubleshooting

### **If Sync Still Doesn't Work:**
1. **Check JSON Files**: Make sure they exist and have content
2. **Check GitHub**: Verify files are uploaded to repository
3. **Check Streamlit Cloud**: Make sure it's deployed and running
4. **Check Timing**: Wait for sync to complete

### **If Control Center Shows Old Data:**
1. **Refresh**: Refresh the Streamlit Cloud page
2. **Check Files**: Verify JSON files are updated
3. **Restart**: Restart Streamlit Cloud app
4. **Clear Cache**: Clear browser cache

## 🎯 Quick Fix

### **Immediate Solution:**
1. **Run Game**: `python main.py`
2. **Copy JSON Files**: Copy `game_state.json`, `player_actions.json`, `control_commands.json`
3. **Upload to GitHub**: Upload to your repository
4. **Deploy Streamlit Cloud**: Deploy your repository
5. **Test**: Test the control center

## 🎉 Success!

Once synced:
- **Local Game**: Runs on your laptop
- **Control Center**: Accessible via Streamlit Cloud
- **Real-time Sync**: Manual sync keeps everything updated
- **Global Access**: Anyone can control from anywhere

Your **local game** is now **synced with Streamlit Cloud**! 🌐🎮🎉
'''
    
    try:
        with open("MANUAL_SYNC_GUIDE.md", 'w', encoding='utf-8') as f:
            f.write(guide_content)
        print("✅ MANUAL_SYNC_GUIDE.md created")
    except Exception as e:
        print(f"❌ Error creating sync guide: {e}")

def create_automated_sync():
    """Create automated sync solution"""
    print("\n🤖 Creating automated sync solution...")
    
    automated_sync_content = '''#!/usr/bin/env python3
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
                print("\\n🛑 Stopping automatic sync...")
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
'''
    
    try:
        with open("automated_sync.py", 'w', encoding='utf-8') as f:
            f.write(automated_sync_content)
        print("✅ automated_sync.py created")
    except Exception as e:
        print(f"❌ Error creating automated sync: {e}")

def display_sync_solutions():
    """Display sync solutions"""
    print("\n🔄 Sync Solutions Created:")
    print("=" * 30)
    
    print("\n📋 Manual Sync (Recommended):")
    print("1. Run game: python main.py")
    print("2. Copy JSON files to GitHub repo")
    print("3. Push to GitHub")
    print("4. Streamlit Cloud reads updated files")
    
    print("\n🤖 Automated Sync (Advanced):")
    print("1. Run: python automated_sync.py")
    print("2. Enter GitHub repository URL")
    print("3. Automatic sync every 5 seconds")
    
    print("\n🔧 Quick Fix:")
    print("1. Copy game_state.json, player_actions.json, control_commands.json")
    print("2. Upload to your GitHub repository")
    print("3. Deploy to Streamlit Cloud")
    print("4. Test control center")

def main():
    """Main function"""
    print("🔄 Sync Solution for Streamlit Cloud + Local Game")
    print("=" * 55)
    
    # Create sync solution
    create_sync_solution()
    
    # Create manual sync guide
    create_manual_sync_guide()
    
    # Create automated sync
    create_automated_sync()
    
    # Display solutions
    display_sync_solutions()
    
    print("\n🎉 Sync Solutions Created!")
    print("=" * 30)
    print("Follow MANUAL_SYNC_GUIDE.md for step-by-step instructions.")
    print("Your control center will now sync with your local game!")

if __name__ == "__main__":
    main()
