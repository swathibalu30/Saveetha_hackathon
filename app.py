from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from utils.db_connection import get_db_connection
from utils.predict import predict_disease
from utils.langchain_diagnosis import get_advanced_diagnosis, search_medical_condition
from datetime import datetime
import os
import secrets
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# SECURITY: Generate a secure secret key (or use environment variable)
app.secret_key = os.getenv('FLASK_SECRET_KEY', secrets.token_hex(32))

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'txt', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Get database connection
db = get_db_connection()


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')


@app.route('/diagnosis')
def diagnosis():
    """Diagnosis form page - requires login"""
    if 'username' not in session:
        flash('Please login to access the diagnosis page', 'warning')
        return redirect(url_for('login'))
    return render_template('diagnosis.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission and make prediction with input validation"""
    if 'username' not in session:
        flash('Please login to make a diagnosis', 'warning')
        return redirect(url_for('login'))
    
    try:
        # Get and validate form data
        name = request.form.get('name', '').strip()
        age_str = request.form.get('age', '').strip()
        gender = request.form.get('gender', '').strip()
        bp_str = request.form.get('bp', '').strip()
        glucose_str = request.form.get('glucose', '').strip()
        heart_rate_str = request.form.get('heart_rate', '').strip()
        symptoms = request.form.get('symptoms', '').strip()
        
        # Validation
        if not all([name, age_str, gender, bp_str, glucose_str, heart_rate_str, symptoms]):
            flash('All fields are required', 'danger')
            return redirect(url_for('diagnosis'))
        
        # Convert to integers with validation
        try:
            age = int(age_str)
            bp = int(bp_str)
            glucose = int(glucose_str)
            heart_rate = int(heart_rate_str)
        except ValueError:
            flash('Please enter valid numbers for age, blood pressure, glucose, and heart rate', 'danger')
            return redirect(url_for('diagnosis'))
        
        # Range validation
        if not (0 < age < 150):
            flash('Please enter a valid age', 'danger')
            return redirect(url_for('diagnosis'))
        
        if not (50 < bp < 250):
            flash('Please enter a valid blood pressure (50-250)', 'danger')
            return redirect(url_for('diagnosis'))
        
        if not (50 < glucose < 500):
            flash('Please enter a valid glucose level (50-500)', 'danger')
            return redirect(url_for('diagnosis'))
        
        if not (40 < heart_rate < 200):
            flash('Please enter a valid heart rate (40-200)', 'danger')
            return redirect(url_for('diagnosis'))
        
        # Prepare data for prediction
        patient_data = {
            'name': name[:100],  # Limit length
            'age': age,
            'gender': gender,
            'bp': bp,
            'glucose': glucose,
            'heart_rate': heart_rate,
            'symptoms': symptoms[:500]  # Limit length
        }
        
        # Make prediction
        diagnosis = predict_disease(patient_data)
        
        # Prepare data for MongoDB
        patient_record = {
            'name': patient_data['name'],
            'age': patient_data['age'],
            'gender': patient_data['gender'],
            'bp': patient_data['bp'],
            'glucose': patient_data['glucose'],
            'heart_rate': patient_data['heart_rate'],
            'symptoms': patient_data['symptoms'],
            'diagnosis': diagnosis,
            'date': datetime.now(),
            'diagnosed_by': session.get('username')
        }
        
        # Store in MongoDB
        if db is not None:
            db.patients.insert_one(patient_record)
        
        # Render result page
        return render_template('result.html', 
                             name=patient_data['name'], 
                             diagnosis=diagnosis)
    
    except Exception as e:
        flash(f'Error during prediction: Please check your input and try again', 'danger')
        return redirect(url_for('diagnosis'))


@app.route('/dashboard')
def dashboard():
    """Dashboard page showing all patient records - requires login"""
    if 'username' not in session:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))
    
    try:
        # Retrieve all patient records from MongoDB
        if db is not None:
            patients = list(db.patients.find())
        else:
            patients = []
        
        return render_template('dashboard.html', patients=patients)
    
    except Exception as e:
        flash(f'Error retrieving patient data: {str(e)}', 'danger')
        return render_template('dashboard.html', patients=[])


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and authentication"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        # Input validation
        if not username or not password:
            flash('Please provide both username and password', 'danger')
            return render_template('login.html')
        
        # Check credentials in MongoDB
        if db is not None:
            user = db.users.find_one({'username': username})
            
            if user:
                # Check if password is hashed (new) or plain text (old/demo)
                if 'password_hash' in user:
                    if check_password_hash(user['password_hash'], password):
                        session['username'] = username
                        session['user_id'] = str(user['_id'])
                        flash('Login successful!', 'success')
                        return redirect(url_for('dashboard'))
                    else:
                        flash('Invalid username or password', 'danger')
                else:
                    # Legacy support for plain text passwords (demo account)
                    if user.get('password') == password:
                        session['username'] = username
                        session['user_id'] = str(user['_id'])
                        flash('Login successful! Please consider updating your password.', 'warning')
                        return redirect(url_for('dashboard'))
                    else:
                        flash('Invalid username or password', 'danger')
            else:
                flash('Invalid username or password', 'danger')
        else:
            flash('Database connection error', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout route"""
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register new user with password hashing"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        # Input validation
        if not username or not password:
            flash('Please provide both username and password', 'danger')
            return render_template('register.html')
        
        if len(username) < 3:
            flash('Username must be at least 3 characters long', 'danger')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long', 'danger')
            return render_template('register.html')
        
        # Sanitize username (allow only alphanumeric and underscore)
        if not username.replace('_', '').isalnum():
            flash('Username can only contain letters, numbers, and underscores', 'danger')
            return render_template('register.html')
        
        if db is not None:
            # Check if user already exists
            existing_user = db.users.find_one({'username': username})
            
            if existing_user:
                flash('Username already exists. Please choose another.', 'danger')
            else:
                # Hash the password
                password_hash = generate_password_hash(password, method='pbkdf2:sha256')
                
                # Create new user
                db.users.insert_one({
                    'username': username,
                    'password_hash': password_hash,
                    'created_at': datetime.now(),
                    'last_login': None
                })
                flash('Registration successful! Please login.', 'success')
                return redirect(url_for('login'))
        else:
            flash('Database connection error', 'danger')
    
    return render_template('register.html')


@app.route('/upload_report', methods=['GET', 'POST'])
def upload_report():
    """Upload and analyze medical reports"""
    if 'username' not in session:
        flash('Please login to upload reports', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Check if file was uploaded
        if 'report_file' not in request.files:
            flash('No file selected', 'danger')
            return redirect(request.url)
        
        file = request.files['report_file']
        
        # Check if file is empty
        if file.filename == '':
            flash('No file selected', 'danger')
            return redirect(request.url)
        
        # Validate and save file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Add timestamp to filename to avoid conflicts
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Get patient information from form
            patient_name = request.form.get('patient_name', 'Unknown')
            report_type = request.form.get('report_type', 'General')
            notes = request.form.get('notes', '')
            
            # Store report information in database
            report_record = {
                'filename': filename,
                'original_filename': file.filename,
                'filepath': filepath,
                'patient_name': patient_name,
                'report_type': report_type,
                'notes': notes,
                'uploaded_by': session.get('username'),
                'upload_date': datetime.now(),
                'file_size': os.path.getsize(filepath),
                'status': 'uploaded'
            }
            
            if db is not None:
                result = db.reports.insert_one(report_record)
                report_id = str(result.inserted_id)
            else:
                report_id = None
            
            flash(f'Report uploaded successfully: {file.filename}', 'success')
            return render_template('report_uploaded.html', 
                                 filename=file.filename,
                                 patient_name=patient_name,
                                 report_type=report_type,
                                 report_id=report_id)
        else:
            flash('Invalid file type. Allowed types: PDF, PNG, JPG, JPEG, TXT, DOC, DOCX', 'danger')
            return redirect(request.url)
    
    return render_template('upload_report.html')


@app.route('/reports')
def view_reports():
    """View all uploaded reports"""
    if 'username' not in session:
        flash('Please login to view reports', 'warning')
        return redirect(url_for('login'))
    
    try:
        # Retrieve all reports from MongoDB
        if db is not None:
            reports = list(db.reports.find().sort('upload_date', -1))
        else:
            reports = []
        
        return render_template('reports.html', reports=reports)
    
    except Exception as e:
        flash(f'Error retrieving reports: {str(e)}', 'danger')
        return render_template('reports.html', reports=[])


@app.route('/advanced_diagnosis')
def advanced_diagnosis():
    """Advanced AI-powered diagnosis page"""
    if 'username' not in session:
        flash('Please login to access advanced diagnosis', 'warning')
        return redirect(url_for('login'))
    return render_template('advanced_diagnosis.html')


@app.route('/advanced_predict', methods=['POST'])
def advanced_predict():
    """Handle advanced diagnosis with LangChain and online sources"""
    if 'username' not in session:
        return jsonify({'error': 'Please login first'}), 401
    
    try:
        # Get form data
        patient_data = {
            'name': request.form.get('name'),
            'age': int(request.form.get('age')),
            'gender': request.form.get('gender'),
            'bp': int(request.form.get('bp')),
            'glucose': int(request.form.get('glucose')),
            'heart_rate': int(request.form.get('heart_rate')),
            'symptoms': request.form.get('symptoms', '')
        }
        
        # Get LLM provider preference (default to Groq - fast & free)
        llm_provider = request.form.get('llm_provider', 'groq')
        
        # Parse symptoms into list
        symptoms_list = [s.strip() for s in patient_data['symptoms'].split(',') if s.strip()]
        
        # First, get ML model prediction
        ml_diagnosis = predict_disease(patient_data)
        
        # Get comprehensive diagnosis using LangChain
        comprehensive_report = get_advanced_diagnosis(
            symptoms=symptoms_list,
            patient_data=patient_data,
            ml_prediction=ml_diagnosis,
            llm_provider=llm_provider
        )
        
        # Store in MongoDB
        if db is not None:
            diagnosis_record = {
                'name': patient_data['name'],
                'age': patient_data['age'],
                'gender': patient_data['gender'],
                'bp': patient_data['bp'],
                'glucose': patient_data['glucose'],
                'heart_rate': patient_data['heart_rate'],
                'symptoms': patient_data['symptoms'],
                'ml_diagnosis': ml_diagnosis,
                'comprehensive_report': comprehensive_report,
                'date': datetime.now(),
                'diagnosed_by': session.get('username'),
                'diagnosis_type': 'advanced'
            }
            db.patients.insert_one(diagnosis_record)
        
        # Render result page
        return render_template('advanced_result.html',
                             patient_data=patient_data,
                             ml_diagnosis=ml_diagnosis,
                             report=comprehensive_report)
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"❌ Error during advanced diagnosis: {str(e)}")
        print(f"📋 Full traceback:\n{error_details}")
        flash(f'Error during advanced diagnosis: {str(e)}', 'danger')
        return redirect(url_for('advanced_diagnosis'))


@app.route('/search_condition', methods=['POST'])
def search_condition():
    """Search for medical condition information"""
    if 'username' not in session:
        return jsonify({'error': 'Please login first'}), 401
    
    try:
        data = request.get_json()
        condition = data.get('condition', '')
        
        if not condition:
            return jsonify({'error': 'No condition specified'}), 400
        
        # Search for medical information
        result = search_medical_condition(condition)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Create a default user if database is available
    if db is not None:
        # Check if users collection exists and is empty
        if db.users.count_documents({}) == 0:
            db.users.insert_one({
                'username': 'admin',
                'password': 'admin123',  # Change this in production!
                'created_at': datetime.now()
            })
            print("Default user created: username='admin', password='admin123'")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
