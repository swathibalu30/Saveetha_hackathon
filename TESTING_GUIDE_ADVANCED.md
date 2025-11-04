# 🧪 Testing Guide - Advanced AI Diagnosis

## ✅ Issue Fixed!

The Advanced AI Diagnosis feature wasn't showing results due to a template syntax error. **It's now fixed!**

---

## 🚀 Quick Test (5 Minutes)

### Step 1: Verify Server is Running

Check your terminal - you should see:
```
Successfully connected to MongoDB
 * Running on http://127.0.0.1:5000
 * Debugger is active!
```

✅ **Server Status**: READY

---

### Step 2: Open the Application

1. **Open Browser**: Chrome, Firefox, or Edge
2. **Navigate to**: http://127.0.0.1:5000
3. **Bookmark it**: You'll use this often!

---

### Step 3: Login

**Credentials**:
- Username: `admin`
- Password: `admin123`

**What to see**:
- Login successful
- Redirected to Dashboard
- Welcome message displayed

---

### Step 4: Access Advanced AI Diagnosis

**Method 1**: Click top navigation
- Look for: "🤖 AI Diagnosis" or "Advanced AI Diagnosis"
- Click it

**Method 2**: Direct URL
- Navigate to: http://127.0.0.1:5000/advanced_diagnosis

**What to see**:
- Purple gradient header
- "Advanced AI-Powered Diagnosis" title
- Form with patient information fields

---

### Step 5: Fill the Form

**Use this test data**:

| Field | Value |
|-------|-------|
| **Patient Name** | John Doe |
| **Age** | 45 |
| **Gender** | Male |
| **Blood Pressure** | 140 |
| **Glucose Level** | 180 |
| **Heart Rate** | 85 |
| **Symptoms** | chest pain, fatigue, shortness of breath |

**Tips**:
- ✅ Symptoms can be comma-separated
- ✅ Age must be 0-150
- ✅ BP must be 50-250
- ✅ Glucose must be 50-500
- ✅ Heart Rate must be 40-200

---

### Step 6: Submit & Wait

1. **Click**: "Get Advanced AI Analysis" button
2. **Wait**: 3-5 seconds (Groq is fast!)
3. **Watch terminal**: Look for any errors

**What to see**:
- Loading indicator (if implemented)
- Page should NOT redirect back to form
- Should navigate to results page

---

### Step 7: Verify Results

**Expected on Results Page**:

1. **Header Section** ✅
   - Patient name displayed
   - Age, gender shown
   - Vitals displayed (BP, Glucose, HR)

2. **ML Prediction** ✅
   - Disease prediction from Random Forest model
   - Displayed in colored box

3. **AI Analysis Section** ✅
   - Badge: "✅ Powered by Groq AI - Lightning-fast health analysis with Llama 3.3 70B"
   - Comprehensive analysis text
   - Sections: Differential Diagnosis, Primary Diagnosis, Reasoning, etc.

4. **Medical Sources** ✅
   - **PubMed Articles**: 3 research articles with titles and links
   - **Wikipedia Summary**: Medical condition information
   - **Web Search Results**: Additional medical information

5. **Disclaimer** ✅
   - Educational purposes notice
   - Consult healthcare professional message

---

## 🔍 What Success Looks Like

### Visual Checklist:

```
✅ Results page loads (URL: /advanced_result)
✅ Patient information displayed correctly
✅ ML diagnosis shown in purple gradient box
✅ "Powered by Groq AI" badge visible
✅ AI analysis text is comprehensive (500+ words)
✅ PubMed articles section populated (3 articles)
✅ Wikipedia summary displayed
✅ No error messages
✅ Terminal shows HTTP 200 OK for /advanced_predict
✅ Response time < 10 seconds
```

---

## ❌ What Failure Looks Like

### Issue 1: Redirect Back to Form

**Symptom**: After submit, you're back at the form page

**What to check**:
1. Look for red error message at top of page
2. Check terminal for error traceback
3. Verify you filled all required fields

**Common causes**:
- Missing required field (name, age, etc.)
- Invalid data (age > 150, BP < 50, etc.)
- API key issue (check .env file)
- Template syntax error (already fixed)

### Issue 2: Blank Analysis

**Symptom**: Results page loads but AI analysis section is empty

**What to check**:
1. Terminal: Look for "⚠️ GROQ_API_KEY not found"
2. Check `.env` file has: `GROQ_API_KEY=gsk_...`
3. Verify langchain-groq is installed in venv

