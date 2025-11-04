"""
Test script to verify Groq API is working
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("Testing Groq API Configuration")
print("=" * 60)

# Check if API key is loaded
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    print(f"✅ GROQ_API_KEY found: {api_key[:20]}...{api_key[-10:]}")
else:
    print("❌ GROQ_API_KEY not found in environment")
    exit(1)

# Try to import langchain_groq
try:
    from langchain_groq import ChatGroq
    print("✅ langchain_groq imported successfully")
except ImportError as e:
    print(f"❌ Failed to import langchain_groq: {e}")
    exit(1)

# Try to initialize the model
try:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=api_key,
        temperature=0.3,
        max_tokens=100
    )
    print("✅ ChatGroq model initialized successfully")
except Exception as e:
    print(f"❌ Failed to initialize ChatGroq: {e}")
    exit(1)

# Try to make a simple API call
try:
    print("\n" + "=" * 60)
    print("Testing API call...")
    print("=" * 60)
    
    response = llm.invoke("Say 'Hello, Groq is working!' in one sentence.")
    print(f"\n✅ API call successful!")
    print(f"Response: {response.content}")
    
except Exception as e:
    print(f"❌ API call failed: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n" + "=" * 60)
print("🎉 All tests passed! Groq API is fully operational")
print("=" * 60)
