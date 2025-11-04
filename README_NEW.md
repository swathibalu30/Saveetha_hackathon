# 🏥 Automated Diagnostic System

> A Machine Learning-powered web application for medical diagnosis based on patient vital signs

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![ML](https://img.shields.io/badge/ML-scikit--learn-orange.svg)](https://scikit-learn.org/)
[![Database](https://img.shields.io/badge/Database-MongoDB-brightgreen.svg)](https://www.mongodb.com/)

## 📋 Project Overview

The Automated Diagnostic System is a full-stack web application that uses Machine Learning to predict potential diseases based on patient data including vital signs and symptoms. The system features user authentication, patient record management, and an intuitive dashboard for healthcare professionals.

## ✨ Features

- 🤖 **AI-Powered Diagnosis** - RandomForest ML model for disease prediction
- 🔐 **Secure Authentication** - User login/registration with session management
- 📊 **Patient Dashboard** - View and manage all patient records
- 💾 **Cloud Database** - MongoDB Atlas integration for data persistence
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile
- ✅ **Form Validation** - Client and server-side input validation
- 🎨 **Modern UI** - Clean, professional medical interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- MongoDB Atlas account (free tier works fine)

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure MongoDB:**
   - Sign up for [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
   - Create a cluster and get your connection string
   - Update `utils/db_connection.py`:
     ```python
     connection_string = "mongodb+srv://your_username:your_password@cluster.mongodb.net/"
     ```

3. **Train the ML model:**
   ```bash
   python train_model.py
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the system:**
   - Open browser: `http://localhost:5000`
   - Login with: `admin` / `admin123`

### Automated Setup (Windows)
Double-click `setup.bat` and follow the instructions!

### Verify Setup
```bash
python check_setup.py
```

## 📖 Usage Guide

### 1. Login
- Use default credentials: `admin` / `admin123`
- Or register a new account

### 2. Patient Diagnosis
Navigate to the diagnosis page and enter patient information:
- Patient Name, Age, Gender
- Blood Pressure, Blood Glucose, Heart Rate
- Symptoms description

### 3. View Results
- Get instant AI-powered diagnosis
- Results are automatically saved

### 4. Dashboard
- View all patient records
- Track diagnoses over time

## 🧠 Machine Learning Model

- **Algorithm:** RandomForestClassifier
- **Features:** Age, Gender, BP, Glucose, Heart Rate
- **Diseases:** 15+ conditions including Heart Disease, Diabetes, Hypertension, and more

## 🛠️ Technology Stack

**Backend:** Flask, scikit-learn, pandas, NumPy, pymongo  
**Frontend:** HTML5, CSS3, JavaScript  
**Database:** MongoDB Atlas  

## 📚 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup instructions
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project documentation

## ⚠️ Medical Disclaimer

**This system is for educational purposes only** and should NOT be used for actual medical diagnosis. Always consult qualified healthcare professionals.

## 🎯 Project Status

✅ **All 8 Development Stages Completed**

---

**Made with ❤️ for improving healthcare through AI**