**Fix**:
```powershell
.\.venv\Scripts\Activate.ps1
pip install langchain-groq
```

### Issue 3: Slow Response (> 20 seconds)

**Symptom**: Page takes forever to load

**Possible causes**:
- Internet connection slow
- Groq API rate limit hit (30 req/min free tier)
- PubMed/Wikipedia timeout

**Fix**:
- Wait 1 minute and retry
- Check internet connection
- Verify Groq status: https://status.groq.com/

---

## 📊 Terminal Output to Watch For

### Success Pattern:
```
127.0.0.1 - - [04/Nov/2025 08:XX:XX] "GET /advanced_diagnosis HTTP/1.1" 200 -
127.0.0.1 - - [04/Nov/2025 08:XX:XX] "POST /advanced_predict HTTP/1.1" 200 -
127.0.0.1 - - [04/Nov/2025 08:XX:XX] "GET /advanced_result HTTP/1.1" 200 -
```

### Error Pattern:
```
127.0.0.1 - - [04/Nov/2025 08:XX:XX] "POST /advanced_predict HTTP/1.1" 302 -
❌ Error during advanced diagnosis: <error message>
📋 Full traceback:
...
```

---

## 🧪 Advanced Testing

### Test Case 1: Different Symptoms

**Input**:
- Symptoms: "headache, fever, cough"
- Expected: Different diagnosis and recommendations

### Test Case 2: Edge Values

**Input**:
- Age: 18 (young adult)
- BP: 120 (normal)
- Glucose: 90 (normal)
- HR: 70 (normal)
- Symptoms: "general checkup"
- Expected: Healthy analysis, preventive care advice

### Test Case 3: High-Risk Patient

**Input**:
- Age: 65
- BP: 160 (high)
- Glucose: 220 (high)
- HR: 95 (elevated)
- Symptoms: "chest pain, dizziness, nausea"
- Expected: Urgent warnings, cardiovascular concerns

---

## 📸 Screenshot Checklist

Take screenshots of these to confirm everything works:

1. [ ] Login page
2. [ ] Dashboard after login
3. [ ] Advanced Diagnosis form (filled)
4. [ ] Results page - full view
5. [ ] AI Analysis section (zoomed)
6. [ ] PubMed articles section
7. [ ] Terminal output showing HTTP 200

---

## 🔧 Quick Fixes

### If Form Won't Submit:

```javascript
// Open Browser Console (F12)
// Check for errors - should be none
```

### If API Key Error:

```powershell
# Verify .env file
Get-Content .env

# Should show:
# GROQ_API_KEY=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
```

### If Template Error:

```powershell
# Restart Flask server
Get-Process python* | Stop-Process -Force
.\.venv\Scripts\Activate.ps1
python app.py
```

---

## ✅ Test Complete Checklist

After successful test:

- [ ] Results page displayed
- [ ] Patient data correct
- [ ] ML diagnosis shown
- [ ] Groq AI badge visible
- [ ] AI analysis comprehensive
- [ ] PubMed articles loaded (3)
- [ ] Wikipedia summary present
- [ ] No errors in terminal
- [ ] Response time < 10 seconds
- [ ] Can navigate back and test again

---

## 🎉 Success Criteria

**Minimum passing grade**: 8/10 checks ✅

**Perfect score**: All 10 checks ✅

**If you got 10/10**: 🎉 **GROQ AI INTEGRATION FULLY OPERATIONAL!**

---

## 📞 Troubleshooting Resources

### Documentation:
1. `GROQ_AI_INTEGRATION.md` - Complete Groq setup guide
2. `TROUBLESHOOTING.md` - Common issues and solutions
3. `ADVANCED_DIAGNOSIS_FIX.md` - Recent fixes applied

### Test Scripts:
- `test_groq.py` - Verify Groq API independently

### Quick Commands:
```powershell
# Restart server
cd D:\Hackathon
.\.venv\Scripts\Activate.ps1
python app.py

# Test Groq API
.\.venv\Scripts\python.exe test_groq.py

# Check packages
pip list | Select-String "groq"
```

---

**Ready to test? Let's go! 🚀**

1. Server running? ✅
2. Browser open? ✅
3. Test data ready? ✅
4. **Click that submit button!** 👆

---

**Last Updated**: November 4, 2025  
**Test Version**: 1.0  
**Estimated Time**: 5 minutes  
**Difficulty**: Easy
