# Agro-Sense-AI-Crop-Intelligence

 Agro-Sense AI: End-to-End Crop Intelligence Ecosystem

Project ID: P139 | Domain: Precision Agriculture, Remote Sensing, Generative AI

(Replace the link above with the actual path to your dashboard screenshot after uploading it)

**Overview**

Agro-Sense AI is a "Digital Twin" system for agriculture that moves farming from reactive monitoring to proactive intelligence. It fuses Sentinel-2 satellite imagery with simulated IoT sensor data to detect invisible crop stress, predict harvest yields months in advance, and provide actionable, AI-driven advisory services to farmers.

**Key Features
**
Data Fusion Architecture: Combines macro-scale Satellite data (NDVI, EVI) with micro-scale IoT data (Soil Moisture, Leaf Wetness) to eliminate blind spots during cloudy weather.

High-Fidelity Modeling: Trained on 10+ years of ground-truth historical farm records (369 crop cycles).

Deep Learning Engine: Utilizes an LSTM (Long Short-Term Memory) model achieving 95% accuracy in predicting detailed crop growth stages.

Yield Forecasting: Implements an XGBoost Regressor ($R^2=0.31$) to statistically link canopy health to final harvest weight.

AI Agronomist Agent: Integrates Google Gemini Pro (LLM) to translate complex data analytics into simple, human-readable advice (e.g., "Stop irrigation due to fungal risk").

Interactive Dashboard: A full-stack Streamlit web application featuring dynamic Earth Engine maps and real-time analytics.

**Tech Stack
**
Languages: Python (Pandas, NumPy)

ML/DL: TensorFlow (Keras), Scikit-Learn (Random Forest, SMOTE), XGBoost

Geospatial: Google Earth Engine (GEE) API, Geemap, GeoPy

Generative AI: Google Gemini Pro API (google-generativeai)

Web Framework: Streamlit, Plotly, PyNgrok

**Setup Instructions**

⚠️ **Security Notice**: This project requires Google API keys. Please follow the security best practices outlined in [SECURITY.md](SECURITY.md).

1. **Clone the repository**
```bash
git clone https://github.com/YasinIIT/Agro-Sense-AI-Crop-Intelligence.git
cd Agro-Sense-AI-Crop-Intelligence
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
pip install python-dotenv
```

3. **Configure API Keys (Important!)**

   a. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

   b. Get your API keys:
   - **Google Gemini API**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **Google Earth Engine**: Follow [GEE Python Installation Guide](https://developers.google.com/earth-engine/guides/python_install)

   c. Edit `.env` and add your keys:
   ```
   GOOGLE_API_KEY=your_actual_gemini_api_key_here
   ```

   d. **NEVER commit the `.env` file to git!** It's already in `.gitignore`.

4. **Authenticate with Google Earth Engine**
```bash
earthengine authenticate
```

5. **Run the notebooks**
   - Start with `01_Model_Training_Pipeline.ipynb` for model training
   - Then use `02_Dashboard_and_App.ipynb` for the dashboard

**Project Structure**

01_Model_Training_Pipeline.ipynb: The "Brain" of the system. Contains:

Data preprocessing pipeline for 9 Punjab fields and historical records.

SMOTE implementation for handling class imbalance.

Training logic for Random Forest, LSTM, and XGBoost models.

02_Dashboard_and_App.ipynb: The "Product". Contains:

IoT Data Simulation Engine.

Streamlit Dashboard code.

Gemini AI Agent integration logic.

**Methodology & Results**

Phase 1: Real-Time Monitoring

We processed 5 years of Sentinel-2 data for 9 fields. Using SMOTE to balance the dataset, we trained a Random Forest classifier that achieved 81% accuracy in detecting basic growth stages.

Phase 2: The "High-Fidelity" Pivot

To predict yield, we digitized 10 years of historical farm logs. This "Gold Standard" dataset allowed us to train an LSTM model that improved stage prediction accuracy to 95%, capturing the sequential nature of crop growth.

Phase 3: The Intelligence Layer

We integrated a Large Language Model (LLM) to act as a reasoning engine. By feeding model predictions (e.g., "Flowering Stage") and weather data (e.g., "Rainy") into the LLM, the system generates specific warnings about risks like fungal diseases, bridging the gap between data science and agronomy.

**Future Scope**

IoT Hardware Integration: Replace simulated data with physical LoRaWAN soil sensors.

Computer Vision: Implement "Doctor Leaf" module for pest detection via smartphone camera.

Automated Alerts: WhatsApp/SMS integration for daily crop status updates.

**Security**

🔒 This project uses API keys that must be kept secure. Please read our [Security Policy](SECURITY.md) for:
- How to properly configure API keys
- What to do if you accidentally expose credentials
- Best practices for keeping your keys secure

**Important**: Never commit API keys, credentials, or `.env` files to git!

Developed by Khilji Mohammed Yasin & Shaik Mohammad Thousif as part of the Open Ended Lab Project (OELP).
