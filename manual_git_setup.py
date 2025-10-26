#!/usr/bin/env python3
"""
Manual Git Setup for Streamlit Cloud + Local Game
This script helps you set up Git integration manually
"""

import os
import subprocess
import json
from pathlib import Path

def check_git_installation():
    """Check if Git is installed"""
    try:
        # Try different ways to find Git
        git_paths = [
            r"C:\Program Files\Git\bin\git.exe",
            r"C:\Program Files (x86)\Git\bin\git.exe",
            r"C:\Users\{}\AppData\Local\Programs\Git\bin\git.exe".format(os.getenv('USERNAME')),
            "git"  # Try if it's in PATH
        ]
        
        for git_path in git_paths:
            try:
                result = subprocess.run([git_path, '--version'], capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"✅ Git found at: {git_path}")
                    print(f"Version: {result.stdout.strip()}")
                    return git_path
            except:
                continue
        
        print("❌ Git not found in common locations")
        return None
    except Exception as e:
        print(f"❌ Error checking Git installation: {e}")
        return None

def manual_git_setup():
    """Manual Git setup process"""
    print("🔄 Manual Git Setup Process")
    print("=" * 35)
    
    # Check if Git is installed
    git_path = check_git_installation()
    if not git_path:
        print("\n❌ Git is not properly installed or not in PATH")
        print("\n📋 Please do the following:")
        print("1. Download Git from: https://git-scm.com/")
        print("2. Install Git with default settings")
        print("3. During installation, make sure to check 'Add Git to PATH'")
        print("4. Restart your terminal/command prompt")
        print("5. Run this script again")
        return False
    
    # Check if we're in a Git repository
    if os.path.exists('.git'):
        print("✅ Git repository already initialized")
    else:
        print("🔄 Initializing Git repository...")
        try:
            subprocess.run([git_path, 'init'], check=True)
            print("✅ Git repository initialized")
        except Exception as e:
            print(f"❌ Error initializing Git: {e}")
            return False
    
    # Create .gitignore
    if not os.path.exists('.gitignore'):
        print("🔄 Creating .gitignore...")
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
        except Exception as e:
            print(f"❌ Error creating .gitignore: {e}")
    
    # Check Git configuration
    try:
        result = subprocess.run([git_path, 'config', 'user.name'], capture_output=True, text=True)
        if result.returncode != 0 or not result.stdout.strip():
            print("🔄 Setting up Git user configuration...")
            name = input("Enter your Git username: ").strip()
            email = input("Enter your Git email: ").strip()
            
            if name and email:
                subprocess.run([git_path, 'config', 'user.name', name], check=True)
                subprocess.run([git_path, 'config', 'user.email', email], check=True)
                print("✅ Git user configuration set")
            else:
                print("❌ Git user configuration not set")
                return False
        else:
            print("✅ Git user configuration already set")
    except Exception as e:
        print(f"❌ Error setting up Git configuration: {e}")
        return False
    
    # Add files to Git
    try:
        print("🔄 Adding files to Git...")
        subprocess.run([git_path, 'add', '.'], check=True)
        print("✅ Files added to Git")
    except Exception as e:
        print(f"❌ Error adding files to Git: {e}")
        return False
    
    # Create initial commit
    try:
        print("🔄 Creating initial commit...")
        subprocess.run([git_path, 'commit', '-m', 'Initial commit: Monopoly game with Streamlit integration'], check=True)
        print("✅ Initial commit created")
    except Exception as e:
        print(f"❌ Error creating initial commit: {e}")
        return False
    
    # Setup GitHub remote
    try:
        print("🔄 Setting up GitHub remote repository...")
        
        # Check if remote already exists
        result = subprocess.run([git_path, 'remote', '-v'], capture_output=True, text=True)
        if 'origin' in result.stdout:
            print("✅ GitHub remote already configured")
        else:
            repo_url = input("Enter your GitHub repository URL (e.g., https://github.com/username/repo.git): ").strip()
            
            if not repo_url:
                print("❌ No repository URL provided")
                return False
            
            subprocess.run([git_path, 'remote', 'add', 'origin', repo_url], check=True)
            print(f"✅ GitHub remote added: {repo_url}")
        
        return True
    except Exception as e:
        print(f"❌ Error setting up GitHub remote: {e}")
        return False

