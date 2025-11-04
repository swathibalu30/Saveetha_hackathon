@echo off
echo ================================================
echo   Automated Diagnostic System - Quick Setup
echo ================================================
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt
echo.

echo Step 2: Setup complete!
echo.
echo ================================================
echo   Next Steps:
echo ================================================
echo 1. Configure MongoDB connection in utils/db_connection.py
echo 2. Run model/model_training.ipynb to train the model
echo 3. Run: python app.py
echo 4. Open browser at: http://localhost:5000
echo 5. Login with: admin / admin123
echo.
echo For detailed instructions, see SETUP_GUIDE.md
echo.
pause
