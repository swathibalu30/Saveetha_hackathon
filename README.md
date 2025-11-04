# 🏥 Automated Diagnostic System with Advanced AI

## Overview
A comprehensive web-based medical diagnostic system that combines MachineStage 6: HTML Templates

For Home:

Create templates/index.html with a welcome message and a button that links to /diagnosis.

For Diagnosis Form:

Create templates/diagnosis.html with input fields for name, age, gender, BP, glucose, heart rate, and symptoms, submitting to /predict.

For Result:

Create templates/result.html to display the patient's name and predicted diagnosis.

Stage 7: Dashboard Page
Add a new Flask route /dashboard that retrieves all documents from the MongoDB patients collection and passes them to dashboard.html for display.
Create templates/dashboard.html to display a table of patient name, age, gender, and diagnosis using a Flask for-loop.

Stage 8: Login System
Create a users collection in MongoDB and implement a simple login route in Flask. Add an HTML login page and restrict access to /dashboard only after login.

---

## 🤖 Advanced AI Diagnosis Features

### How It Works

```
Patient Input → ML Model → AI Analysis → PubMed Search → Web Research → Comprehensive Report
     ↓              ↓           ↓             ↓              ↓                ↓
  Vitals      Random Forest  LangChain    Medical      DuckDuckGo      Combined
  Symptoms    Prediction     Gemini/GPT   Articles     Wikipedia       Insights
```

### What You Get

1. **ML Prediction** - Fast, trained model diagnosis
2. **AI Differential Diagnosis** - Multiple possible conditions ranked by likelihood
3. **Medical Reasoning** - Why this diagnosis is most likely
4. **Research Articles** - Latest PubMed publications (with links)
5. **Wikipedia Summary** - Quick medical reference
6. **Web Search Results** - Current medical information
7. **Recommended Tests** - What tests should be ordered next
8. **Warning Signs** - Symptoms requiring immediate attention
9. **Treatment Recommendations** - Evidence-based suggestions

### AI Providers

| Provider | Cost | Quality | Setup Time | Best For |
|----------|------|---------|------------|----------|
| **Google Gemini** | FREE | Excellent | 2 min | Everyone |
| **OpenAI GPT-3.5** | ~$0.01-0.05/diagnosis | Excellent | 3 min | Premium users |

### Example Analysis

**Input:**
```
Patient: John Doe, 45, Male
BP: 155 mmHg | Glucose: 180 mg/dL | HR: 88 bpm
Symptoms: frequent urination, excessive thirst, fatigue, blurred vision
```

**Output:**
- ML Model: "Diabetes"
- AI Analysis: "Type 2 Diabetes Mellitus (primary), Hyperglycemia (secondary), Metabolic Syndrome (consider)"
- PubMed: 3 recent research articles on T2DM management
- Recommended Tests: HbA1c, Fasting Blood Glucose, Lipid Panel
- Warning Signs: Diabetic ketoacidosis symptoms
- Recommendations: Diet modification, exercise regimen, glucose monitoring

### Setup Guide

**Quick Setup (2 minutes):**
```powershell
# Run interactive setup wizard
.\setup_advanced_diagnosis.ps1
```

**Or manually:**
1. Get free API key: https://makersuite.google.com/app/apikey
2. Set environment variable: `$env:GOOGLE_API_KEY="your_key"`
3. Restart Flask app
4. Visit /advanced_diagnosis

**Full documentation:** See `ADVANCED_DIAGNOSIS_GUIDE.md`

---

## 📊 Model Performance

- **Algorithm:** Random Forest Classifier
- **Training Samples:** 72 patient records
- **Features:** Age, Gender, Blood Pressure, Glucose, Heart Rate
- **Accuracy:** 80%
- **Conditions Detected:** 13 different diagnoses

**Feature Importance:**
1. Glucose Level: 32.84%
2. Blood Pressure: 23.83%
3. Heart Rate: 19.86%
4. Age: 15.88%
5. Gender: 7.59%

---

## 🔒 Security & Privacy

### Current Implementation
- ✅ Session-based authentication
- ✅ MongoDB data storage
- ✅ Secure file uploads with validation
- ✅ Environment variables for API keys
- ✅ HTTPS encryption (when deployed)

### Important Notes
⚠️ **This system is for educational purposes only**
- Not HIPAA compliant in current form
- Not intended for production medical use
- Always consult qualified healthcare professionals
- AI analysis is supplementary, not diagnostic

### For Production Use
- [ ] Implement HIPAA-compliant hosting
- [ ] Add end-to-end encryption
- [ ] Implement audit logging
- [ ] Sign Business Associate Agreements (BAAs)
- [ ] Add role-based access control (RBAC)
- [ ] Implement data anonymization
- [ ] Add backup and disaster recovery
- [ ] Conduct security penetration testing

---

## 📚 Documentation

