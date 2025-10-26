# 🌐 Excitel WiFi Router Configuration Guide

## 🔧 How to Configure Your Excitel Router for Port Forwarding

This guide is specifically designed for **Excitel WiFi routers** to help you set up port forwarding for your Monopoly game.

## 📋 Excitel Router Information

### **Common Excitel Router Details:**
- **Default IP**: `192.168.1.1` or `192.168.0.1`
- **Default Username**: `admin`
- **Default Password**: `admin` or `password`
- **Brand**: Usually TP-Link, D-Link, or similar
- **Model**: Varies by location

### **Before You Start:**
- [ ] Make sure you're connected to Excitel WiFi
- [ ] Note your laptop's IP address
- [ ] Have router admin credentials ready
- [ ] Know which port your Streamlit app uses (usually 8501)

## 🔍 Step 1: Find Your Network Information

### **Run Network Info Script:**
```bash
python network_info.py
```

This will show you:
- Your laptop's IP address
- Your public IP address
- Your router's IP address
- Port forwarding configuration

### **Manual Check:**
1. **Open Command Prompt**: Press `Win + R`, type `cmd`, press Enter
2. **Run Command**: Type `ipconfig` and press Enter
3. **Find IP**: Look for "IPv4 Address" under your WiFi adapter
4. **Find Gateway**: Look for "Default Gateway" (this is your router IP)

## 🌐 Step 2: Access Excitel Router Admin Panel

### **Common Excitel Router IPs:**
- `192.168.1.1` (Most common)
- `192.168.0.1`
- `192.168.2.1`
- `10.0.0.1`

### **Access Steps:**
1. **Open Browser**: Use Chrome, Firefox, Safari, etc.
2. **Enter IP**: Type your router's IP address
3. **Login**: Enter admin credentials
4. **Default Credentials**:
   - **Username**: `admin`
   - **Password**: `admin` or `password`

### **If Default Credentials Don't Work:**
- Check router label for credentials
- Contact Excitel support
- Try common passwords: `12345`, `admin123`, `password123`

## 🔧 Step 3: Configure Port Forwarding on Excitel Router

### **Step 3.1: Find Port Forwarding Section**
1. **Login**: Access your Excitel router admin panel
2. **Navigate**: Look for one of these sections:
   - **Advanced** → **Port Forwarding**
   - **Network** → **Port Forwarding**
   - **Firewall** → **Port Forwarding**
   - **Security** → **Port Forwarding**
   - **NAT** → **Port Forwarding**

### **Step 3.2: Create Port Forwarding Rule**
1. **Add New Rule**: Click "Add" or "Create New"
2. **Fill in Details**:
   - **Service Name**: `Monopoly Game`
   - **Protocol**: `TCP` (or `Both`)
   - **External Port**: `8501` (or your chosen port)
   - **Internal Port**: `8501` (same as external)
   - **Internal IP**: Your laptop's IP (e.g., `192.168.1.100`)
   - **Enabled**: `Yes` or `On`

### **Step 3.3: Save Configuration**
1. **Save**: Click "Save" or "Apply"
2. **Restart**: Some routers require restart
3. **Wait**: Wait for router to restart (1-2 minutes)

## 🛡️ Step 4: Configure Firewall

### **Windows Firewall:**
1. **Open Windows Defender**: Search "Windows Defender Firewall"
2. **Allow App**: Click "Allow an app through firewall"
3. **Add Python**: Add Python.exe to allowed apps
4. **Add Streamlit**: Add Streamlit to allowed apps

### **Mac Firewall:**
1. **System Preferences**: Apple menu → System Preferences
2. **Security & Privacy**: Click "Security & Privacy"
3. **Firewall**: Click "Firewall" tab
4. **Allow Python**: Add Python to allowed apps

### **Linux Firewall:**
1. **Open Terminal**: Press `Ctrl + Alt + T`
2. **Run Command**: `sudo ufw allow 8501`
3. **Enable**: `sudo ufw enable`

## 🌍 Step 5: Get Your Public IP

### **Find Public IP:**
1. **Open Browser**: Go to https://whatismyipaddress.com
2. **Note IP**: Copy your public IP address
3. **Example**: `123.456.789.012`

### **Test Access:**
1. **Create URL**: `http://[PUBLIC_IP]:8501`
2. **Test**: Try accessing from another device
3. **Verify**: Make sure it works

## 📱 Step 6: Test Public Access

### **Test from Mobile:**
1. **Disconnect WiFi**: Use mobile data (not WiFi)
2. **Open Browser**: Use mobile browser
3. **Enter URL**: `http://[PUBLIC_IP]:8501`
4. **Login**: Use Control Center password: `ferrari`

