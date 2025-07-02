from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)
model = joblib.load('model/house_price_model.pkl')

# USD to INR conversion rate
USD_TO_INR = float(os.getenv("USD_TO_INR", 85.33))

# Proper Indian number formatting using Python
def format_in_indian_currency(amount):
    s = str(int(amount))
    if len(s) <= 3:
        return '₹' + s
    else:
        last3 = s[-3:]
        rest = s[:-3]
        new_rest = ""
        while len(rest) > 2:
            new_rest = ',' + rest[-2:] + new_rest
            rest = rest[:-2]
        new_rest = rest + new_rest
        return '₹' + new_rest + ',' + last3

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sqft = float(request.form['sqft'])
    bed = int(request.form['bedrooms'])
    bath = float(request.form['bathrooms'])

    input_features = np.array([[sqft, bed, bath]])
    prediction_usd = model.predict(input_features)[0]
    prediction_inr = prediction_usd * USD_TO_INR

    formatted_price = format_in_indian_currency(prediction_inr)

    return render_template('index.html',
        prediction_text=f"Predicted House Price: {formatted_price} (approx.)",
        sqft=int(sqft),
        bedrooms=bed,
        bathrooms=bath
    )

if __name__ == '__main__':
    app.run(debug=True)