def create_simple_sync_script():
    """Create a simple sync script"""
    sync_script_content = '''#!/usr/bin/env python3
"""
Simple Sync Script for Git Integration
"""

import subprocess
import os
import json
from datetime import datetime

def find_git():
    """Find Git executable"""
    git_paths = [
        r"C:\\Program Files\\Git\\bin\\git.exe",
        r"C:\\Program Files (x86)\\Git\\bin\\git.exe",
        r"C:\\Users\\{}\\AppData\\Local\\Programs\\Git\\bin\\git.exe".format(os.getenv('USERNAME')),
        "git"
    ]
    
    for git_path in git_paths:
        try:
            result = subprocess.run([git_path, '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                return git_path
        except:
            continue
    return None

def sync_to_github():
    """Sync JSON files to GitHub"""
    git_path = find_git()
    if not git_path:
        print("❌ Git not found")
        return False
    
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
            subprocess.run([git_path, 'add', file], check=True)
            print(f"✅ Added {file}")
        
        # Commit changes
        commit_message = f"Auto-sync game state - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run([git_path, 'commit', '-m', commit_message], check=True)
        print("✅ Committed changes")
        
        # Push to GitHub
        subprocess.run([git_path, 'push', 'origin', 'main'], check=True)
        print("✅ Pushed to GitHub")
        
        print(f"🎉 Successfully synced {len(existing_files)} files to GitHub!")
        return True
    except Exception as e:
        print(f"❌ Error syncing to GitHub: {e}")
        return False

def pull_from_github():
    """Pull latest changes from GitHub"""
    git_path = find_git()
    if not git_path:
        print("❌ Git not found")
        return False
    
    try:
        print("🔄 Pulling latest changes from GitHub...")
        subprocess.run([git_path, 'pull', 'origin', 'main'], check=True)
        print("✅ Pulled latest changes from GitHub")
        return True
    except Exception as e:
        print(f"❌ Error pulling from GitHub: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Simple Sync Script for Git Integration")
    print("=" * 45)
    
    while True:
        print("\\nOptions:")
        print("1. Sync to GitHub (Push changes)")
        print("2. Pull from GitHub (Get latest changes)")
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
            print("❌ Invalid option. Please choose 1-3.")
        
        print("\\n" + "="*45)

if __name__ == "__main__":
    main()
'''
    
    try:
        with open('simple_sync.py', 'w', encoding='utf-8') as f:
            f.write(sync_script_content)
        print("✅ simple_sync.py created")
        return True
    except Exception as e:
        print(f"❌ Error creating sync script: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Manual Git Setup for Streamlit Cloud + Local Game")
    print("=" * 60)
    
    # Run manual Git setup
    if manual_git_setup():
        print("\\n✅ Git setup completed successfully!")
        
        # Create simple sync script
        create_simple_sync_script()
        
        print("\\n🎉 Git Integration Setup Complete!")
        print("=" * 40)
        print("Your local game is now integrated with Git!")
        print("\\n📋 Next Steps:")
        print("1. Create a GitHub repository")
        print("2. Get the repository URL")
        print("3. Run: python simple_sync.py")
        print("4. Deploy to Streamlit Cloud")
        
        print("\\n🔧 Manual Commands:")
        print("• Sync to GitHub: python simple_sync.py (option 1)")
        print("• Pull from GitHub: python simple_sync.py (option 2)")
    else:
        print("\\n❌ Git setup failed!")
        print("Please install Git properly and try again.")

if __name__ == "__main__":
    main()
