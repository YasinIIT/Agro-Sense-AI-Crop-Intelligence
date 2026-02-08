# Security Policy

## Reporting Security Issues

If you discover a security vulnerability in this project, please report it by:
- Opening a private security advisory on GitHub
- Emailing the maintainers directly

**Please do not report security vulnerabilities through public GitHub issues.**

## API Key Security

### Important: API Key Management

This project uses Google Cloud Platform APIs (Gemini Pro and Earth Engine). **NEVER** commit API keys directly into your code or Jupyter notebooks.

### ⚠️ Previous Security Incident

A Google API key was previously exposed in this repository. If you cloned or forked this repository before February 8, 2026, please:

1. **Regenerate any API keys** you may have used
2. **Check your Google Cloud Console** for unexpected usage
3. **Review billing alerts** for any unusual activity

### Best Practices for API Keys

#### 1. Use Environment Variables

Create a `.env` file (never commit this):
```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

In your Python code:
```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access API key
api_key = os.getenv('GOOGLE_API_KEY')
```

In Jupyter notebooks:
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

# Use the API key
import google.generativeai as genai
genai.configure(api_key=api_key)
```

#### 2. Add Restrictions to Your API Keys

In the [Google Cloud Console](https://console.cloud.google.com/apis/credentials):

- **Application restrictions**: Limit usage to specific IP addresses or HTTP referrers
- **API restrictions**: Restrict which APIs the key can access
- **Set usage quotas**: Limit daily usage to prevent abuse

#### 3. Use .gitignore

This repository includes a `.gitignore` file that prevents committing:
- `.env` files
- Any file containing `api_key`, `secrets`, or `credentials`
- Jupyter notebook checkpoints

#### 4. For Jupyter Notebooks

**Option A: Use environment variables (recommended)**
```python
import os
api_key = os.getenv('GOOGLE_API_KEY')
```

**Option B: Use a separate config file**
Create `config.py` (add to `.gitignore`):
```python
GOOGLE_API_KEY = "your_key_here"
```

Then import:
```python
from config import GOOGLE_API_KEY
```

**Option C: Input at runtime**
```python
import getpass
api_key = getpass.getpass('Enter your Google API key: ')
```

### What NOT to Do ❌

- ❌ Hard-code API keys in notebooks or Python files
- ❌ Commit `.env` files to git
- ❌ Share API keys in screenshots or documentation
- ❌ Use the same API key across multiple projects
- ❌ Ignore Google Cloud security alerts

### What to Do if You Accidentally Commit an API Key ✅

1. **Immediately regenerate the key** in Google Cloud Console
2. **Revoke the old key** to prevent further use
3. **Check for unusual activity** in your Google Cloud usage logs
4. **Update your local code** with the new key in `.env`
5. **Consider using git history rewriting** (contact maintainers for help)

### Installing Required Dependencies

To use environment variables with Python:
```bash
pip install python-dotenv
```

### Additional Security Resources

- [Google Cloud API Key Best Practices](https://cloud.google.com/docs/authentication/api-keys)
- [Handling Compromised Credentials](https://support.google.com/cloud/answer/6310037)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## Dependency Security

We recommend:
- Regularly updating dependencies
- Using tools like `pip-audit` or `safety` to check for vulnerabilities
- Reviewing dependency updates before merging

## Reporting Other Security Concerns

For questions about security practices in this project, please contact the maintainers.