- **[ADVANCED_DIAGNOSIS_GUIDE.md](ADVANCED_DIAGNOSIS_GUIDE.md)** - Complete setup and usage guide for AI features
- **[QUICK_START_ADVANCED.md](QUICK_START_ADVANCED.md)** - Quick reference card for advanced diagnosis
- **[UPLOAD_FEATURE_GUIDE.md](UPLOAD_FEATURE_GUIDE.md)** - Medical report upload documentation
- **[TESTING_GUIDE.md](TESTING_GUIDE.md)** - Testing procedures and examples

---

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.0** - Web framework
- **Python 3.12** - Programming language
- **MongoDB** - NoSQL database
- **scikit-learn 1.3.2** - Machine learning
- **LangChain** - AI orchestration framework
- **Google Gemini / OpenAI** - Large Language Models

### AI & Research
- **LangChain Community** - Tools and integrations
- **PubMed E-utilities API** - Medical research database (free)
- **DuckDuckGo Search** - Web search engine
- **Wikipedia API** - Medical reference

### Frontend
- **HTML5/CSS3** - Structure and styling
- **JavaScript** - Client-side interactivity
- **Responsive Design** - Mobile-friendly interface

---

## 🚀 Usage Examples

### Basic Diagnosis
```python
# Input patient vitals
age = 45
gender = "Male"
bp = 140
glucose = 180
heart_rate = 85

# Get prediction
diagnosis = predict_disease(patient_data)
# Output: "Diabetes"
```

### Advanced AI Diagnosis
```python
# Same input + symptoms
symptoms = ["frequent urination", "excessive thirst", "fatigue"]

# Get comprehensive analysis
report = get_advanced_diagnosis(
    symptoms=symptoms,
    patient_data=patient_data,
    ml_prediction="Diabetes",
    llm_provider="google"
)

# Output includes:
# - Differential diagnosis
# - PubMed articles
# - Treatment recommendations
# - Warning signs
```

---

## 🤝 Contributing

### Areas for Improvement
- [ ] Additional ML models (neural networks, ensemble methods)
- [ ] More medical data sources
- [ ] Multi-language support
- [ ] Voice input for symptoms
- [ ] Image analysis for medical reports
- [ ] Drug interaction checking
- [ ] Integration with EHR systems
- [ ] Telemedicine features

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Test thoroughly
5. Submit a pull request

---

## ⚠️ Medical Disclaimer

**IMPORTANT:** This system is designed for **EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY**.

**This is NOT:**
- ❌ A substitute for professional medical advice
- ❌ A diagnostic tool for clinical use
- ❌ A replacement for seeing a doctor
- ❌ Approved for medical decision-making

**You MUST:**
- ✅ Consult qualified healthcare professionals
- ✅ Seek immediate medical attention for emergencies
- ✅ Verify all information with licensed practitioners
- ✅ Use only as a learning/research tool

**In case of medical emergency, call your local emergency number immediately.**

---

## 📞 Resources & Links

### API Keys
- **Google Gemini (FREE):** https://makersuite.google.com/app/apikey
- **OpenAI (PAID):** https://platform.openai.com/api-keys

### Medical Databases
- **PubMed:** https://pubmed.ncbi.nlm.nih.gov/
- **MedlinePlus:** https://medlineplus.gov/
- **WHO:** https://www.who.int/
- **CDC:** https://www.cdc.gov/

### Documentation
- **LangChain:** https://python.langchain.com/
- **Flask:** https://flask.palletsprojects.com/
- **scikit-learn:** https://scikit-learn.org/

---

## 📝 License

This project is for educational purposes. See LICENSE file for details.

---

## 🎉 Quick Start Checklist

- [ ] Install Python 3.12+
- [ ] Install MongoDB
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Get Google Gemini API key (free, 2 minutes)
- [ ] Run setup script: `.\setup_advanced_diagnosis.ps1`
- [ ] Train model: `python train_model.py`
- [ ] Start app: `python app.py`
- [ ] Visit: http://127.0.0.1:5000
- [ ] Try Basic Diagnosis
- [ ] Try Advanced AI Diagnosis 🤖
- [ ] Upload a medical report
- [ ] Explore the dashboard

**You're ready to go!** 🚀

---

**Version:** 2.0.0 (with Advanced AI)  
**Last Updated:** November 4, 2025  
**Developed by:** Automated Diagnostic System Teams with advanced AI analysis using LangChain, PubMed research, and real-time medical sources.

## 🌟 Features

### Core Features
- ✅ **ML-Powered Diagnosis** - Random Forest model trained on patient vitals
- ✅ **Patient Dashboard** - Complete records management system
- ✅ **Medical Report Upload** - Secure file storage with metadata tracking
- ✅ **User Authentication** - Login system with session management
- ✅ **MongoDB Integration** - NoSQL database for scalable storage

