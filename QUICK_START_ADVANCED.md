# 🚀 Advanced AI Diagnosis - Quick Start

## ⚡ 3-Minute Setup

### Step 1: Get FREE API Key (2 minutes)
1. Open: https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key

### Step 2: Set Environment Variable (1 minute)

**PowerShell (Windows):**
```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

**Or run the setup script:**
```powershell
.\setup_advanced_diagnosis.ps1
```

### Step 3: Start Using
```bash
python app.py
```
Visit: http://127.0.0.1:5000/advanced_diagnosis

---

## 🎯 What You Get

| Feature | Basic Diagnosis | Advanced AI Diagnosis |
|---------|----------------|----------------------|
| ML Prediction | ✅ | ✅ |
| Differential Diagnosis | ❌ | ✅ |
| PubMed Research | ❌ | ✅ |
| AI Analysis | ❌ | ✅ |
| Medical Sources | ❌ | ✅ |
| Treatment Recommendations | ❌ | ✅ |
| Warning Signs | ❌ | ✅ |

---

## 💡 Example Usage

### Input:
```
Name: John Doe
Age: 45
Gender: Male
BP: 155 mmHg
Glucose: 180 mg/dL
Heart Rate: 88 bpm
Symptoms: frequent urination, excessive thirst, fatigue, blurred vision
```

### Output:
- ✅ ML Prediction: Diabetes
- ✅ AI Differential Diagnosis: Type 2 Diabetes Mellitus (most likely), Hyperglycemia, Metabolic Syndrome
- ✅ PubMed Articles: 3 recent research papers
- ✅ Recommended Tests: HbA1c, Fasting Glucose, Lipid Panel
- ✅ Warning Signs: Diabetic ketoacidosis symptoms to watch for
- ✅ Recommendations: Diet modifications, exercise, monitor glucose

---

## 🆓 Free vs Paid

### Google Gemini (FREE)
- ✅ No credit card required
- ✅ Good quality results
- ✅ 60 requests/minute
- ✅ Recommended for most users

### OpenAI GPT-3.5 (PAID)
- 💰 ~$0.01-0.05 per diagnosis
- ✅ Potentially more detailed
- ✅ Faster responses
- 💳 Credit card required

---

## ⚠️ Troubleshooting

### "API Key Required" message?
1. Check environment variable: `echo $env:GOOGLE_API_KEY`
2. Restart Flask app after setting key
3. Verify key is correct

### Slow response?
- Normal! Takes 5-10 seconds
- Processing multiple data sources

### Import errors?
```bash
pip install langchain langchain-community langchain-google-genai
```

---

## 📞 Quick Links

- 🔑 Get API Key: https://makersuite.google.com/app/apikey
- 📚 Full Guide: ADVANCED_DIAGNOSIS_GUIDE.md
- 🌐 Home: http://127.0.0.1:5000
- 🤖 Advanced Diagnosis: http://127.0.0.1:5000/advanced_diagnosis

---

## ⚡ Pro Tips

1. **Be Specific with Symptoms**
   - ❌ Bad: "pain"
   - ✅ Good: "sharp chest pain radiating to left arm"

2. **Use Multiple Symptoms**
   ```
   headache, nausea, sensitivity to light, dizziness
   ```

3. **Accurate Vitals Matter**
   Use recent measurements for best results

4. **Review All Sources**
   Check ML prediction, AI analysis, AND research articles

---

**Ready to go?** Run: `python app.py` 🚀

**Need help?** Check `ADVANCED_DIAGNOSIS_GUIDE.md`
