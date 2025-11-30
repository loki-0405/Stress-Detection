# Stress Detection System - Setup Guide

## 📋 Project Overview

**Real-Time Stress Detection System Using Facial Expression Recognition and Heart Rate Monitoring**

A comprehensive desktop application that detects stress levels using facial expression analysis and heart rate monitoring.

---

## 🎯 Quick Start

### Prerequisites
- Windows 10/11 or macOS/Linux
- Python 3.8 or higher
- MySQL 8.0 or higher
- 8GB RAM minimum
- Webcam

---

## ⚙️ Installation Steps

### Step 1: Install Python 3.8+

```bash
# Download from: https://www.python.org/downloads/
# During installation, CHECK: "Add Python to PATH"

# Verify installation
python --version
```

### Step 2: Install MySQL Server

1. Download: https://dev.mysql.com/downloads/mysql/
2. Run installer with these settings:
   - **Server Type:** Development Machine
   - **Config Type:** Server Machine
   - **Port:** 3306
   - **MySQL Root Password:** `*******`

3. Start MySQL Service:
   ```bash
   # Windows
   net start MySQL80
   
   # Or use MySQL Notifier
   ```

### Step 3: Create Database

Open Command Prompt and run:

```bash
mysql -u root -p
```

Enter password: `*******`

Then copy-paste this entire block:

```sql
CREATE DATABASE stress_detection;

USE stress_detection;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stress_results (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    stress_score FLOAT NOT NULL,
    beats_per_minute FLOAT NOT NULL,
    date_recorded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE session_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    session_start TIMESTAMP,
    session_end TIMESTAMP,
    detection_type VARCHAR(20),
    frames_processed INT,
    average_fps FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

SHOW TABLES;
EXIT;
```

### Step 4: Download Project

Copy all project files to this folder.

### Step 5: Install Python Dependencies

```bash

# Install dependencies
pip install --upgrade pip

pip install opencv-python==4.5.4.60
pip install fer==21.0.2
pip install tensorflow==2.10.0
pip install PySerial==3.5
pip install numpy==1.21.0
pip install pandas==1.3.0
pip install Pillow==8.3.0
pip install matplotlib==3.4.3
pip install scipy==1.7.1
pip install mysql-connector-python==8.0.28
pip install PySimpleGUI==4.60.0
pip install scikit-learn==0.24.2
pip install imutils==0.5.4
```

### Step 6: Verify Setup

```bash
# Check Python packages
pip list

# Test imports
python -c "import cv2; print('✓ OpenCV OK')"
python -c "import tensorflow; print('✓ TensorFlow OK')"
python -c "import mysql.connector; print('✓ MySQL OK')"
python -c "from fer import FER; print('✓ FER OK')"
```

### Step 7: Configure Project

Edit `project.py` and update:

**Line 1-5 (Add missing imports):**
```python
import tkinter as tk
import cv2
import os
import time
import random
import mysql.connector
import numpy as np
from tkinter import ttk, Button, messagebox, filedialog
from PIL import Image, ImageTk
from datetime import datetime
from threading import Thread
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.interpolate import make_interp_spline
from fer.fer import FER
```

**Database credentials (around line 47):**
```python
try:
    self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*******",  # Change if different
        database="stress_detection"
    )
    self.cursor = self.db.cursor()
except mysql.connector.Error as err:
    messagebox.showwarning("Database Warning", f"Connection error: {err}")
```

**Image paths (around line 20):**
```python
# Update to your image path
image = Image.open("C:/Users/Happy/OneDrive/Pictures/a.jpg")
```

**Serial port (around line 188):**
```python
self.serial_port = 'COM15'  # Change to your port (COM3, COM4, etc.)
```

### Step 8: Run Application

```bash

# Run the application
python project.py
```

If it works, you should see:
- ✓ Splash screen with background image
- ✓ "Proceed" button
- ✓ Menu bar after clicking proceed
- ✓ Database connection message (if connected)

---

## 🔍 Verify Everything Works

### Test 1: Database Connection

```bash
mysql -u root -p
# Password: *****

USE stress_detection;
SHOW TABLES;
# Should show: users, stress_results, session_logs
```

### Test 2: Webcam

```python
python -c "import cv2; cap = cv2.VideoCapture(0); print('✓ Webcam works' if cap.isOpened() else '✗ Webcam failed'); cap.release()"
```

