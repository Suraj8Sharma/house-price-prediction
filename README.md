# 🏠 Bangalore House Price Prediction
### *An End-to-End Machine Learning Web Application*

This repository contains a full-stack machine learning project that predicts real estate prices in Bangalore, India. It includes the entire pipeline: from data cleaning and feature engineering to model deployment using FastAPI and a Streamlit frontend.

---

## 🏗️ Project Structure

```plaintext
house-price-prediction/
├── client/                 # Frontend Streamlit Web App
│   └── app.py              # Main UI script
├── server/                 # Backend FastAPI Server
│   ├── main.py             # API Routes & Server Config
│   ├── util.py             # Prediction logic & Artifact loading
│   └── artifacts/          # Trained Model & Feature Columns
│       ├── banglore_home_price_model.pickle
│       └── columns.json
├── model/                  # Data Science & Training
│   ├── banglore_house_prices.csv
│   └── house_price_prediction.ipynb
└── requirements.txt        # Project Dependencies ```
#🚀 Features
### *Data Cleaning: Handled missing values, outliers, and dimensionality reduction.
---


### *Feature Engineering: Location-based one-hot encoding and square-ft processing.
---

### *Model Training: Built using Scikit-Learn (Linear Regression, Lasso, Decision Trees).
---
###Deployment: - Backend: FastAPI for high-performance API serving.
---
###Frontend: Streamlit for a clean, interactive user interface.
---
#🛠️ Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/Suraj8Sharma/house-price-prediction.git
cd house-price-prediction
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Run the Backend (FastAPI)
Bash
cd server
python main.py
The server will typically start on http://127.0.0.1:8000

4. Run the Frontend (Streamlit)
Open a new terminal and run:

Bash
cd client
streamlit run app.py
📊 Dataset
The dataset used is the Bangalore Home Prices dataset from Kaggle. It contains features like location, total square footage, number of bathrooms, and BHK.

🧠 Machine Learning Workflow
Data Discovery: Exploring the raw CSV data.

Preprocessing: Removing unnecessary features and handling null values.

Outlier Removal: Using business logic (price per sqft, bhk vs sqft) to filter noise.

Model Selection: Using GridSearchCV to find the best performing model.

Export: Saving the model as a .pickle file and column names as a .json for production use.

