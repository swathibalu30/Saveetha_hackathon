# Automated Diagnostic System

A web-based medical diagnostic system powered by Machine Learning that predicts diseases based on patient vital signs and symptoms.

## Project Structure

```
Automated_Diagnostic_System/
│
├── app.py                          # Flask application with all routes
├── requirements.txt                # Python dependencies
│
├── model/
│   ├── diagnostic_model.pkl        # Trained ML model (generated after training)
│   └── model_training.ipynb        # Jupyter notebook for model training
│
├── static/
│   ├── css/style.css              # Application styling
│   ├── js/script.js               # Client-side JavaScript
│   └── images/
│       ├── logo.svg               # Medical logo (SVG)
│       └── logo.png               # Placeholder
│
├── templates/
│   ├── index.html                 # Home page
│   ├── diagnosis.html             # Patient input form
│   ├── result.html                # Diagnosis result page
│   ├── dashboard.html             # Patient records dashboard
│   ├── login.html                 # Login page
│   └── register.html              # Registration page
│
├── data/
│   └── sample_patient_data.csv    # Training dataset
│
└── utils/
    ├── db_connection.py           # MongoDB connection utility
    ├── preprocess.py              # Data preprocessing functions
    └── predict.py                 # Prediction utility
```

## Features

✅ **Machine Learning Diagnosis** - RandomForest classifier for disease prediction  
✅ **User Authentication** - Secure login system with MongoDB  
✅ **Patient Dashboard** - View all patient records and diagnoses  
✅ **Data Storage** - MongoDB integration for persistent storage  
✅ **Responsive Design** - Mobile-friendly interface  
✅ **Form Validation** - Client and server-side validation  

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (or local MongoDB installation)
- pip package manager

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure MongoDB

1. Create a MongoDB Atlas account at https://www.mongodb.com/cloud/atlas
2. Create a new cluster
3. Get your connection string
4. Update `utils/db_connection.py` with your MongoDB connection string:

```python
connection_string = "mongodb+srv://username:password@cluster.mongodb.net/"
```

### Step 3: Train the Model

Open and run the Jupyter notebook to train the model:

```bash
jupyter notebook model/model_training.ipynb
```

Run all cells in the notebook. This will:
- Load the sample patient data
- Train a RandomForestClassifier
- Save the model as `model/diagnostic_model.pkl`

Alternatively, you can run it as a Python script if you convert it.

### Step 4: Run the Application

```bash
python app.py
```

The application will be available at: `http://localhost:5000`

### Default Login Credentials

- **Username:** admin
- **Password:** admin123

⚠️ **Important:** Change these credentials in production!

## Usage Guide

### 1. Home Page
- Welcome page with system overview
- Navigation to diagnosis, dashboard, and login

### 2. Login
- Login with username and password
- Register new users if needed

### 3. Patient Diagnosis
- Fill in patient information:
  - Name
  - Age
  - Gender
  - Blood Pressure (mmHg)
  - Blood Glucose Level (mg/dL)
  - Heart Rate (bpm)
  - Symptoms
- Submit for diagnosis

### 4. Results
- View predicted diagnosis
- Save to patient records automatically

### 5. Dashboard
- View all patient records
- See complete medical history
- Access restricted to logged-in users

## Technology Stack

### Backend
- **Flask** - Web framework
- **Python 3.x** - Programming language
- **scikit-learn** - Machine learning
- **pandas** - Data manipulation
- **joblib** - Model serialization
- **pymongo** - MongoDB driver

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **JavaScript** - Interactivity
- **Responsive Design** - Mobile-friendly

### Database
- **MongoDB Atlas** - Cloud database

## Model Information

The diagnostic model uses a **RandomForestClassifier** trained on the following features:
- Age
- Gender (0=Male, 1=Female)
- Blood Pressure
- Blood Glucose Level
- Heart Rate

**Predicted Diseases Include:**
- Heart Disease
- Diabetes
- Hypertension
- Migraine
- Asthma
- Arthritis
- And more...

## Security Notes

⚠️ **Important Security Considerations:**

1. **Passwords**: In production, use proper password hashing (bcrypt, argon2)
2. **Secret Key**: Change the Flask secret key in `app.py`
3. **MongoDB**: Use environment variables for connection strings
4. **HTTPS**: Always use HTTPS in production
5. **Input Validation**: Already implemented but review for your use case

## Future Enhancements

- [ ] Password hashing with bcrypt
- [ ] Email verification
- [ ] PDF report generation
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] API endpoints for mobile apps
- [ ] Integration with medical devices
- [ ] Enhanced ML models with more features

## Troubleshooting

### Model Not Found Error
- Make sure you've run the `model_training.ipynb` notebook
- Check that `diagnostic_model.pkl` exists in the `model/` directory

### MongoDB Connection Error
- Verify your MongoDB connection string
- Check network connectivity
- Ensure MongoDB Atlas IP whitelist includes your IP

### Dependencies Issues
- Update pip: `python -m pip install --upgrade pip`
- Install dependencies one by one if batch install fails

## License

This project is for educational purposes. 

## Disclaimer

⚠️ **Medical Disclaimer**: This system provides preliminary diagnostic suggestions based on limited data. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical concerns.

## Contributors

Developed as part of a hackathon project to demonstrate ML integration in healthcare applications.

## Support

For issues and questions, please create an issue in the repository or contact the development team.

---

**Happy Diagnosing! 🏥💙**
