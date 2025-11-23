from flask import Flask, render_template, request
from joblib import load
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained RandomForest model
model = load('model/RandomForest_BostonHousing.joblib')

# Feature order for model
features = ['ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','PTRATIO','CRIM_log','TAX_log','LSTAT_log']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect raw input values from form
        ZN = float(request.form['ZN'])
        INDUS = float(request.form['INDUS'])
        CHAS = float(request.form['CHAS'])
        NOX = float(request.form['NOX'])
        RM = float(request.form['RM'])
        AGE = float(request.form['AGE'])
        DIS = float(request.form['DIS'])
        RAD = float(request.form['RAD'])
        PTRATIO = float(request.form['PTRATIO'])
        CRIM = float(request.form['CRIM'])
        TAX = float(request.form['TAX'])
        LSTAT = float(request.form['LSTAT'])

        # Create dataframe for model
        input_df = pd.DataFrame([[
            ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, PTRATIO,
            np.log(CRIM + 1),  # log transform
            np.log(TAX + 1),   # log transform
            np.log(LSTAT + 1)  # log transform
        ]], columns=features)

        # Predict MEDV
        prediction = model.predict(input_df)[0]
        prediction = round(prediction, 2)

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
