# Quick Start Guide: API Key Setup

This guide helps you quickly set up the required API keys for Agro-Sense AI.

## Prerequisites

- Google Account
- Python 3.8 or higher installed

## Step-by-Step Setup

### 1. Get Your Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. **Copy the key immediately** (you won't be able to see it again)

### 2. Set Up Google Earth Engine (Optional but Recommended)

1. Visit [Google Earth Engine](https://earthengine.google.com/)
2. Sign up for access (usually approved within 1-2 days)
3. Once approved, install the Earth Engine Python API:
   ```bash
   pip install earthengine-api
   ```
4. Authenticate:
   ```bash
   earthengine authenticate
   ```

### 3. Configure Your Environment

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file** and add your API key:
   ```bash
   # Use your preferred text editor
   nano .env
   # or
   vim .env
   # or open in your IDE
   ```

3. **Replace the placeholder** with your actual key:
   ```
   GOOGLE_API_KEY=AIzaSy...your_actual_key_here
   ```

4. **Save and close** the file

### 4. Verify Your Setup

Run the configuration tester:
```bash
python config_loader.py
```

You should see:
```
✓ Google API key loaded successfully
  Key prefix: AIzaSy...
```

### 5. Add Restrictions to Your API Key (Important!)

For security, add restrictions in [Google Cloud Console](https://console.cloud.google.com/apis/credentials):

1. Click on your API key
2. Under "API restrictions":
   - Select "Restrict key"
   - Choose "Generative Language API"
3. Under "Application restrictions" (optional):
   - Set IP address restrictions if you know your server IP
4. Click "Save"

## Common Issues

### Issue: "Google API key not found!"

**Solution:** Make sure:
- You created the `.env` file (not `.env.example`)
- The file is in the project root directory
- The key name is exactly `GOOGLE_API_KEY=`
- There are no spaces around the `=` sign

### Issue: "Permission denied" or "Invalid API key"

**Solution:**
- Verify the API key was copied correctly (no extra spaces)
- Check that the API is enabled in Google Cloud Console
- Make sure you're using a Gemini API key (not other Google API keys)

### Issue: ".env file not loading in Jupyter notebooks"

**Solution:** Add this at the top of your notebook:
```python
import os
from dotenv import load_dotenv

# Explicitly load the .env file
load_dotenv()

# Verify it loaded
print("API Key loaded:", "GOOGLE_API_KEY" in os.environ)
```

## Security Reminders

- ✅ **DO**: Keep your `.env` file local and never commit it
- ✅ **DO**: Add API restrictions in Google Cloud Console
- ✅ **DO**: Regenerate keys if they're accidentally exposed
- ❌ **DON'T**: Share your API keys in screenshots or documentation
- ❌ **DON'T**: Commit `.env` files to git
- ❌ **DON'T**: Hard-code API keys in notebooks or scripts

## Need Help?

- Read the full [Security Policy](SECURITY.md)
- Check the [README](README.md) for more details
- Report issues on GitHub (but never include your actual API keys!)

## What's Next?

Once your API keys are configured:

1. Install dependencies: `pip install -r requirements.txt`
2. Open `01_Model_Training_Pipeline.ipynb` to train models
3. Open `02_Dashboard_and_App.ipynb` to run the dashboard

Happy coding! 🌾🚜
