# 🔧 Router Configuration Guide for Port Forwarding

## 🌐 How to Configure Your Router for Public Internet Access

This guide will help you configure your router to forward ports to your laptop, allowing anyone to access your Monopoly game from anywhere on the internet.

## 📋 Prerequisites

### **What You Need:**
- **Router Admin Access**: Username and password for your router
- **Laptop IP Address**: Your laptop's local IP address
- **Port Number**: The port your Streamlit app uses (usually 8501)
- **Public IP**: Your router's public IP address

### **Before You Start:**
- [ ] Make sure your laptop is connected to the router via WiFi or Ethernet
- [ ] Note your laptop's local IP address
- [ ] Have your router's admin credentials ready
- [ ] Know which port your Streamlit app uses

## 🔍 Step 1: Find Your Laptop's IP Address

### **Windows:**
1. **Open Command Prompt**: Press `Win + R`, type `cmd`, press Enter
2. **Run Command**: Type `ipconfig` and press Enter
3. **Find IP**: Look for "IPv4 Address" under your network adapter
4. **Example**: `192.168.1.100`

### **Mac:**
1. **Open Terminal**: Press `Cmd + Space`, type "Terminal", press Enter
2. **Run Command**: Type `ifconfig` and press Enter
3. **Find IP**: Look for "inet" under your network adapter
4. **Example**: `192.168.1.100`

### **Linux:**
1. **Open Terminal**: Press `Ctrl + Alt + T`
2. **Run Command**: Type `ip addr show` and press Enter
3. **Find IP**: Look for "inet" under your network adapter
4. **Example**: `192.168.1.100`

## 🌐 Step 2: Find Your Router's Admin Panel

### **Common Router IP Addresses:**
- **192.168.1.1** (Most common)
- **192.168.0.1**
- **192.168.2.1**
- **10.0.0.1**
- **192.168.100.1**

### **How to Find Your Router IP:**
1. **Open Command Prompt/Terminal**
2. **Run**: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
3. **Look for**: "Default Gateway" or "Gateway"
4. **Example**: `192.168.1.1`

### **Access Router Admin Panel:**
1. **Open Browser**: Use Chrome, Firefox, Safari, etc.
2. **Enter IP**: Type your router's IP address
3. **Login**: Enter admin username and password
4. **Default Credentials**: Check router label or manual

## 🔧 Step 3: Configure Port Forwarding

### **Step 3.1: Access Port Forwarding Settings**
1. **Login**: Access your router's admin panel
2. **Navigate**: Look for "Port Forwarding", "Virtual Server", or "NAT"
3. **Common Locations**:
   - Advanced → Port Forwarding
   - Network → Port Forwarding
   - Firewall → Port Forwarding
   - Security → Port Forwarding

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

## 🔧 Router-Specific Instructions

### **Netgear Routers:**
1. **Login**: Go to `192.168.1.1`
2. **Advanced**: Click "Advanced"
3. **Port Forwarding**: Click "Port Forwarding"
4. **Add Rule**: Click "Add Custom Service"
5. **Configure**: Fill in port forwarding details

### **Linksys Routers:**
1. **Login**: Go to `192.168.1.1`
2. **Smart Wi-Fi**: Click "Smart Wi-Fi Tools"
3. **Port Forwarding**: Click "Port Forwarding"
4. **Add Rule**: Click "Add Port Forwarding Rule"
5. **Configure**: Fill in port forwarding details

### **TP-Link Routers:**
1. **Login**: Go to `192.168.1.1`
2. **Advanced**: Click "Advanced"
3. **NAT Forwarding**: Click "NAT Forwarding"
4. **Port Forwarding**: Click "Port Forwarding"
5. **Add Rule**: Click "Add" and configure

### **ASUS Routers:**
1. **Login**: Go to `192.168.1.1`
2. **Advanced Settings**: Click "Advanced Settings"
3. **WAN**: Click "WAN"
4. **Port Forwarding**: Click "Port Forwarding"
5. **Add Rule**: Click "Add" and configure

### **D-Link Routers:**
1. **Login**: Go to `192.168.1.1`
2. **Advanced**: Click "Advanced"
3. **Port Forwarding**: Click "Port Forwarding"
4. **Add Rule**: Click "Add" and configure

## 🔍 Troubleshooting

### **Can't Access Router Admin Panel:**
1. **Check IP**: Make sure you're using the correct IP address
2. **Check Connection**: Make sure you're connected to the router
3. **Try Different IPs**: Try common router IPs
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

## 🛡️ Security Considerations

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

## 📋 Quick Reference

### **Common Router IPs:**
- `192.168.1.1` (Most common)
- `192.168.0.1`
- `192.168.2.1`
- `10.0.0.1`

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

## 📞 Support

### **Router Issues:**
- **Check Manual**: Look at router manual
- **Contact ISP**: Contact your internet provider
- **Reset Router**: Hold reset button for 30 seconds
- **Update Firmware**: Update router firmware

### **Port Forwarding Issues:**
- **Check Configuration**: Verify port forwarding settings
- **Check IP**: Make sure laptop IP is correct
- **Check Port**: Make sure port number is correct
- **Restart Router**: Restart router after changes

### **Access Issues:**
- **Check Public IP**: Verify public IP address
- **Check Service**: Make sure Streamlit is running
- **Check Firewall**: Make sure firewall allows connection
- **Test Locally**: Test local access first

Your Monopoly game is now ready for **global internet access**! 🌐🎮
