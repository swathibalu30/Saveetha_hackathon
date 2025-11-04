"""
System Check Script
Verifies that all components are properly set up before running the application.
"""

import sys
import os

def check_dependencies():
    """Check if all required packages are installed"""
    print("Checking dependencies...")
    required_packages = [
        'flask',
        'pandas',
        'numpy',
        'sklearn',
        'joblib',
        'pymongo'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} - NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print(f"\n⚠ Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    return True

def check_files():
    """Check if all required files and directories exist"""
    print("\nChecking project structure...")
    
    required_items = {
        'directories': [
            'model',
            'static/css',
            'static/js',
            'static/images',
            'templates',
            'data',
            'utils'
        ],
        'files': [
            'app.py',
            'requirements.txt',
            'utils/db_connection.py',
            'utils/preprocess.py',
            'utils/predict.py',
            'data/sample_patient_data.csv',
            'templates/index.html',
            'templates/diagnosis.html',
            'templates/result.html',
            'templates/dashboard.html',
            'templates/login.html',
            'static/css/style.css',
            'static/js/script.js'
        ]
    }
    
    all_exist = True
    
    # Check directories
    for directory in required_items['directories']:
        if os.path.isdir(directory):
            print(f"  ✓ {directory}/")
        else:
            print(f"  ✗ {directory}/ - MISSING")
            all_exist = False
    
    # Check files
    for file in required_items['files']:
        if os.path.isfile(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - MISSING")
            all_exist = False
    
    return all_exist

def check_model():
    """Check if the ML model has been trained"""
    print("\nChecking ML model...")
    model_path = 'model/diagnostic_model.pkl'
    
    if os.path.isfile(model_path):
        print(f"  ✓ Model found: {model_path}")
        return True
    else:
        print(f"  ⚠ Model not found: {model_path}")
        print("  → Run: python train_model.py")
        print("  → Or use: jupyter notebook model/model_training.ipynb")
        return False

def check_mongodb_config():
    """Check if MongoDB connection string is configured"""
    print("\nChecking MongoDB configuration...")
    
    try:
        with open('utils/db_connection.py', 'r') as f:
            content = f.read()
            # Check if still using the placeholder
            if 'mongodb+srv://username:password@cluster' in content:
                print("  ⚠ MongoDB connection string not configured")
                print("  → Update utils/db_connection.py with your MongoDB Atlas credentials")
                return False
            # Check if configured (either localhost or Atlas)
            elif 'mongodb://localhost' in content or 'mongodb+srv://' in content:
                if 'mongodb://localhost' in content:
                    print("  ✓ MongoDB configured for local instance (localhost:27017)")
                else:
                    print("  ✓ MongoDB connection string configured")
                print("  → Make sure MongoDB is running")
                return True
            else:
                print("  ✓ MongoDB connection string appears to be configured")
                return True
    except Exception as e:
        print(f"  ✗ Error checking MongoDB config: {e}")
        return False

def main():
    """Run all checks"""
    print("=" * 60)
    print("  Automated Diagnostic System - Setup Check")
    print("=" * 60)
    print()
    
    checks = [
        ("Dependencies", check_dependencies()),
        ("Project Structure", check_files()),
        ("ML Model", check_model()),
        ("MongoDB Config", check_mongodb_config())
    ]
    
    print("\n" + "=" * 60)
    print("  Summary")
    print("=" * 60)
    
    for check_name, result in checks:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {check_name:20s}: {status}")
    
    all_passed = all(result for _, result in checks)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("  ✓ All checks passed! You're ready to run the application.")
        print("=" * 60)
        print("\nTo start the application:")
        print("  python app.py")
        print("\nThen visit: http://localhost:5000")
        print("Login with: admin / admin123")
    else:
        print("  ⚠ Some checks failed. Please fix the issues above.")
        print("=" * 60)
        print("\nSetup steps:")
        print("  1. pip install -r requirements.txt")
        print("  2. Update MongoDB connection in utils/db_connection.py")
        print("  3. python train_model.py")
        print("  4. python app.py")
    
    print()
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