### Test 3: Pulse Sensor (if connected)

```python
import serial
port = serial.Serial('COM15', 9600, timeout=1)
print(port.readline())
port.close()
```

---

## 🆘 Troubleshooting

### Issue: "Python not found"
```
✓ Ensure Python added to PATH during installation
✓ Restart Command Prompt after Python installation
✓ Use: python --version to verify
```

### Issue: "MySQL connection refused"
```
✓ Start MySQL service:
  net start MySQL80

✓ Verify credentials in project.py

✓ Check database exists:
  mysql -u root -p
  SHOW DATABASES;
```

### Issue: "Module not found" error
```
✓ Ensure virtual environment activated
✓ Reinstall module:
  pip uninstall [module_name]
  pip install [module_name]
```

### Issue: "Webcam not working"
```
✓ Check if another app uses webcam
✓ Update camera drivers
✓ Try different camera index in code:
  cv2.VideoCapture(0)  # Try 0, 1, 2, etc.
```

### Issue: "Image file not found"
```
✓ Check image path exists:
  C:\Users\Happy\OneDrive\Pictures\a.jpg

✓ Use correct path separator (/ or \\)
```

---

## 📁 Project Structure

```
Final-project/
├── project.py                 # Main application
├── requirements.txt           # Dependencies list
├── README.md                  # This file
├── captured_images/           # Auto-created folder
│   ├── image_0.png
│   ├── image_1.png
│   └── ...

```

---

## 📊 Expected Output

### On First Run:
```
✓ Background image loads
✓ "Proceed" button visible
✓ Database connection successful (or warning if failed)
✓ Application ready to use
```

### On Stress Detection:
```
✓ Webcam activates
✓ Face detected with rectangle
✓ Emotions: Happy, Sad, Angry, etc. displayed
✓ Heart rate shown (if sensor connected)
✓ Stress score calculated and stored
```

---

## 🎮 How to Use

### 1. First Time
- Click "Proceed"
- Enter user details (name, age)
- Click "Submit"

### 2. Detect Stress
- Click "Detect Stress" tab
- Click "Start Detection"
- Keep face in view for 10 frames
- Wait for results

### 3. View Results
- Click "Results" tab
- Enter User ID
- Click "Fetch Results"
- View stress history

### 4. Upload Video
- Click "Upload Media"
- Select video file (.mp4, .avi)
- Results generated automatically

---

## 🔧 Advanced Configuration

### Change Database Credentials

Edit these lines in `project.py`:

```python
self.db = mysql.connector.connect(
    host="localhost",      # or IP address
    user="root",           # your MySQL username
    password="*****", # your MySQL password
    database="stress_detection"
)
```

### Find Your Serial Port

**Windows:**
```
Device Manager → Ports (COM & LPT) → Look for "Arduino" or "USB Serial"
```

**Linux:**
```bash
ls /dev/ttyUSB*
```

**macOS:**
```bash
ls /dev/tty.*
```

Update in `project.py`:
```python
self.serial_port = 'COM15'  # Change to your port
```

---

## ✅ Setup Checklist

- [ ] Python 3.8+ installed
- [ ] MySQL 8.0+ installed and running
- [ ] Database "stress_detection" created
- [ ] All tables created successfully
- [ ] Project files downloaded
- [ ] All Python packages installed
- [ ] project.py configured with correct paths
- [ ] Webcam connected and working
- [ ] Image file exists at specified path
- [ ] Application starts without errors

---

## 🚀 Next Steps

1. **Customize UI** - Edit colors, fonts in `project.py`
2. **Add Features** - Implement additional analysis
3. **Setup Arduino** - Connect pulse sensor for better accuracy
4. **Deploy** - Convert to .exe using PyInstaller

---

## 📞 Support

If you encounter issues:

1. Check all dependencies are installed: `pip list`
2. Verify MySQL is running: `mysql --version`
3. Test database: `mysql -u root -p`
4. Check Python version: `python --version`
5. Review error messages carefully

---

## 📝 Important Notes

⚠️ **Database Password:** Change `*******` to a secure password in production

⚠️ **Webcam Permissions:** Grant permissions if system asks

⚠️ **Firewall:** Ensure MySQL port 3306 is not blocked

⚠️ **Antivirus:** Add Python/MySQL to exclusions if issues occur

---

**Setup Complete! Ready to detect stress! 🎥💓📊**