### **Test from Another Network:**
1. **Go Elsewhere**: Use a different WiFi network
2. **Open Browser**: Use any browser
3. **Enter URL**: `http://[PUBLIC_IP]:8501`
4. **Login**: Use Control Center password: `ferrari`

## 🔧 Excitel-Specific Instructions

### **TP-Link Excitel Routers:**
1. **Login**: Go to `192.168.1.1`
2. **Advanced**: Click "Advanced"
3. **NAT Forwarding**: Click "NAT Forwarding"
4. **Port Forwarding**: Click "Port Forwarding"
5. **Add Rule**: Click "Add" and configure

### **D-Link Excitel Routers:**
1. **Login**: Go to `192.168.1.1`
2. **Advanced**: Click "Advanced"
3. **Port Forwarding**: Click "Port Forwarding"
4. **Add Rule**: Click "Add" and configure

### **Generic Excitel Routers:**
1. **Login**: Go to your router's IP address
2. **Find Section**: Look for "Port Forwarding" or "Virtual Server"
3. **Add Rule**: Create new port forwarding rule
4. **Configure**: Fill in the details

## 🔍 Troubleshooting for Excitel Routers

### **Can't Access Router Admin Panel:**
1. **Check IP**: Try `192.168.1.1` and `192.168.0.1`
2. **Check Connection**: Make sure you're connected to Excitel WiFi
3. **Try Different Browser**: Use Chrome, Firefox, or Edge
4. **Reset Router**: Hold reset button for 30 seconds

### **Port Forwarding Not Working:**
1. **Check IP**: Make sure laptop IP is correct
2. **Check Port**: Make sure port number is correct
3. **Check Protocol**: Make sure protocol is TCP
4. **Restart Router**: Restart router after configuration

### **Can't Access from Internet:**
1. **Check Public IP**: Make sure public IP is correct
2. **Check Port**: Make sure port is forwarded correctly
3. **Check Firewall**: Make sure firewall allows the port
4. **Check Service**: Make sure Streamlit is running

### **Connection Refused:**
1. **Check Service**: Make sure Streamlit is running
2. **Check Port**: Make sure port is correct
3. **Check IP**: Make sure IP address is correct
4. **Check Firewall**: Make sure firewall allows the connection

## 🛡️ Security Considerations for Excitel

### **Before Going Public:**
- [ ] **Change Passwords**: Use strong, unique passwords
- [ ] **Enable HTTPS**: Use HTTPS if possible
- [ ] **Monitor Access**: Keep track of who's accessing
- [ ] **Backup Data**: Save important game data

### **During Public Use:**
- [ ] **Monitor Activity**: Watch for suspicious activity
- [ ] **Update Passwords**: Change passwords regularly
- [ ] **Limit Access**: Only share with authorized players
- [ ] **Log Activity**: Keep logs of game activity

### **After Public Use:**
- [ ] **Disable Port Forwarding**: Turn off port forwarding
- [ ] **Change Passwords**: Update all passwords
- [ ] **Review Logs**: Check for any issues
- [ ] **Backup Data**: Save important game data

## 📋 Quick Reference for Excitel

### **Common Excitel Router IPs:**
- `192.168.1.1` (Most common)
- `192.168.0.1`
- `192.168.2.1`
- `10.0.0.1`

### **Default Credentials:**
- **Username**: `admin`
- **Password**: `admin` or `password`

### **Port Forwarding Settings:**
- **Service Name**: `Monopoly Game`
- **Protocol**: `TCP`
- **External Port**: `8501`
- **Internal Port**: `8501`
- **Internal IP**: Your laptop's IP
- **Enabled**: `Yes`

### **Test URLs:**
- **Local**: `http://[LAPTOP_IP]:8501`
- **Public**: `http://[PUBLIC_IP]:8501`

### **Default Passwords:**
- **Control Center**: `ferrari`
- **Team 1**: `mercedes`
- **Team 2**: `mclaren`
- **Team 3**: `redbull`
- **Team 4**: `audi`
- **Team 5**: `astonmartin`

## 🎉 Success!

Once configured correctly, anyone can access your Monopoly game from anywhere on the internet using:
- **URL**: `http://[PUBLIC_IP]:8501`
- **Login**: Use appropriate team password
- **Access**: Full game control from anywhere!

## 📞 Excitel Support

### **If You Need Help:**
- **Excitel Support**: Contact Excitel customer support
- **Router Manual**: Check your router's manual
- **Online Support**: Check Excitel's website
- **Community Forums**: Ask on Excitel forums

### **Common Issues:**
- **Router Access**: Try different IP addresses
- **Port Forwarding**: Check configuration and restart router
- **Internet Access**: Verify public IP and port forwarding
- **Security**: Change default passwords and monitor access

Your Excitel WiFi router is now ready for **global internet access**! 🌐🎮
