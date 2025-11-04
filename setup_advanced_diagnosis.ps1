# Advanced AI Diagnosis Setup Script
# This script helps you configure API keys for advanced diagnosis features

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  🤖 Advanced AI Diagnosis - Setup Wizard" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "This wizard will help you set up API keys for advanced AI-powered diagnosis." -ForegroundColor Yellow
Write-Host ""

# Function to test Google API key
function Test-GoogleAPIKey {
    param($apiKey)
    try {
        $body = @{
            contents = @(
                @{
                    parts = @(
                        @{ text = "Hello" }
                    )
                }
            )
        } | ConvertTo-Json -Depth 10
        
        $response = Invoke-RestMethod -Uri "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=$apiKey" `
            -Method Post -ContentType "application/json" -Body $body -ErrorAction Stop
        return $true
    }
    catch {
        return $false
    }
}

# Main menu
Write-Host "Choose your AI provider:" -ForegroundColor Green
Write-Host "1. Google Gemini (FREE - Recommended)" -ForegroundColor White
Write-Host "2. OpenAI GPT-3.5 (PAID)" -ForegroundColor White
Write-Host "3. Skip setup" -ForegroundColor Gray
Write-Host ""

$choice = Read-Host "Enter your choice (1-3)"

if ($choice -eq "1") {
    # Google Gemini setup
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host "  Setting up Google Gemini (FREE)" -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
    
    Write-Host "Steps to get your FREE Google Gemini API key:" -ForegroundColor Yellow
    Write-Host "1. Visit: https://makersuite.google.com/app/apikey" -ForegroundColor White
    Write-Host "2. Sign in with your Google account" -ForegroundColor White
    Write-Host "3. Click 'Create API Key'" -ForegroundColor White
    Write-Host "4. Copy the API key" -ForegroundColor White
    Write-Host ""
    
    $openBrowser = Read-Host "Would you like to open the Google AI Studio in your browser? (Y/N)"
    if ($openBrowser -eq "Y" -or $openBrowser -eq "y") {
        Start-Process "https://makersuite.google.com/app/apikey"
        Write-Host "Browser opened. Please get your API key and return here." -ForegroundColor Green
    }
    
    Write-Host ""
    $apiKey = Read-Host "Paste your Google Gemini API key here"
    
    if ($apiKey) {
        Write-Host ""
        Write-Host "Testing API key..." -ForegroundColor Yellow
        
        if (Test-GoogleAPIKey $apiKey) {
            Write-Host "✅ API key is valid!" -ForegroundColor Green
            
            # Set environment variable for current session
            $env:GOOGLE_API_KEY = $apiKey
            Write-Host "✅ Environment variable set for current session" -ForegroundColor Green
            
            # Ask to set permanently
            Write-Host ""
            $setPermanent = Read-Host "Would you like to set this permanently? (Y/N)"
            
            if ($setPermanent -eq "Y" -or $setPermanent -eq "y") {
                [System.Environment]::SetEnvironmentVariable("GOOGLE_API_KEY", $apiKey, "User")
                Write-Host "✅ Environment variable set permanently!" -ForegroundColor Green
                Write-Host ""
                Write-Host "Note: You may need to restart your terminal/IDE for the change to take effect." -ForegroundColor Yellow
            }
        }
        else {
            Write-Host "❌ API key test failed. Please check your key and try again." -ForegroundColor Red
            Write-Host "   Make sure you copied the complete key." -ForegroundColor Yellow
        }
    }
}
elseif ($choice -eq "2") {
    # OpenAI setup
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host "  Setting up OpenAI GPT-3.5 (PAID)" -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
    
    Write-Host "Steps to get your OpenAI API key:" -ForegroundColor Yellow
    Write-Host "1. Visit: https://platform.openai.com/api-keys" -ForegroundColor White
    Write-Host "2. Sign in or create an account" -ForegroundColor White
    Write-Host "3. Add payment method (credit card required)" -ForegroundColor White
    Write-Host "4. Create a new API key" -ForegroundColor White
    Write-Host "5. Copy the API key" -ForegroundColor White
    Write-Host ""
    Write-Host "💰 Pricing: ~$0.002 per 1K tokens (~$0.01-0.05 per diagnosis)" -ForegroundColor Yellow
    Write-Host ""
    
    $openBrowser = Read-Host "Would you like to open the OpenAI Platform in your browser? (Y/N)"
    if ($openBrowser -eq "Y" -or $openBrowser -eq "y") {
        Start-Process "https://platform.openai.com/api-keys"
        Write-Host "Browser opened. Please get your API key and return here." -ForegroundColor Green
    }
    
    Write-Host ""
    $apiKey = Read-Host "Paste your OpenAI API key here"
    
    if ($apiKey) {
        # Set environment variable for current session
        $env:OPENAI_API_KEY = $apiKey
        Write-Host "✅ Environment variable set for current session" -ForegroundColor Green
        
        # Ask to set permanently
        Write-Host ""
        $setPermanent = Read-Host "Would you like to set this permanently? (Y/N)"
        
        if ($setPermanent -eq "Y" -or $setPermanent -eq "y") {
            [System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", $apiKey, "User")
            Write-Host "✅ Environment variable set permanently!" -ForegroundColor Green
            Write-Host ""
            Write-Host "Note: You may need to restart your terminal/IDE for the change to take effect." -ForegroundColor Yellow
        }
    }
}
else {
    Write-Host ""
    Write-Host "Setup skipped. You can run this script again anytime." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Green
Write-Host "1. Run: python app.py" -ForegroundColor White
Write-Host "2. Visit: http://127.0.0.1:5000/advanced_diagnosis" -ForegroundColor White
Write-Host "3. Start using AI-powered diagnosis!" -ForegroundColor White
Write-Host ""
Write-Host "📚 For more information, read: ADVANCED_DIAGNOSIS_GUIDE.md" -ForegroundColor Cyan
Write-Host ""

$startApp = Read-Host "Would you like to start the Flask application now? (Y/N)"
if ($startApp -eq "Y" -or $startApp -eq "y") {
    Write-Host ""
    Write-Host "Starting Flask application..." -ForegroundColor Green
    python app.py
}
