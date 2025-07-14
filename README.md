# Smart House Price Predictor

A machine learning-powered web application to predict house prices using the Ames Housing dataset. Users enter property details to get instant price predictions. The app uses a Linear Regression model and is deployed with a modern, responsive frontend.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Modeling Approach](#modeling-approach)
- [Web Application](#web-application)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [File & Feature Descriptions](#file--feature-descriptions)
- [Limitations](#limitations)
- [Future Scope](#future-scope)
- [Contact](#contact)

---

## Overview

**Smart House Price Predictor** is an internship project focused on building a predictive web app using machine learning. The model estimates house prices based on user-input property features such as square footage, bedrooms, and bathrooms.

---

## Features

- **Instant House Price Prediction:** Users enter property details and receive estimates in both USD and INR.
- **Responsive UI:** Modern layout with left-side input form and right-side dynamic prediction history.
- **Temporary History:** Predictions stored in browser localStorage and cleared on page reload.
- **Modular Design:** Easy to extend with new models or features.
- **Real-time currency conversion** (USD to INR).
- **Simple, interpretable model:** Linear Regression for transparency.

---

## Tech Stack

- **Backend:** Python, Flask, Scikit-learn
- **Frontend:** HTML5, CSS3, JavaScript ES6
- **Data Handling:** Pandas
- **Visualization:** Matplotlib, Seaborn

---

## Dataset

- **Source:** Kaggle Ames Housing dataset
- Contains detailed records of real estate sales in Ames, Iowa.
- Only the most relevant features are used for this prototype, keeping the model simple and explainable.

---

## Modeling Approach

- **Algorithm:** Linear Regression
- **Features Used:** Square footage, bedrooms, bathrooms, and derived features like total bathrooms.
- **Metrics:** 
    - Mean Squared Error (MSE)
    - Root Mean Squared Error (RMSE)
    - R² Score: ~0.6579

Example (from notebook):
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

---

## Web Application

- **Deployment:** Flask web app
- **Workflow:**
    1. User fills in property details.
    2. Server predicts price and returns formatted output.
    3. Prediction history displayed, cleared on reload.

- **Frontend Features:**
    - Responsive layout (form + history)
    - UX enhancements with styled components
    - Temporary history in browser localStorage

- **Limitations:**
    - Location-specific data and market fluctuations not considered
    - Prediction history is not saved permanently
    - Feature set is limited for simplicity

---

## Setup & Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/manoj-2305/SCT_ML_1.git
    cd SCT_ML_1
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If requirements.txt is missing, install manually: Flask, scikit-learn, pandas, numpy, matplotlib, seaborn, joblib)*

3. **Prepare environment:**
    - Ensure model file exists at `model/house_price_model.pkl`
    - Set USD to INR conversion rate via environment variable if needed:
      ```
      export USD_TO_INR=85.33
      ```

4. **Run the app:**
    ```bash
    python app.py
    ```
    The application will run locally at `http://127.0.0.1:5000/`.

---

## Usage

1. Open the web app in your browser.
2. Enter property details (square footage, bedrooms, bathrooms, etc.).
3. Get instant price predictions.
4. View temporary history (cleared on refresh).

**For Jupyter Notebook:**
- Explore `House_Price_Prediction.ipynb` for model training, evaluation, and submission file creation.

---

## File & Feature Descriptions

- `app.py`: Flask server handling requests and predictions.
- `model/house_price_model.pkl`: Pre-trained Linear Regression model.
- `model/data_description.txt`: Detailed documentation of dataset features (e.g., MSZoning, LotArea, HouseStyle, OverallQual, etc.).
- `House_Price_Prediction.ipynb`: Model training, validation, and inference notebook.
- `templates/index.html`: Main HTML template with project overview, dataset info, modeling approach, and contact.
- `static/style.css`: Responsive and modern UI styling.
- `static/script.js`: Handles frontend history logic and navigation.

**Feature Glossary:**  
See `model/data_description.txt` for full details of all dataset features (zoning, house style, quality ratings, etc.).

---

## Limitations

- Market fluctuations and location-specific factors not modeled.
- Prediction history is not persisted beyond session.
- Feature set is minimal for prototype simplicity.

---

## Future Scope

- Add location data and connect to real estate APIs.
- Enable user accounts and save permanent history.
- Integrate advanced ML algorithms (Random Forest, XGBoost).
- Cloud deployment (Heroku, AWS, Streamlit Cloud).

---

## Contact

**Phone:** +91 9876543210  
**Email:** info@smartprice.in  
**Location:** Bangalore, India

---

© 2025 SmartPrice | All Rights Reserved
