# 🤖 Advanced AI-Powered Diagnosis System

## Overview

The Advanced Diagnosis feature enhances the Automated Diagnostic System with **LangChain integration**, **PubMed research access**, and **AI-powered differential diagnosis** using Large Language Models (LLMs).

## 🌟 Features

### 1. **AI-Powered Differential Diagnosis**
- Uses LangChain with Google Gemini (free) or OpenAI GPT-3.5 (paid)
- Provides detailed differential diagnosis with reasoning
- Recommends additional tests and warning signs
- Offers lifestyle and treatment recommendations

### 2. **PubMed Research Integration**
- Searches latest medical research articles from PubMed database
- Displays relevant scientific papers with citations
- Provides evidence-based medical information
- Direct links to full articles on PubMed

### 3. **Medical Web Search**
- Real-time search using DuckDuckGo
- Gathers information from trusted medical sources
- Wikipedia medical summaries for quick reference

### 4. **Comprehensive Reporting**
- Combines ML model predictions with AI analysis
- Multiple data sources in one report
- Patient vitals tracking and symptom analysis
- Downloadable and printable reports

## 📋 Prerequisites

### Required Python Packages
All packages are already installed:
```bash
langchain
langchain-community
langchain-openai
langchain-google-genai
wikipedia-api
requests
beautifulsoup4
duckduckgo-search
```

### API Keys (Choose One)

#### Option 1: Google Gemini (FREE - Recommended)
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

#### Option 2: OpenAI (PAID)
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account and add payment method
3. Create a new API key
4. Copy your API key

## ⚙️ Configuration

### Setting Up API Keys

#### Windows (PowerShell)
```powershell
# For Google Gemini (Free)
$env:GOOGLE_API_KEY="your_api_key_here"

# For OpenAI (Paid)
$env:OPENAI_API_KEY="your_api_key_here"
```

#### Windows (Command Prompt)
```cmd
# For Google Gemini (Free)
set GOOGLE_API_KEY=your_api_key_here

# For OpenAI (Paid)
set OPENAI_API_KEY=your_api_key_here
```

#### Linux/Mac
```bash
# For Google Gemini (Free)
export GOOGLE_API_KEY="your_api_key_here"

# For OpenAI (Paid)
export OPENAI_API_KEY="your_api_key_here"
```

#### Permanent Setup (Recommended)

**Windows:**
1. Search for "Environment Variables" in Start Menu
2. Click "Edit system environment variables"
3. Click "Environment Variables" button
4. Under "User variables", click "New"
5. Variable name: `GOOGLE_API_KEY` or `OPENAI_API_KEY`
6. Variable value: Your API key
7. Click OK

**Linux/Mac:**
Add to `~/.bashrc` or `~/.zshrc`:
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

Then run:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

## 🚀 Usage

### 1. Start the Application
```bash
python app.py
```

### 2. Access Advanced Diagnosis
Navigate to: http://127.0.0.1:5000/advanced_diagnosis

Or click the "🤖 Advanced AI Diagnosis" button on the home page.

### 3. Select AI Provider
Choose between:
- **Google Gemini** (Free) - Recommended for most users
- **OpenAI GPT-3.5** (Paid) - Premium option

### 4. Enter Patient Information
- Patient Name
- Age, Gender
- Blood Pressure (mmHg)
- Glucose Level (mg/dL)
- Heart Rate (bpm)
- Symptoms (comma-separated)

**Example Symptoms:**
```
persistent headache, nausea, sensitivity to light, dizziness
```

### 5. Review Comprehensive Report
The system will provide:
- ✅ ML Model Prediction (Random Forest)
- ✅ AI Differential Diagnosis
- ✅ PubMed Research Articles
- ✅ Wikipedia Medical Summary
- ✅ Web Search Results
- ✅ Recommended Tests
- ✅ Warning Signs
- ✅ Treatment Recommendations

## 📊 How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    Patient Input                            │
│  (Age, Gender, Vitals, Symptoms)                           │
└────────────────────────┬────────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                  │
        ▼                                  ▼
