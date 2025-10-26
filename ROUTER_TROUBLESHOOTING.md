# 🔧 Router Configuration Troubleshooting Guide

## 🚨 Common Issues and Solutions

### **Issue 1: Can't Access Router Admin Panel**

#### **Symptoms:**
- Browser shows "This site can't be reached"
- "Connection refused" error
- Page loads but shows "Unauthorized"

#### **Solutions:**
1. **Check Router IP Address:**
   ```bash
   # Run this script to find your router IP
   python network_info.py
   ```

2. **Try Common Router IPs:**
   - `192.168.1.1` (Most common)
   - `192.168.0.1`
   - `192.168.2.1`
   - `10.0.0.1`
   - `192.168.100.1`

3. **Check Connection:**
   - Make sure you're connected to the router via WiFi or Ethernet
   - Try disconnecting and reconnecting to WiFi
   - Restart your laptop

4. **Reset Router:**
   - Hold the reset button for 30 seconds
   - Wait for router to restart
   - Try accessing admin panel again

### **Issue 2: Port Forwarding Not Working**

#### **Symptoms:**
- Local access works but public access doesn't
- "Connection refused" when accessing from internet
- Port forwarding rule exists but doesn't work

#### **Solutions:**
1. **Check Port Forwarding Configuration:**
   - **Service Name**: `Monopoly Game`
   - **Protocol**: `TCP` (or `Both`)
   - **External Port**: `8501`
   - **Internal Port**: `8501`
   - **Internal IP**: Your laptop's IP address
   - **Enabled**: `Yes` or `On`

2. **Verify Laptop IP:**
   ```bash
   # Run this to get your laptop's IP
   python network_info.py
   ```

3. **Check Port Number:**
   - Make sure you're using the correct port (usually 8501)
   - Check what port your Streamlit app is using

4. **Restart Router:**
   - Save port forwarding configuration
   - Restart router
   - Wait 2-3 minutes for router to restart

### **Issue 3: Can't Access from Internet**

#### **Symptoms:**
- Local access works fine
- Public URL doesn't work
- "This site can't be reached" from external devices

#### **Solutions:**
1. **Check Public IP:**
   ```bash
   # Get your public IP
   python network_info.py
   ```

2. **Test from Different Network:**
   - Use mobile data (not WiFi)
   - Try from a different WiFi network
   - Ask someone else to test the URL

3. **Check Port Forwarding:**
   - Verify port forwarding is configured correctly
   - Make sure the rule is enabled
   - Check that internal IP is correct

4. **Check Firewall:**
   - Windows: Allow Python/Streamlit through firewall
   - Mac: Allow Python in Security & Privacy
   - Linux: `sudo ufw allow 8501`

### **Issue 4: Connection Refused**

#### **Symptoms:**
- "Connection refused" error
- "This site can't be reached"
- Browser shows error page

#### **Solutions:**
1. **Check Streamlit Service:**
   - Make sure Streamlit is running
   - Check if the port is correct
   - Restart Streamlit if needed

2. **Check Port Number:**
   - Verify you're using the correct port
   - Check if port is already in use
   - Try a different port if needed

3. **Check IP Address:**
   - Make sure IP address is correct
   - Check if laptop IP has changed
   - Update port forwarding if needed

4. **Check Firewall:**
   - Allow Python/Streamlit through firewall
   - Check both Windows and router firewall
   - Temporarily disable firewall to test

### **Issue 5: Slow Performance**

#### **Symptoms:**
- Game loads slowly
- Laggy interface
- Timeout errors

#### **Solutions:**
1. **Check Internet Speed:**
   - Test your internet speed
   - Make sure you have good upload speed
   - Consider upgrading internet plan

2. **Check Router Performance:**
   - Restart router
   - Check router temperature
   - Update router firmware

3. **Check Laptop Performance:**
   - Close unnecessary programs
   - Check CPU and memory usage
   - Restart laptop if needed

4. **Check Network Congestion:**
   - Avoid peak hours
   - Use wired connection if possible
   - Check for interference

### **Issue 6: Security Concerns**

#### **Symptoms:**
- Unauthorized access attempts
- Suspicious activity
- Security warnings

#### **Solutions:**
1. **Change Passwords:**
   - Change all default passwords
   - Use strong, unique passwords
   - Update passwords regularly

2. **Monitor Access:**
   - Check router logs
   - Monitor game activity
   - Watch for suspicious behavior

3. **Limit Access:**
   - Only share URLs with authorized players
   - Use VPN for extra security
   - Close access when done

4. **Update Security:**
   - Update router firmware
   - Enable security features
   - Use HTTPS if possible

## 🔍 Diagnostic Steps

### **Step 1: Check Network Information**
```bash
python network_info.py
```
This will show:
- Your laptop's IP address
- Your public IP address
- Your router's IP address
- Port forwarding configuration

### **Step 2: Test Local Access**
1. Start your Monopoly game
2. Try accessing: `http://[LAPTOP_IP]:8501`
3. If this works, local setup is correct

### **Step 3: Test Public Access**
1. Use mobile data (not WiFi)
2. Try accessing: `http://[PUBLIC_IP]:8501`
3. If this works, port forwarding is correct

### **Step 4: Check Router Configuration**
1. Access router admin panel
2. Check port forwarding rules
3. Verify configuration is correct
4. Restart router if needed

## 🛠️ Advanced Troubleshooting

### **Check Port Status**
```bash
# Windows
netstat -an | findstr 8501

# Mac/Linux
netstat -an | grep 8501
```

### **Check Firewall Status**
```bash
# Windows
netsh advfirewall show allprofiles

# Mac
sudo pfctl -s rules

# Linux
sudo ufw status
```

### **Check Router Logs**
1. Access router admin panel
2. Go to "Logs" or "System Log"
3. Look for port forwarding entries
4. Check for errors or warnings

### **Test Port Forwarding**
```bash
# Test if port is open
telnet [PUBLIC_IP] 8501
```

## 📞 Getting Help

### **Router Support**
- **Check Manual**: Look at router manual
- **Contact ISP**: Contact your internet provider
- **Online Support**: Check router manufacturer's website
- **Community Forums**: Ask on router forums

### **Network Issues**
- **ISP Support**: Contact your internet provider
- **Network Admin**: Ask your network administrator
- **Online Tools**: Use network diagnostic tools
- **Professional Help**: Hire a network technician

### **Game Issues**
- **Check Logs**: Look at game and Streamlit logs
- **Restart Services**: Restart game and Streamlit
- **Check Configuration**: Verify all settings
- **Update Software**: Update Python and Streamlit

## 🎯 Quick Fixes

### **Most Common Solutions:**
1. **Restart Router**: Hold reset button for 30 seconds
2. **Restart Laptop**: Restart your laptop
3. **Check IP**: Make sure IP addresses are correct
4. **Check Port**: Verify port number is correct
5. **Check Firewall**: Allow Python/Streamlit through firewall

### **Emergency Reset:**
1. **Reset Router**: Hold reset button for 30 seconds
2. **Reconfigure**: Set up port forwarding again
3. **Test Access**: Test both local and public access
4. **Update Passwords**: Change all passwords

## 🎉 Success Indicators

### **Port Forwarding Working:**
- ✅ Local access works: `http://[LAPTOP_IP]:8501`
- ✅ Public access works: `http://[PUBLIC_IP]:8501`
- ✅ Access from different networks works
- ✅ No "Connection refused" errors

### **Security Working:**
- ✅ Password protection active
- ✅ Only authorized users can access
- ✅ No suspicious activity
- ✅ Regular password updates

Your Monopoly game should now be accessible from anywhere on the internet! 🌐🎮
