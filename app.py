from flask import Flask, render_template, request
import joblib
import numpy as np
import locale

app = Flask(__name__)
model = joblib.load('model/house_price_model.pkl')

# Set Indian locale for proper comma formatting
locale.setlocale(locale.LC_ALL, 'en_IN')

# Approximate USD to INR rate
USD_TO_INR = 85.33

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

    # Convert to INR
    prediction_inr = prediction_usd * USD_TO_INR
    prediction_inr_formatted = locale.format_string("₹%d", prediction_inr, grouping=True)

    return render_template('index.html',
        prediction_text=f"Predicted House Price: {prediction_inr_formatted} (approx.)",
        sqft=int(sqft),
        bedrooms=bed,
        bathrooms=bath
    )

if __name__ == '__main__':
    app.run(debug=True)
