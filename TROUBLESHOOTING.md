# 🔧 Troubleshooting Guide - MediCare Health Platform

## ✅ Issue Fixed: "No module named 'langchain_groq'"

### Problem:
When trying to use the Advanced AI Diagnosis feature, you saw this error:
```
⚠️  Error initializing LLM: No module named 'langchain_groq'
```

### Root Cause:
The `langchain-groq` package was installed in the **system Python** instead of the **virtual environment** (`.venv`) that Flask uses.

### Solution Applied:
```powershell
# 1. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 2. Install langchain-groq in virtual environment
pip install langchain-groq

# 3. Restart Flask server
python app.py
```

### ✅ Status: **FIXED**
- Package installed: `langchain-groq==1.0.0` ✅
- Package installed: `groq==0.33.0` ✅
- Server running: http://127.0.0.1:5000 ✅
- Groq API ready: Llama 3.3 70B model ✅

---

## 🚨 Common Issues & Solutions

### 1. Module Not Found Errors

**Error**: `No module named 'xyz'`

**Solution**:
```powershell
# Always use virtual environment
.\.venv\Scripts\Activate.ps1

# Install missing package
pip install package-name

# Restart Flask
python app.py
```

---

### 2. Flask Server Not Starting

**Error**: `Address already in use` or server won't start

**Solution**:
```powershell
# Check running Python processes
Get-Process python* | Select-Object Id, ProcessName

# Stop old processes
Stop-Process -Id <PROCESS_ID> -Force

# Start fresh
.\.venv\Scripts\Activate.ps1
python app.py
```

---

### 3. MongoDB Connection Error

**Error**: `Failed to connect to MongoDB`

**Solution**:
```powershell
# Check MongoDB is running
Get-Process mongod

# Start MongoDB
mongod --dbpath "C:\data\db"

# Or use MongoDB Compass
# Start MongoDB service from Windows Services
```

---

### 4. Groq API Key Not Found

**Error**: `⚠️ GROQ_API_KEY not found in environment`

**Solution**:
```powershell
# Check .env file exists
Get-Content .env

# Verify key is set
GROQ_API_KEY=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

# Restart Flask server
python app.py
```

---

### 5. Import Error in langchain_diagnosis.py

**Error**: `ImportError: cannot import name 'ChatGroq'`

**Solution**:
```powershell
# Verify package installed
pip list | Select-String "groq"

# Should show:
# groq                         0.33.0
# langchain-groq               1.0.0

# If missing, install
pip install langchain-groq
```

---

### 6. AI Diagnosis Returns Error

**Error**: `Error getting advanced diagnosis`

**Possible Causes**:
1. API key invalid
2. Rate limit exceeded (30 req/min free tier)
3. Network connection issue
4. Groq service down

**Solution**:
```python
# Check terminal logs for specific error
# Look for:
# - "401 Unauthorized" → Invalid API key
# - "429 Rate Limit" → Too many requests
# - "Connection timeout" → Network issue
# - "500 Server Error" → Groq service issue
```

---

### 7. Virtual Environment Not Activated

**Error**: Packages installed but Flask can't find them

**Solution**:
```powershell
# Always activate BEFORE running Flask
.\.venv\Scripts\Activate.ps1

# Check activation (should show (.venv) in prompt)
# (.venv) PS D:\Hackathon>

# Then run
python app.py
```

---

### 8. Package Version Conflicts

**Error**: `ImportError` or compatibility issues

**Solution**:
```powershell
# Check installed versions
pip list

# Verify requirements.txt
Get-Content requirements.txt

# Reinstall from requirements
pip install -r requirements.txt --upgrade
```

---

### 9. Port 5000 Already in Use

**Error**: `OSError: [WinError 10048] Only one usage of each socket address`

**Solution**:
```powershell
# Find process using port 5000
netstat -ano | Select-String "5000"

# Kill process (replace PID)
Stop-Process -Id <PID> -Force

# Or use different port in app.py
# app.run(debug=True, host='0.0.0.0', port=5001)
```

