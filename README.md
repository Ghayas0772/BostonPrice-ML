# Boston Housing Price Prediction

## 1. Problem Definition
The goal of this project is to predict Boston housing prices using machine learning models. 
Machine learning is suitable because the relationship between housing price and features such as crime rate, number of rooms, and accessibility is non-linear and complex.

## 2. Dataset
- **Dataset:** BostonHousing.csv  
- **Location:** `data/BostonHousing.csv` in this repository.  
- **Description:** Contains features such as ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, PTRATIO, CRIM, TAX, and LSTAT.

## 3. Data Exploration & Feature Engineering
- Cleaned the data by handling outliers and skewness.
- Applied log-transformations to CRIM, TAX, and LSTAT.
- Normalized features where necessary.
- Removed irrelevant features and performed feature selection.
- Split data into training, validation, and testing sets.
- Saved cleaned data as `data/BostonHousing_clean.csv`.

## 4. Model Training & Evaluation
- Trained three models:  
  1. Linear Regression  
  2. Support Vector Regression (SVR)  
  3. Random Forest Regressor  
- Evaluated using RMSE and R² metrics.
- Random Forest performed the best.
- Saved the trained model as `models/RandomForest_BostonHousing.joblib`.

## 5. Local Deployment (Flask)
- **Flask app:** `app.py`  
- **HTML template:** `templates/index.html`  
- Users can input feature values and get a predicted MEDV.  
- Run locally:  
  ```bash
  python app.py
