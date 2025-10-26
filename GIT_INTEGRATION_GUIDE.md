# 🔄 Git Integration Guide for Streamlit Cloud + Local Game

## 🚨 Git Not Installed - Here's How to Set It Up!

Git is not installed on your system. Here's a complete guide to set up Git integration for automatic syncing between your local game and Streamlit Cloud.

## 📋 Step 1: Install Git

### **Download Git:**
1. **Go to**: https://git-scm.com/
2. **Download**: Click "Download for Windows"
3. **Install**: Run the installer
4. **Restart**: Restart your terminal/command prompt

### **Verify Installation:**
```bash
git --version
```
Should show: `git version 2.x.x`

## 📋 Step 2: Create GitHub Repository

### **Create Repository:**
1. **Go to GitHub**: https://github.com
2. **Sign In**: Login to your account
3. **New Repository**: Click "New Repository"
4. **Name**: `arthvidya-monopoly-cloud`
5. **Make Public**: Choose "Public"
6. **Create**: Click "Create repository"

### **Get Repository URL:**
Copy the repository URL (e.g., `https://github.com/your-username/arthvidya-monopoly-cloud.git`)

## 📋 Step 3: Manual Git Setup

### **Initialize Git Repository:**
```bash
git init
```

### **Create .gitignore:**
```bash
# Create .gitignore file
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore
echo "*.pyo" >> .gitignore
echo "*.pyd" >> .gitignore
echo ".Python" >> .gitignore
echo "env/" >> .gitignore
echo "venv/" >> .gitignore
echo ".venv/" >> .gitignore
echo "*.log" >> .gitignore
echo ".DS_Store" >> .gitignore
echo "Thumbs.db" >> .gitignore
```

### **Configure Git:**
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### **Add Files:**
```bash
git add .
```

### **Create Initial Commit:**
```bash
git commit -m "Initial commit: Monopoly game with Streamlit integration"
```

### **Add GitHub Remote:**
```bash
git remote add origin https://github.com/your-username/arthvidya-monopoly-cloud.git
```

### **Push to GitHub:**
```bash
git push -u origin main
```

## 🔄 Step 4: Daily Git Workflow

### **When Playing the Game:**

#### **Sync to GitHub (After Game Changes):**
```bash
# Add JSON files
git add game_state.json player_actions.json control_commands.json

# Commit changes
git commit -m "Update game state"

# Push to GitHub
git push origin main
```

#### **Pull from GitHub (After Control Center Changes):**
```bash
# Pull latest changes
git pull origin main
```

### **Quick Sync Commands:**

#### **Sync to GitHub:**
```bash
git add game_state.json player_actions.json control_commands.json
git commit -m "Sync game state - $(date)"
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

## 🤖 Step 5: Automated Sync Script

### **Create Auto Sync Script:**
Create a file called `auto_sync.py`:

```python
#!/usr/bin/env python3
"""
Automatic Sync Script for Git Integration
"""

import subprocess
import json
import os
from datetime import datetime

def sync_to_github():
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
            sync_to_github()
        elif choice == "2":
            pull_from_github()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
```

### **Use Auto Sync Script:**
```bash
python auto_sync.py
```

## 🔧 Step 6: Deploy to Streamlit Cloud

### **Deploy Process:**
1. **Go to Streamlit Cloud**: https://share.streamlit.io
2. **Sign In**: Use GitHub account
3. **New App**: Click "New app"
4. **Repository**: Select `arthvidya-monopoly-cloud`
5. **Branch**: `main`
6. **Main File**: `streamlit_app.py`
7. **Deploy**: Click "Deploy"

### **Get Public URL:**
After deployment: `https://your-app-name.streamlit.app`

## 🔄 Complete Workflow

### **Daily Workflow:**

#### **1. Play Local Game:**
```bash
python main.py
```

#### **2. Sync Changes to GitHub:**
```bash
python auto_sync.py
# Choose option 1
```

#### **3. Use Control Center:**
- Go to Streamlit Cloud URL
- Make changes in control center
- Changes are saved to GitHub

#### **4. Pull Changes to Local:**
```bash
python auto_sync.py
# Choose option 2
```

#### **5. Restart Local Game:**
```bash
python main.py
```

## 🔍 Troubleshooting

### **Git Not Found:**
1. **Install Git**: https://git-scm.com/
2. **Restart Terminal**: Close and reopen
3. **Check PATH**: Make sure Git is in system PATH

### **Authentication Failed:**
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

## 🎯 Quick Reference

### **Essential Commands:**
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
# Manual sync to GitHub
git add game_state.json player_actions.json control_commands.json
git commit -m "Sync game state"
git push origin main

# Manual pull from GitHub
git pull origin main

# Auto sync script
python auto_sync.py
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

Your **Git integration** setup is now **complete**! 🎉
