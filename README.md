🏠 Bangalore House Price Prediction
An End-to-End Machine Learning Web Application

🏗️ Project Structure
Plaintext

house-price-prediction/
├── client/                     # Frontend Streamlit Web App
│   └── app.py                  # Main UI script
├── server/                     # Backend FastAPI Server
│   ├── main.py                 # API Routes & Server Config
│   ├── util.py                 # Prediction logic & Artifact loading
│   └── artifacts/              # Model & Feature data
│       ├── banglore_home_price_model.pickle
│       └── columns.json
├── model/                      # Data Science & Training
│   ├── banglore_house_prices.csv
│   └── house_price_prediction.ipynb
└── requirements.txt            # Project Dependencies