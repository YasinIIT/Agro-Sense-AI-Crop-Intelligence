"""
Configuration loader for Agro-Sense AI
This file demonstrates the secure way to load API keys from environment variables.

Usage in notebooks or scripts:
    from config_loader import load_google_api_key
    
    api_key = load_google_api_key()
    
    # Configure your API
    import google.generativeai as genai
    genai.configure(api_key=api_key)
"""

import os
from dotenv import load_dotenv
import sys


def load_google_api_key():
    """
    Load Google Gemini API key from environment variables.
    
    Returns:
        str: The API key
        
    Raises:
        ValueError: If the API key is not found
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the API key
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        error_msg = (
            "Google API key not found!\n"
            "Please follow these steps:\n"
            "1. Copy .env.example to .env\n"
            "2. Add your Google Gemini API key to .env\n"
            "3. Get your API key from: https://makersuite.google.com/app/apikey\n"
            "4. NEVER commit the .env file to git!"
        )
        raise ValueError(error_msg)
    
    return api_key


def load_earth_engine_project():
    """
    Load Google Earth Engine project ID from environment variables.
    
    Returns:
        str: The project ID or None if not set
    """
    load_dotenv()
    return os.getenv('EE_PROJECT_ID')


if __name__ == "__main__":
    # Test the configuration
    try:
        api_key = load_google_api_key()
        print("✓ Google API key loaded successfully")
        print(f"  Key prefix: {api_key[:10]}...")
        
        project_id = load_earth_engine_project()
        if project_id:
            print(f"✓ Earth Engine project ID: {project_id}")
        else:
            print("ℹ Earth Engine project ID not set (optional)")
            
    except ValueError as e:
        print(f"✗ Configuration error:\n{e}")
        sys.exit(1)
