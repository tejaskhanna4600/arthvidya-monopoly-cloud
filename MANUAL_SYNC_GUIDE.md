# 🔄 Manual Sync Guide for Streamlit Cloud + Local Game

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