### 🆕 Advanced AI Features (NEW!)
- 🤖 **AI Differential Diagnosis** - LangChain-powered analysis with Gemini/GPT
- 📚 **PubMed Research** - Access to latest medical research articles
- 🌐 **Medical Web Search** - Real-time information from trusted sources
- 📊 **Comprehensive Reports** - Combined ML + AI + Research insights
- 💡 **Treatment Recommendations** - Evidence-based suggestions
- ⚠️ **Warning Signs** - Critical symptoms identification

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- MongoDB (localhost:27017)
- Google Gemini API key (free) OR OpenAI API key (paid)

### Installation

1. **Clone and navigate:**
```bash
cd d:\Hackathon
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Setup API key for Advanced AI (Optional but Recommended):**

**Option 1: Use Setup Script**
```powershell
.\setup_advanced_diagnosis.ps1
```

**Option 2: Manual Setup**
```powershell
# Get free API key from: https://makersuite.google.com/app/apikey
$env:GOOGLE_API_KEY="your_api_key_here"
```

4. **Train the ML model:**
```bash
python train_model.py
```

5. **Start the application:**
```bash
python app.py
```

6. **Access the system:**
- Home: http://127.0.0.1:5000
- Basic Diagnosis: http://127.0.0.1:5000/diagnosis
- **Advanced AI Diagnosis: http://127.0.0.1:5000/advanced_diagnosis** 🆕
- Dashboard: http://127.0.0.1:5000/dashboard

### Default Login
- Username: `admin`
- Password: `admin123`

## 📁 Project Structure

Stage 1:

Automated_Diagnostic_System/
│
├── app.py                              # Main Flask application
├── requirements.txt                    # Python dependencies
├── train_model.py                      # Model training script
│
├── model/
│   ├── diagnostic_model.pkl           # Trained ML model
│   └── model_training.ipynb           # Training notebook
│
├── static/
│   ├── css/style.css                  # Styling
│   ├── js/script.js                   # Client-side logic
│   └── images/logo.png                # Assets
│
├── templates/
│   ├── index.html                     # Home page
│   ├── diagnosis.html                 # Basic diagnosis form
│   ├── advanced_diagnosis.html        # 🆕 Advanced AI form
│   ├── advanced_result.html           # 🆕 AI analysis results
│   ├── result.html                    # Basic results
│   ├── dashboard.html                 # Patient records
│   ├── upload_report.html             # Report upload
│   └── reports.html                   # Reports repository
│
├── data/
│   └── sample_patient_data.csv        # Training dataset (72 samples)
│
├── utils/
│   ├── db_connection.py               # MongoDB connection
│   ├── preprocess.py                  # Data preprocessing
│   ├── predict.py                     # ML prediction
│   └── langchain_diagnosis.py         # 🆕 Advanced AI diagnosis
│
├── uploads/                            # Medical report storage
│
└── docs/
    ├── ADVANCED_DIAGNOSIS_GUIDE.md    # 🆕 Complete AI setup guide
    ├── QUICK_START_ADVANCED.md        # 🆕 Quick reference
    └── UPLOAD_FEATURE_GUIDE.md        # Report upload docs

Include requirements.txt with Flask, pandas, numpy, scikit-learn, joblib, pymongo, langchain, langchain-community, langchain-google-genai, and related packages.

Stage 2: MongoDB Connection Setup
In utils/db_connection.py, write a function get_db_connection() that connects to a MongoDB Atlas cluster and returns the database instance named diagnostic_system.

Stage 3: Model Training Notebook
In model/model_training.ipynb, write Python code to train a RandomForestClassifier using a sample dataset data/sample_patient_data.csv, then save it as diagnostic_model.pkl using joblib.

Stage 4: Utility Scripts
For preprocessing:

In utils/preprocess.py, create a function that converts gender text to numeric (0 for Male, 1 for Female).

For prediction:

In utils/predict.py, write a function predict_disease() that loads the saved model, processes the input data using preprocess_input(), and returns the predicted disease name.

Stage 5: Flask App Setup
In app.py, create a Flask app with three routes — / for home, /diagnosis for input form, and /predict to handle POST form submission. Use the prediction utility and store patient data into MongoDB.

Stage 6: HTML Templates

For Home:

Create templates/index.html with a welcome message and a button that links to /diagnosis.

For Diagnosis Form:

Create templates/diagnosis.html with input fields for name, age, gender, BP, glucose, heart rate, and symptoms, submitting to /predict.

For Result:

Create templates/result.html to display the patient’s name and predicted diagnosis.

Stage 7: Dashboard Page
Add a new Flask route /dashboard that retrieves all documents from the MongoDB patients collection and passes them to dashboard.html for display.
Create templates/dashboard.html to display a table of patient name, age, gender, and diagnosis using a Flask for-loop.

Stage 8:  Login System
Create a users collection in MongoDB and implement a simple login route in Flask. Add an HTML login page and restrict access to /dashboard only after login.