#!/usr/bin/env python3
"""
Git Integration Setup for Streamlit Cloud + Local Game
This script helps you set up Git integration for automatic syncing
"""

import os
import subprocess
import json
from pathlib import Path

def check_git_installation():
    """Check if Git is installed"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Git is installed: {result.stdout.strip()}")
            return True
        else:
            print("❌ Git is not installed")
            return False
    except FileNotFoundError:
        print("❌ Git is not installed")
        return False

def initialize_git_repository():
    """Initialize Git repository"""
    try:
        if os.path.exists('.git'):
            print("✅ Git repository already initialized")
            return True
        
        print("🔄 Initializing Git repository...")
        subprocess.run(['git', 'init'], check=True)
        print("✅ Git repository initialized")
        return True
    except Exception as e:
        print(f"❌ Error initializing Git repository: {e}")
        return False

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = '''# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
*.log

# Game files (keep JSON files for sync)
# *.json
# !game_state.json
# !player_actions.json
# !control_commands.json

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp
'''
    
    try:
        with open('.gitignore', 'w', encoding='utf-8') as f:
            f.write(gitignore_content)
        print("✅ .gitignore created")
        return True
    except Exception as e:
        print(f"❌ Error creating .gitignore: {e}")
        return False

def setup_git_config():
    """Setup Git configuration"""
    try:
        # Check if user is configured
        result = subprocess.run(['git', 'config', 'user.name'], capture_output=True, text=True)
        if result.returncode != 0 or not result.stdout.strip():
            print("🔄 Setting up Git user configuration...")
            name = input("Enter your Git username: ").strip()
            email = input("Enter your Git email: ").strip()
            
            if name and email:
                subprocess.run(['git', 'config', 'user.name', name], check=True)
                subprocess.run(['git', 'config', 'user.email', email], check=True)
                print("✅ Git user configuration set")
            else:
                print("❌ Git user configuration not set")
                return False
        else:
            print("✅ Git user configuration already set")
        
        return True
    except Exception as e:
        print(f"❌ Error setting up Git configuration: {e}")
        return False

def add_files_to_git():
    """Add files to Git"""
    try:
        print("🔄 Adding files to Git...")
        
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Check what files are staged
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if result.stdout.strip():
            print("✅ Files added to Git")
            print("Files to be committed:")
            print(result.stdout)
            return True
        else:
            print("ℹ️ No new files to add")
            return True
    except Exception as e:
        print(f"❌ Error adding files to Git: {e}")
        return False

def create_initial_commit():
    """Create initial commit"""
    try:
        print("🔄 Creating initial commit...")
        subprocess.run(['git', 'commit', '-m', 'Initial commit: Monopoly game with Streamlit integration'], check=True)
        print("✅ Initial commit created")
        return True
    except Exception as e:
        print(f"❌ Error creating initial commit: {e}")
        return False

def setup_github_remote():
    """Setup GitHub remote repository"""
    try:
        print("🔄 Setting up GitHub remote repository...")
        
        # Check if remote already exists
        result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
        if 'origin' in result.stdout:
            print("✅ GitHub remote already configured")
            return True
        
        # Get repository URL
        repo_url = input("Enter your GitHub repository URL (e.g., https://github.com/username/repo.git): ").strip()
        
        if not repo_url:
            print("❌ No repository URL provided")
            return False
        
        # Add remote
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        print(f"✅ GitHub remote added: {repo_url}")
        
        return True
    except Exception as e:
        print(f"❌ Error setting up GitHub remote: {e}")
        return False

def push_to_github():
    """Push to GitHub"""
    try:
        print("🔄 Pushing to GitHub...")
        
        # Push to main branch
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
        print("✅ Pushed to GitHub")
        return True
    except Exception as e:
        print(f"❌ Error pushing to GitHub: {e}")
        print("💡 Make sure your GitHub repository exists and you have push access")
        return False

def create_auto_sync_script():
    """Create automatic sync script"""
    auto_sync_content = '''#!/usr/bin/env python3
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
        
        # Add JSON files to git
        for file in existing_files:
            subprocess.run(['git', 'add', file], check=True)
        
        # Commit changes
        commit_message = f"Auto-sync game state - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
        # Push to GitHub
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        
        print(f"✅ Synced {len(existing_files)} files to GitHub")
        return True
    except Exception as e:
        print(f"❌ Error syncing to GitHub: {e}")
        return False

def pull_from_github():
    """Pull latest changes from GitHub"""
    try:
        subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
        print("✅ Pulled latest changes from GitHub")
        return True
    except Exception as e:
        print(f"❌ Error pulling from GitHub: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Automatic Sync Script")
    print("=" * 25)
    
    while True:
        print("\\nOptions:")
        print("1. Sync to GitHub")
        print("2. Pull from GitHub")
        print("3. Exit")
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == "1":
            sync_json_files()
        elif choice == "2":
            pull_from_github()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
'''
    
    try:
        with open('auto_sync.py', 'w', encoding='utf-8') as f:
            f.write(auto_sync_content)
        print("✅ auto_sync.py created")
        return True
    except Exception as e:
        print(f"❌ Error creating auto sync script: {e}")
        return False

def create_git_workflow_guide():
    """Create Git workflow guide"""
    guide_content = '''# 🔄 Git Integration Workflow Guide

## 🚀 Complete Git Integration Setup

This guide helps you set up Git integration for automatic syncing between your local game and Streamlit Cloud.

## 📋 Prerequisites

### **Required Software:**
- **Git**: Download from https://git-scm.com/
- **GitHub Account**: Create at https://github.com
- **Python**: Already installed

## 🔧 Step-by-Step Setup

### **Step 1: Install Git**
1. **Download Git**: Go to https://git-scm.com/
2. **Install Git**: Follow installation instructions
3. **Verify Installation**: Run `git --version`

### **Step 2: Create GitHub Repository**
1. **Go to GitHub**: https://github.com
2. **Create Repository**: Click "New Repository"
3. **Name**: `arthvidya-monopoly-cloud`
4. **Make Public**: Choose "Public"
5. **Create**: Click "Create repository"

### **Step 3: Run Git Integration Script**
```bash
python setup_git_integration.py
```

This will:
- Initialize Git repository
- Create .gitignore
- Setup Git configuration
- Add files to Git
- Create initial commit
- Setup GitHub remote
- Push to GitHub

### **Step 4: Deploy to Streamlit Cloud**
1. **Go to Streamlit Cloud**: https://share.streamlit.io
2. **Sign in**: Use GitHub account
3. **New App**: Click "New app"
4. **Repository**: Select your repository
5. **Branch**: `main`
6. **Main File**: `streamlit_app.py`
7. **Deploy**: Click "Deploy"

## 🔄 Git Workflow

### **Daily Workflow:**

#### **When Playing the Game:**
1. **Run Game**: `python main.py`
2. **Play Game**: Make moves, buy properties, etc.
3. **Auto-Sync**: `python auto_sync.py` (option 1)
4. **Streamlit Cloud**: Shows updated state

#### **When Using Control Center:**
1. **Use Control Center**: Make changes in Streamlit Cloud
2. **Pull Changes**: `python auto_sync.py` (option 2)
3. **Restart Game**: `python main.py`
4. **Local Game**: Shows updated state

### **Manual Git Commands:**

#### **Sync to GitHub:**
```bash
git add game_state.json player_actions.json control_commands.json
git commit -m "Update game state"
git push origin main
```

#### **Pull from GitHub:**
```bash
git pull origin main
```

#### **Check Status:**
```bash
git status
```

#### **View History:**
```bash
git log --oneline
```

## 🤖 Automated Sync

### **Option 1: Manual Sync Script**
```bash
python auto_sync.py
```
- Choose option 1 to sync to GitHub
- Choose option 2 to pull from GitHub

### **Option 2: Git Hooks (Advanced)**
Create Git hooks to automatically sync when files change.

### **Option 3: File Watcher (Advanced)**
Use a file watcher to automatically sync when JSON files change.

## 🔍 Troubleshooting

### **Git Not Installed:**
1. **Download Git**: https://git-scm.com/
2. **Install Git**: Follow installation instructions
3. **Restart Terminal**: Close and reopen terminal
4. **Verify**: Run `git --version`

### **GitHub Authentication:**
1. **Generate Token**: GitHub → Settings → Developer settings → Personal access tokens
2. **Use Token**: Use token instead of password
3. **SSH Keys**: Alternative authentication method

### **Push Rejected:**
1. **Pull First**: `git pull origin main`
2. **Resolve Conflicts**: Fix any merge conflicts
3. **Push Again**: `git push origin main`

### **Files Not Syncing:**
1. **Check .gitignore**: Make sure JSON files aren't ignored
2. **Check Git Status**: `git status`
3. **Add Files**: `git add filename.json`
4. **Commit**: `git commit -m "message"`
5. **Push**: `git push origin main`

## 🎯 Quick Commands

### **Essential Git Commands:**
```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push origin main

# Pull from GitHub
git pull origin main

# View history
git log --oneline
```

### **Sync Commands:**
```bash
# Sync to GitHub
python auto_sync.py

# Manual sync
git add game_state.json player_actions.json control_commands.json
git commit -m "Sync game state"
git push origin main
```

## 🎉 Success!

Once Git integration is set up:
- **Automatic Sync**: JSON files sync automatically
- **Real-time Updates**: Changes appear in Streamlit Cloud
- **Version Control**: Track all game changes
- **Backup**: All data is backed up to GitHub
- **Collaboration**: Multiple people can access

Your **local game** is now **fully integrated with Streamlit Cloud**! 🌐🎮🎉

## 📞 Support

### **Git Issues:**
- **Git Documentation**: https://git-scm.com/doc
- **GitHub Help**: https://help.github.com
- **Stack Overflow**: Search for Git questions

### **Streamlit Cloud Issues:**
- **Streamlit Docs**: https://docs.streamlit.io
- **Community**: https://discuss.streamlit.io

Your **Git integration** is now **complete**! 🎉
'''
    
    try:
        with open('GIT_WORKFLOW_GUIDE.md', 'w', encoding='utf-8') as f:
            f.write(guide_content)
        print("✅ GIT_WORKFLOW_GUIDE.md created")
        return True
    except Exception as e:
        print(f"❌ Error creating Git workflow guide: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Git Integration Setup for Streamlit Cloud + Local Game")
    print("=" * 65)
    
    # Check Git installation
    if not check_git_installation():
        print("\\n❌ Git is not installed. Please install Git first:")
        print("1. Go to https://git-scm.com/")
        print("2. Download and install Git")
        print("3. Restart terminal")
        print("4. Run this script again")
        return
    
    # Initialize Git repository
    if not initialize_git_repository():
        return
    
    # Create .gitignore
    if not create_gitignore():
        return
    
    # Setup Git configuration
    if not setup_git_config():
        return
    
    # Add files to Git
    if not add_files_to_git():
        return
    
    # Create initial commit
    if not create_initial_commit():
        return
    
    # Setup GitHub remote
    if not setup_github_remote():
        return
    
    # Push to GitHub
    if not push_to_github():
        return
    
    # Create auto sync script
    create_auto_sync_script()
    
    # Create Git workflow guide
    create_git_workflow_guide()
    
    print("\\n🎉 Git Integration Setup Complete!")
    print("=" * 40)
    print("Your local game is now integrated with GitHub!")
    print("Follow GIT_WORKFLOW_GUIDE.md for daily workflow.")
    print("Use python auto_sync.py for automatic syncing.")

if __name__ == "__main__":
    main()
