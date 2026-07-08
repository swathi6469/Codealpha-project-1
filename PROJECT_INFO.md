# CodeAlpha Credit Scoring Model

## Internship Task

**Task 1: Credit Scoring Model**

## Objective

Predict an individual's creditworthiness using financial-history data.

## Approach

This project trains a **Random Forest Classifier** on a realistic synthetic credit dataset. The dataset is generated locally because real credit data is sensitive and should not be shared publicly.

## Key Features

- Feature engineering from financial history.
- Uses income, debt, savings, loan amount, payment history, credit utilization, and previous defaults.
- Adds engineered features:
  - debt-to-income ratio
  - loan-to-income ratio
  - savings-to-loan ratio
  - stability index
- Evaluates the model using:
  - accuracy
  - precision
  - recall
  - F1-score
  - ROC-AUC
- Includes a Streamlit dashboard and command-line demo.

## Files Included

- `src/data_builder.py`: creates and loads the dataset.
- `src/train_model.py`: trains and evaluates the model.
- `src/predict.py`: loads the saved model and makes predictions.
- `app.py`: Streamlit app.
- `run_demo.py`: quick command-line test.
- `reports/`: model evaluation reports.
- `models/`: trained model file.

## Disclaimer

This project is for education and internship demonstration only. It must not be used for real credit approval decisions.
