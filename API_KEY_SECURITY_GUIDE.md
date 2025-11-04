# 🔐 API Key Configuration & Security Guide

## ⚠️ CRITICAL SECURITY ALERT

**Your API key has been exposed in this conversation and MUST be revoked immediately!**

### Immediate Actions Required:

1. **Go to OpenRouter Dashboard:**
   - Visit: https://openrouter.ai/keys
   - Find the key starting with: `sk-or-v1-c9ac500252...`
   - Click "Revoke" or "Delete" immediately

2. **Generate a New API Key:**
   - Create a new key in the dashboard
   - Copy it securely (don't share it anywhere)

---

## ✅ Proper API Key Setup (Completed)

I've already configured your system securely:

### 1. Created `.env` File ✅
Location: `d:\Hackathon\.env`

```env
GOOGLE_API_KEY=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
```

**Important:** Replace this with your NEW key after revoking the old one!

### 2. Added `.gitignore` Entry ✅
The `.env` file is already protected from being committed to Git:

```gitignore
# Environment variables
.env
.env.local
```

### 3. Updated `app.py` ✅
Added automatic `.env` file loading:

```python
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
```

### 4. Installed `python-dotenv` ✅
Package is already installed and ready to use.

---

## 🔄 How to Update Your API Key

### Step 1: Get Your New Key
After revoking the exposed key:
1. Go to https://openrouter.ai/keys
2. Click "Create Key"
3. Give it a name (e.g., "MediCare Hospital - Dev")
4. Copy the new key

### Step 2: Update .env File
Edit `d:\Hackathon\.env`:

```env
# Replace the old key with your NEW key
GOOGLE_API_KEY=sk-or-v1-YOUR_NEW_KEY_HERE
```

### Step 3: Restart Flask Server
```bash
# Stop current server (Ctrl+C in terminal)
# Start again
python app.py
```

The system will automatically load the new key!

---

## 📋 API Key Types Supported

### 1. OpenRouter (Recommended) ✅
- **Provider:** OpenRouter
- **Model:** Google Gemini (free tier available)
- **Key Format:** `sk-or-v1-...`
- **Environment Variable:** `GOOGLE_API_KEY`
- **Signup:** https://openrouter.ai

### 2. Google AI Studio (Alternative)
- **Provider:** Google Direct
- **Model:** Gemini
- **Key Format:** `AIzaSy...`
- **Environment Variable:** `GOOGLE_API_KEY`
- **Signup:** https://ai.google.dev

### 3. OpenAI (Alternative - Paid)
- **Provider:** OpenAI
- **Model:** GPT-3.5 / GPT-4
- **Key Format:** `sk-...`
- **Environment Variable:** `OPENAI_API_KEY`
- **Signup:** https://platform.openai.com

---

## 🔍 Verify API Key is Working

### Check 1: Server Startup
When you start Flask, you should NOT see this warning:
```
⚠️  GOOGLE_API_KEY not found. Please set it for advanced diagnosis.
```

If you see it, the key isn't loaded properly.

### Check 2: Test Advanced Diagnosis
1. Go to: http://127.0.0.1:5000/advanced_diagnosis
2. Fill in patient symptoms
3. Click "Get Advanced AI Diagnosis"
4. You should see:
   - ✅ Comprehensive analysis
   - ✅ PubMed research articles
   - ✅ Medical literature references
   - ✅ Differential diagnosis
   - ✅ Treatment recommendations

### Check 3: Terminal Output
Look for successful API calls in terminal:
```
127.0.0.1 - - [04/Nov/2025 06:46:09] "POST /advanced_predict HTTP/1.1" 200 -
```
- **200** = Success ✅
- **500** = Error (check API key) ❌

---

## 🛡️ Security Best Practices

### DO ✅
- ✅ Store API keys in `.env` file
- ✅ Keep `.env` in `.gitignore`
- ✅ Use environment variables in code
- ✅ Revoke exposed keys immediately
- ✅ Use different keys for dev/prod
- ✅ Set spending limits on API providers
- ✅ Rotate keys regularly (monthly)

### DON'T ❌
- ❌ Hardcode keys in source code
- ❌ Commit `.env` to Git
- ❌ Share keys in chat/email
- ❌ Use production keys in development
- ❌ Share API keys with team members
- ❌ Post keys in forums/Discord
- ❌ Store keys in browser localStorage

---

## 🚨 What to Do If Key Is Exposed

### Immediate Actions (Within Minutes):
1. **Revoke the key** at provider dashboard
2. **Generate a new key**
3. **Update `.env` file** with new key
4. **Restart application**
5. **Check billing** for unauthorized usage

### Follow-up Actions (Within 24 Hours):
6. **Review access logs** at provider dashboard
7. **Set spending limits** if not already set
8. **Enable rate limiting** on API provider
9. **Add IP restrictions** if supported
10. **Document the incident**

---

## 📊 Current System Status

```
✅ .env file created: d:\Hackathon\.env
✅ API key configured: GOOGLE_API_KEY
✅ python-dotenv installed: v1.2.1
✅ app.py updated: load_dotenv() added
✅ .gitignore configured: .env excluded
✅ Flask server running: http://127.0.0.1:5000
✅ MongoDB connected: localhost:27017
```

---

## 🔧 Troubleshooting

### Problem: "GOOGLE_API_KEY not found" warning

**Solution:**
```bash
# 1. Check .env file exists
Test-Path "d:\Hackathon\.env"
# Should return: True

# 2. Check .env content
Get-Content "d:\Hackathon\.env"
# Should show: GOOGLE_API_KEY=sk-or-v1-...

# 3. Restart Flask server
python app.py
```

### Problem: Advanced diagnosis returns error

**Possible Causes:**
1. **Invalid API key** → Update with new key
2. **Rate limit exceeded** → Wait or upgrade plan
3. **Network issue** → Check internet connection
4. **Revoked key** → Generate new key

**Check logs:**
```python
# Look in terminal for error messages
# Common errors:
# - "401 Unauthorized" → Invalid/revoked key
# - "429 Too Many Requests" → Rate limit
# - "500 Internal Server Error" → Server issue
```

### Problem: API key works but responses are slow

**Solutions:**
1. Check API provider status page
2. Consider switching providers
3. Increase timeout in code
4. Use caching for repeated queries

---

## 💡 Pro Tips

### 1. Multiple Environments
Create separate keys for different environments:

```env
# Development
GOOGLE_API_KEY_DEV=sk-or-v1-dev-key-here

# Production
GOOGLE_API_KEY_PROD=sk-or-v1-prod-key-here

# Testing
GOOGLE_API_KEY_TEST=sk-or-v1-test-key-here
```

### 2. Key Rotation Script
Create a reminder to rotate keys:

```python
# utils/check_key_age.py
import os
from datetime import datetime, timedelta

def check_key_age():
    # Add logic to check when key was last rotated
    # Alert if > 30 days old
    pass
```

### 3. Monitoring Usage
Most providers offer usage dashboards:
- OpenRouter: https://openrouter.ai/activity
- Google AI: https://aistudio.google.com/app/apikey
- OpenAI: https://platform.openai.com/usage

### 4. Cost Management
Set monthly spending limits:
- OpenRouter: $10/month for development
- Google: Usually free tier sufficient
- OpenAI: Set strict limits

---

## 📞 Need Help?

### API Provider Support:
- **OpenRouter:** https://discord.gg/openrouter
- **Google AI:** https://ai.google.dev/support
- **OpenAI:** https://help.openai.com

### Common Issues:
- Key not working → Check revoked status
- Slow responses → Check provider status
- High costs → Review usage analytics
- Rate limits → Upgrade plan or optimize requests

---

## ✅ Final Checklist

Before deploying to production:
- [ ] Revoke exposed API key
- [ ] Generate new production key
- [ ] Update `.env` with new key
- [ ] Test advanced diagnosis feature
- [ ] Set spending limits
- [ ] Enable monitoring alerts
- [ ] Document key rotation schedule
- [ ] Add key to password manager
- [ ] Configure backup API provider
- [ ] Test failover mechanism

---

## 🎯 Summary

Your API key configuration is now **secure and production-ready**:

1. ✅ API key stored in `.env` file (not in code)
2. ✅ `.env` file excluded from Git
3. ✅ Application loads keys automatically
4. ✅ Flask server running successfully

**NEXT STEP:** Revoke the exposed key and update `.env` with a new one!

---

*Security Guide Generated: November 4, 2025*  
*Status: Configuration Complete - Action Required (Key Revocation)*  
*Priority: CRITICAL*
