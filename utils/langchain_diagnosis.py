"""
Advanced Diagnosis Module using LangChain
Integrates with online medical sources for evidence-based diagnosis
Supports Groq (fast & free), Google Gemini, and OpenAI
"""

import os
import requests
from typing import List, Dict, Optional
from datetime import datetime
from langchain_core.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
import json

# Note: Users need to set their API keys as environment variables
# For Groq: GROQ_API_KEY (Recommended - Fast & Free)
# For Google: GOOGLE_API_KEY
# For OpenAI: OPENAI_API_KEY


class AdvancedDiagnosisSystem:
    """
    Advanced diagnosis system using LangChain and online medical sources
    """
    
    def __init__(self, llm_provider="groq"):
        """
        Initialize the diagnosis system
        
        Args:
            llm_provider: "groq" (fast & free, recommended), "google" (free with Gemini), or "openai" (paid)
        """
        self.llm_provider = llm_provider
        self.llm = self._initialize_llm()
        self.search_tool = DuckDuckGoSearchRun()
        self.wikipedia = WikipediaAPIWrapper()
        
    def _initialize_llm(self):
        """Initialize the Language Model based on provider"""
        try:
            if self.llm_provider == "groq":
                from langchain_groq import ChatGroq
                api_key = os.getenv("GROQ_API_KEY")
                if not api_key:
                    print("⚠️  GROQ_API_KEY not found. Please set it for advanced diagnosis.")
                    return None
                return ChatGroq(
                    model="llama-3.3-70b-versatile",  # Fast and powerful model
                    groq_api_key=api_key,
                    temperature=0.3,
                    max_tokens=2048
                )
            elif self.llm_provider == "google":
                from langchain_google_genai import ChatGoogleGenerativeAI
                api_key = os.getenv("GOOGLE_API_KEY")
                if not api_key:
                    print("⚠️  GOOGLE_API_KEY not found. Please set it for advanced diagnosis.")
                    return None
                return ChatGoogleGenerativeAI(
                    model="gemini-pro",
                    google_api_key=api_key,
                    temperature=0.3
                )
            elif self.llm_provider == "openai":
                from langchain_openai import ChatOpenAI
                api_key = os.getenv("OPENAI_API_KEY")
                if not api_key:
                    print("⚠️  OPENAI_API_KEY not found. Please set it for advanced diagnosis.")
                    return None
                return ChatOpenAI(
                    model="gpt-3.5-turbo",
                    temperature=0.3,
                    openai_api_key=api_key
                )
        except Exception as e:
            print(f"⚠️  Error initializing LLM: {e}")
            return None
    
    def search_medical_info(self, query: str, num_results: int = 3) -> List[Dict]:
        """
        Search for medical information using DuckDuckGo
        
        Args:
            query: Medical query to search
            num_results: Number of results to return
            
        Returns:
            List of search results
        """
        try:
            search_query = f"medical condition {query} symptoms treatment"
            results = self.search_tool.run(search_query)
            return [{
                "source": "DuckDuckGo Medical Search",
                "content": results[:500],  # Limit content length
                "timestamp": datetime.now().isoformat()
            }]
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def get_wikipedia_summary(self, condition: str) -> Optional[Dict]:
        """
        Get Wikipedia summary for a medical condition
        
        Args:
            condition: Medical condition name
            
        Returns:
            Wikipedia summary
        """
        try:
            summary = self.wikipedia.run(f"{condition} medical condition")
            return {
                "source": "Wikipedia",
                "content": summary[:800],  # Limit content length
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Wikipedia error: {e}")
            return None
    
    def get_pubmed_articles(self, condition: str, max_results: int = 3) -> List[Dict]:
        """
        Search PubMed for medical articles (using free NCBI API)
        
        Args:
            condition: Medical condition to search
            max_results: Maximum number of articles
            
        Returns:
            List of PubMed articles
        """
        try:
            base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
            
            # Search for article IDs
            search_url = f"{base_url}esearch.fcgi"
            search_params = {
                "db": "pubmed",
                "term": f"{condition}[Title/Abstract]",
                "retmax": max_results,
                "retmode": "json"
            }
            
            response = requests.get(search_url, params=search_params, timeout=10)
            search_data = response.json()
            
            if "esearchresult" not in search_data or "idlist" not in search_data["esearchresult"]:
                return []
            
            article_ids = search_data["esearchresult"]["idlist"]
            
            if not article_ids:
                return []
            
            # Fetch article summaries
            summary_url = f"{base_url}esummary.fcgi"
            summary_params = {
                "db": "pubmed",
                "id": ",".join(article_ids),
                "retmode": "json"
            }
            
            response = requests.get(summary_url, params=summary_params, timeout=10)
            summary_data = response.json()
            
            articles = []
            if "result" in summary_data:
                for article_id in article_ids:
                    if article_id in summary_data["result"]:
                        article = summary_data["result"][article_id]
                        articles.append({
                            "source": "PubMed",
                            "title": article.get("title", ""),
                            "authors": ", ".join([author.get("name", "") for author in article.get("authors", [])[:3]]),
                            "journal": article.get("source", ""),
                            "pub_date": article.get("pubdate", ""),
                            "pmid": article_id,
                            "url": f"https://pubmed.ncbi.nlm.nih.gov/{article_id}/"
                        })
            
            return articles
            
        except Exception as e:
            print(f"PubMed error: {e}")
            return []
    
    def analyze_symptoms(self, symptoms: List[str], patient_data: Dict) -> Dict:
        """
        Analyze symptoms and provide differential diagnosis using LangChain
        
        Args:
            symptoms: List of symptoms
            patient_data: Patient information (age, gender, vitals)
            
        Returns:
            Analysis results with differential diagnoses
        """
        if not self.llm:
            return self._get_fallback_analysis(symptoms, patient_data)
        
        try:
            # Create prompt template for medical diagnosis
            diagnosis_prompt = PromptTemplate(
                input_variables=["symptoms", "age", "gender", "bp", "glucose", "heart_rate"],
                template="""You are an expert medical AI assistant. Based on the following patient information, provide a detailed medical analysis:

Patient Information:
- Age: {age} years
- Gender: {gender}
- Blood Pressure: {bp} mmHg
- Glucose Level: {glucose} mg/dL
- Heart Rate: {heart_rate} bpm
- Symptoms: {symptoms}

Please provide:
1. **Differential Diagnosis** (list 3-5 possible conditions in order of likelihood)
2. **Primary Diagnosis** (most likely condition)
3. **Reasoning** (why this is the most likely diagnosis)
4. **Recommended Tests** (what additional tests should be ordered)
5. **Warning Signs** (symptoms that require immediate medical attention)
6. **General Recommendations** (lifestyle changes, precautions)

Important: This is for educational purposes only. Always consult a qualified healthcare professional for medical advice.

Analysis:"""
            )
            
            # Use the new LangChain API (invoke instead of LLMChain)
            # Format the prompt with parameters
            formatted_prompt = diagnosis_prompt.format(
                symptoms=", ".join(symptoms),
                age=patient_data.get("age", "Unknown"),
                gender=patient_data.get("gender", "Unknown"),
                bp=patient_data.get("bp", "Unknown"),
                glucose=patient_data.get("glucose", "Unknown"),
                heart_rate=patient_data.get("heart_rate", "Unknown")
            )
            
            # Run the analysis using invoke
            result = self.llm.invoke(formatted_prompt)
            
            # Extract content from the result
            analysis_text = result.content if hasattr(result, 'content') else str(result)
            
            return {
                "success": True,
                "analysis": analysis_text,
                "timestamp": datetime.now().isoformat(),
                "provider": self.llm_provider
            }
            
        except Exception as e:
            print(f"LLM analysis error: {e}")
            return self._get_fallback_analysis(symptoms, patient_data)
    
    def _get_fallback_analysis(self, symptoms: List[str], patient_data: Dict) -> Dict:
        """Fallback analysis when LLM is not available"""
        return {
            "success": False,
            "analysis": """**API Key Required**

To use advanced AI-powered diagnosis, please set up an API key:

**Option 1: Google Gemini (FREE)**
1. Visit https://makersuite.google.com/app/apikey
2. Create a free API key
3. Set environment variable: GOOGLE_API_KEY=your_key_here

**Option 2: OpenAI (PAID)**
1. Visit https://platform.openai.com/api-keys
2. Create an API key
3. Set environment variable: OPENAI_API_KEY=your_key_here

**Current Basic Analysis:**
Based on the symptoms: {symptoms}
- Patient Age: {age}
- Blood Pressure: {bp} mmHg
- Glucose: {glucose} mg/dL
- Heart Rate: {heart_rate} bpm

Please configure an API key to get detailed AI-powered diagnosis with differential diagnosis, medical references, and treatment recommendations.
""".format(
                symptoms=", ".join(symptoms),
                age=patient_data.get("age", "Unknown"),
                bp=patient_data.get("bp", "Unknown"),
                glucose=patient_data.get("glucose", "Unknown"),
                heart_rate=patient_data.get("heart_rate", "Unknown")
            ),
            "timestamp": datetime.now().isoformat(),
            "provider": "fallback"
        }
    
    def get_comprehensive_diagnosis(self, symptoms: List[str], patient_data: Dict, 
                                   ml_prediction: str) -> Dict:
        """
        Get comprehensive diagnosis combining ML model, LangChain analysis, and online sources
        
        Args:
            symptoms: List of symptoms
            patient_data: Patient information
            ml_prediction: Prediction from the ML model
            
        Returns:
            Comprehensive diagnosis report
        """
        # Get AI analysis
        ai_analysis = self.analyze_symptoms(symptoms, patient_data)
        
        # Get medical information from online sources
        medical_info = self.search_medical_info(ml_prediction)
        wiki_info = self.get_wikipedia_summary(ml_prediction)
        pubmed_articles = self.get_pubmed_articles(ml_prediction)
        
        # Combine all information
        comprehensive_report = {
            "ml_prediction": ml_prediction,
            "ai_analysis": ai_analysis,
            "medical_sources": {
                "web_search": medical_info,
                "wikipedia": wiki_info,
                "pubmed_articles": pubmed_articles
            },
            "patient_summary": {
                "age": patient_data.get("age"),
                "gender": patient_data.get("gender"),
                "vitals": {
                    "blood_pressure": patient_data.get("bp"),
                    "glucose": patient_data.get("glucose"),
                    "heart_rate": patient_data.get("heart_rate")
                },
                "symptoms": symptoms
            },
            "timestamp": datetime.now().isoformat(),
            "disclaimer": "This is an AI-assisted analysis for educational purposes only. Always consult qualified healthcare professionals for medical advice and treatment."
        }
        
        return comprehensive_report


# Utility functions for easy integration

def get_advanced_diagnosis(symptoms: List[str], patient_data: Dict, 
                          ml_prediction: str, llm_provider: str = "google") -> Dict:
    """
    Main function to get advanced diagnosis
    
    Args:
        symptoms: List of patient symptoms
        patient_data: Dictionary with age, gender, bp, glucose, heart_rate
        ml_prediction: Prediction from the ML model
        llm_provider: "google" or "openai"
        
    Returns:
        Comprehensive diagnosis report
    """
    system = AdvancedDiagnosisSystem(llm_provider=llm_provider)
    return system.get_comprehensive_diagnosis(symptoms, patient_data, ml_prediction)


def search_medical_condition(condition: str) -> Dict:
    """
    Search for information about a medical condition
    
    Args:
        condition: Medical condition name
        
    Returns:
        Medical information from various sources
    """
    system = AdvancedDiagnosisSystem()
    
    return {
        "condition": condition,
        "web_search": system.search_medical_info(condition),
        "wikipedia": system.get_wikipedia_summary(condition),
        "pubmed_articles": system.get_pubmed_articles(condition),
        "timestamp": datetime.now().isoformat()
    }
