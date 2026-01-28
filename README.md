# Bangalore House Price Prediction 🏠

A complete end-to-end Machine Learning project that predicts real estate prices in Bangalore. This project features a **Linear Regression** model, a **FastAPI** backend for serving predictions, and a **Streamlit** web interface for user interaction.

---

## 📂 Project Structure

The repository is organized to maintain a clear separation between the Machine Learning workflow, the backend API, and the frontend client.

```text
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
├── requirements.txt            # Project Dependencies
└── README.md                   # Documentation ```
Module Breakdown:
client/: Built with Streamlit. It communicates with the FastAPI server to fetch location names and display the predicted price based on user inputs (Square Feet, BHK, Bathrooms).

server/: The engine of the project. It uses FastAPI to serve the model. The artifacts folder contains the saved state of the model and the column mapping required for one-hot encoding.

model/: Contains the raw data and the Jupyter Notebook documenting the data cleaning, feature engineering, and model training process.

Machine Learning: Scikit-learn, Pandas, NumPy

API Framework: FastAPI

Web Frontend: Streamlit

Server/Deployment:   python

🚀 Installation & Setup
1. Clone the repository
```Bash

git clone [https://github.com/Suraj8Sharma/house-price-prediction.git](https://github.com/Suraj8Sharma/house-price-prediction.git)
cd house-price-prediction ```