---

### 10. Static Files Not Loading (CSS/JS/Images)

**Error**: 404 errors for `/static/css/style.css`

**Solution**:
```powershell
# Check static folder structure
Get-ChildItem static -Recurse

# Should have:
# static/
#   css/
#     style.css
#   js/
#     script.js
#   images/
#     logo.png

# Clear browser cache
# Ctrl + Shift + R (Chrome)
# Ctrl + F5 (Firefox)
```

---

## 🔍 Debugging Tips

### Enable Verbose Logging

Add to `app.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Environment Variables

```powershell
# Verify .env loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('GROQ_API_KEY:', bool(os.getenv('GROQ_API_KEY')))"
```

### Test Groq API Directly

```python
# Create test script: test_groq.py
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

response = llm.invoke("Say hello!")
print(response.content)
```

Run: `python test_groq.py`

---

## 📊 Health Check Checklist

Use this checklist before running the application:

- [ ] Virtual environment activated (`.venv`)
- [ ] All packages installed (`pip list`)
- [ ] MongoDB running (check Windows Services)
- [ ] `.env` file exists with `GROQ_API_KEY`
- [ ] Port 5000 available (not in use)
- [ ] Static files present in `static/` folder
- [ ] No Python processes stuck (check Task Manager)
- [ ] Internet connection active (for Groq API)

---

## 🚀 Quick Start Commands

### Normal Startup:
```powershell
cd D:\Hackathon
.\.venv\Scripts\Activate.ps1
python app.py
```

### Fresh Installation:
```powershell
cd D:\Hackathon
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### Troubleshooting Startup:
```powershell
# Stop all Python processes
Get-Process python* | Stop-Process -Force

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Verify packages
pip list | Select-String "langchain|groq|flask"

# Start fresh
python app.py
```

---

## 📞 Getting Help

### Check Logs:
- Flask terminal output (shows all requests & errors)
- Browser console (F12 → Console tab)
- MongoDB logs (if connection issues)

### Common Log Patterns:

**Success**:
```
Successfully connected to MongoDB
Running on http://127.0.0.1:5000
Debugger is active!
```

**Module Error**:
```
⚠️  Error initializing LLM: No module named 'xyz'
→ Install package in virtual environment
```

**API Error**:
```
401 Unauthorized
→ Check GROQ_API_KEY in .env
```

**Database Error**:
```
Failed to connect to MongoDB
→ Start MongoDB service
```

---

## ✅ Current System Status

As of November 4, 2025:

- **Flask Server**: ✅ Running on http://127.0.0.1:5000
- **MongoDB**: ✅ Connected successfully
- **Virtual Environment**: ✅ Activated with all packages
- **Groq API**: ✅ Configured with Llama 3.3 70B
- **langchain-groq**: ✅ v1.0.0 installed
- **groq**: ✅ v0.33.0 installed

**Status**: 🟢 **ALL SYSTEMS OPERATIONAL**

---

## 🎯 Next Steps

1. **Test AI Diagnosis**:
   - Visit: http://127.0.0.1:5000
   - Login: admin / admin123
   - Navigate to "🤖 AI Diagnosis"
   - Submit test patient data
   - Verify Groq AI response

2. **Monitor Performance**:
   - Check response times (should be 3-5 seconds)
   - Verify "Powered by Groq AI" branding
   - Ensure no errors in terminal

3. **Production Deployment** (Future):
   - Use Gunicorn/uWSGI instead of Flask dev server
   - Set up SSL certificate
   - Configure reverse proxy (nginx)
   - Set up proper logging
   - Implement rate limiting
   - Add monitoring (Sentry, New Relic)

---

**Last Updated**: November 4, 2025  
**System Version**: 2.1.1 - Groq AI Edition (Virtual Environment Fixed)
