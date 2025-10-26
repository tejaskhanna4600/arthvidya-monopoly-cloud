#!/usr/bin/env python3
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
        r"C:\Program Files\Git\bin\git.exe",
        r"C:\Program Files (x86)\Git\bin\git.exe",
        r"C:\Users\{}\AppData\Local\Programs\Git\bin\git.exe".format(os.getenv('USERNAME')),
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
        
        # Check if there are changes to commit
        result = subprocess.run([git_path, 'diff', '--cached', '--quiet'], capture_output=True)
        if result.returncode == 0:
            print("ℹ️ No changes to commit")
            return True
        
        # Commit changes
        commit_message = f"Auto-sync game state - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run([git_path, 'commit', '-m', commit_message], check=True)
        print("✅ Committed changes")
        
        # Push to GitHub
        try:
            subprocess.run([git_path, 'push', 'origin', 'main'], check=True)
            print("✅ Pushed to GitHub")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Push failed: {e}")
            print("💡 This might be due to authentication. Try running:")
            print("   git config --global credential.helper store")
            return False
        
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

def setup_github_remote():
    """Setup GitHub remote repository"""
    git_path = find_git()
    if not git_path:
        print("❌ Git not found")
        return False
    
    try:
        print("🔄 Setting up GitHub remote repository...")
        
        # Check if remote already exists
        result = subprocess.run([git_path, 'remote', '-v'], capture_output=True, text=True)
        if 'origin' in result.stdout:
            print("✅ GitHub remote already configured")
            return True
        
        repo_url = input("Enter your GitHub repository URL (e.g., https://github.com/tejaskhanna4600/arthvidya-monopoly-cloud.git): ").strip()
        
        if not repo_url:
            print("❌ No repository URL provided")
            return False
        
        subprocess.run([git_path, 'remote', 'add', 'origin', repo_url], check=True)
        print(f"✅ GitHub remote added: {repo_url}")
        
        # Push to GitHub
        print("🔄 Pushing to GitHub...")
        subprocess.run([git_path, 'push', '-u', 'origin', 'main'], check=True)
        print("✅ Pushed to GitHub")
        
        return True
    except Exception as e:
        print(f"❌ Error setting up GitHub remote: {e}")
        return False

def main():
    """Main function"""
    print("🔄 Simple Sync Script for Git Integration")
    print("=" * 45)
    
    while True:
        print("\nOptions:")
        print("1. Setup GitHub remote repository")
        print("2. Sync to GitHub (Push changes)")
        print("3. Pull from GitHub (Get latest changes)")
        print("4. Exit")
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            setup_github_remote()
        elif choice == "2":
            sync_to_github()
        elif choice == "3":
            pull_from_github()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-4.")
        
        print("\n" + "="*45)

if __name__ == "__main__":
    main()