┌───────────────────┐          ┌──────────────────────┐
│   ML Model        │          │   LangChain AI       │
│   (Random Forest) │          │   (Gemini/GPT)       │
│   Prediction      │          │   Analysis           │
└────────┬──────────┘          └──────────┬───────────┘
         │                                 │
         │                    ┌────────────┴────────────┐
         │                    │                         │
         │                    ▼                         ▼
         │          ┌─────────────────┐      ┌──────────────────┐
         │          │  PubMed API     │      │  Web Search      │
         │          │  (Research)     │      │  (DuckDuckGo)    │
         │          └────────┬────────┘      └─────────┬────────┘
         │                   │                         │
         └───────────────────┴─────────────────────────┘
                             │
                             ▼
                 ┌───────────────────────────┐
                 │  Comprehensive Report     │
                 │  - ML Prediction          │
                 │  - AI Differential Dx     │
                 │  - Research Articles      │
                 │  - Medical Sources        │
                 │  - Recommendations        │
                 └───────────────────────────┘
```

## 🔧 Technical Architecture

### Core Components

#### 1. **utils/langchain_diagnosis.py**
Main module containing:
- `AdvancedDiagnosisSystem` class
- LLM initialization (Google Gemini / OpenAI)
- PubMed API integration
- Wikipedia search
- Medical web search
- Differential diagnosis generation

#### 2. **Flask Routes**

**`/advanced_diagnosis`** (GET)
- Renders the advanced diagnosis form
- Requires authentication

**`/advanced_predict`** (POST)
- Processes patient data
- Runs ML model prediction
- Gets AI analysis from LangChain
- Searches medical databases
- Returns comprehensive report

**`/search_condition`** (POST)
- API endpoint for searching specific conditions
- Returns medical information in JSON format

### Data Flow

1. **User Input** → Patient information form
2. **ML Prediction** → Random Forest model analyzes vitals
3. **LangChain Analysis** → LLM generates differential diagnosis
4. **PubMed Search** → Fetches research articles via NCBI API
5. **Web Search** → Gathers additional medical information
6. **Report Generation** → Combines all sources
7. **Database Storage** → Saves to MongoDB
8. **Display** → Renders comprehensive report

## 📁 File Structure

```
d:\Hackathon\
├── app.py                              # Added advanced routes
├── utils/
│   ├── langchain_diagnosis.py          # NEW: LangChain integration
│   ├── predict.py                      # Existing ML prediction
│   └── db_connection.py                # MongoDB connection
├── templates/
│   ├── advanced_diagnosis.html         # NEW: Advanced form
│   ├── advanced_result.html            # NEW: Results page
│   ├── index.html                      # Updated with AI button
│   └── ...
└── ADVANCED_DIAGNOSIS_GUIDE.md         # This file
```

## 🎯 API Reference

### PubMed API
- **Endpoint:** `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`
- **Database:** PubMed (biomedical literature)
- **Free:** Yes, no API key required
- **Rate Limit:** 3 requests/second (respects rate limits)

### Google Gemini API
- **Model:** `gemini-pro`
- **Cost:** FREE (with rate limits)
- **Temperature:** 0.3 (for medical accuracy)
- **Best For:** Most users

### OpenAI API
- **Model:** `gpt-3.5-turbo`
- **Cost:** ~$0.002/1K tokens
- **Temperature:** 0.3 (for medical accuracy)
- **Best For:** Premium features

## 💡 Tips for Best Results

### 1. Symptom Entry
Be specific and detailed:
- ❌ Bad: "pain"
- ✅ Good: "sharp chest pain, radiating to left arm, worsens with exertion"

### 2. Multiple Symptoms
Enter multiple symptoms separated by commas:
```
persistent headache, nausea, sensitivity to light, dizziness, visual disturbances
```

### 3. Accurate Vitals
Ensure blood pressure, glucose, and heart rate are current measurements.

### 4. Choose Right Provider
- **Google Gemini:** Free, good for general use
- **OpenAI GPT-3.5:** Paid, potentially more detailed

## ⚠️ Troubleshooting

### Issue: "API Key Required" Message

**Solution:**
1. Ensure environment variable is set correctly
2. Restart the Flask application after setting the variable
3. Verify API key is valid by testing it directly

**Test Google API Key:**
```bash
curl "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=YOUR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Hello"}]}]}'
```

### Issue: PubMed Not Returning Results

**Possible Causes:**
- Network connectivity issues
- PubMed API temporarily down
- Condition name too generic or misspelled

**Solution:**
- Check internet connection
- Try more specific medical terms
- Wait a moment and try again

### Issue: Slow Response Time

**Causes:**
- LLM API calls take 2-5 seconds
- PubMed searches add 1-2 seconds
- Web searches add 1-2 seconds

**Expected Time:** 5-10 seconds total

**Solution:**
This is normal. The system processes multiple data sources for comprehensive results.

### Issue: Import Errors

**Error:**
```
ModuleNotFoundError: No module named 'langchain'
```

**Solution:**
```bash
pip install langchain langchain-community langchain-openai langchain-google-genai wikipedia-api requests beautifulsoup4 duckduckgo-search
```

## 🔒 Security & Privacy

### Data Handling
- Patient data is sent to AI providers (Google/OpenAI)
- Encrypted in transit via HTTPS
- Not permanently stored by AI providers (per their policies)
- Stored locally in MongoDB

### HIPAA Compliance
⚠️ **Important:** This system is for educational purposes only. For production use:
1. Use HIPAA-compliant hosting
2. Implement proper encryption
3. Add audit logging
4. Sign Business Associate Agreements (BAAs) with AI providers
5. Conduct security assessments

### API Key Security
- Never commit API keys to version control
- Use environment variables only
- Rotate keys regularly
- Monitor usage for anomalies

## 📈 Future Enhancements

### Planned Features
- [ ] Image analysis for medical reports
- [ ] Drug interaction checking
- [ ] Treatment plan generation
- [ ] Multi-language support
- [ ] Voice input for symptoms
- [ ] Integration with EHR systems
- [ ] Clinical decision support tools
- [ ] Real-time symptom checker
- [ ] Telemedicine integration

## 📚 Medical Disclaimer

**⚠️ CRITICAL NOTICE:**

This AI-assisted diagnostic tool is designed for **EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY**. It is **NOT** a substitute for professional medical advice, diagnosis, or treatment.

**You should always:**
- Consult qualified healthcare professionals for medical advice
- Seek immediate medical attention for emergencies
- Never disregard professional medical advice
- Never delay seeking medical treatment based on AI analysis
- Verify all information with licensed medical practitioners

**The developers, contributors, and AI providers:**
- Make no warranties about accuracy or completeness
- Are not responsible for any decisions made based on this tool
- Do not establish a doctor-patient relationship
- Cannot guarantee the correctness of any diagnosis or recommendation

**In case of medical emergency, call your local emergency number immediately.**

## 🤝 Support & Contribution

### Getting Help
- Check this guide thoroughly
- Review error messages carefully
- Test with different symptoms/conditions
- Verify API keys are set correctly

### Contributing
Improvements welcome:
- Better prompts for medical accuracy
- Additional medical data sources
- Enhanced UI/UX
- Performance optimizations
- Security enhancements

## 📞 Resources

### Official Documentation
- [LangChain Docs](https://python.langchain.com/)
- [Google AI Studio](https://ai.google.dev/)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [PubMed E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/)

### Medical Databases
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/) - Biomedical literature
- [MedlinePlus](https://medlineplus.gov/) - Consumer health info
- [WHO](https://www.who.int/) - World Health Organization
- [CDC](https://www.cdc.gov/) - Centers for Disease Control

### Learning Resources
- [LangChain Tutorial](https://python.langchain.com/docs/get_started)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Medical AI Ethics](https://www.who.int/publications/i/item/9789240029200)

---

## 🎉 Quick Start Checklist

- [ ] Install all required packages ✅ (Already done)
- [ ] Get Google Gemini API key (free)
- [ ] Set environment variable `GOOGLE_API_KEY`
- [ ] Restart Flask application
- [ ] Navigate to http://127.0.0.1:5000/advanced_diagnosis
- [ ] Enter patient information
- [ ] Review comprehensive AI-powered diagnosis
- [ ] Save report for records

**Enjoy enhanced medical insights with AI-powered diagnosis!** 🚀

---

**Version:** 1.0.0  
**Last Updated:** November 4, 2025  
**Author:** Automated Diagnostic System Team
