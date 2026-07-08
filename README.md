# CodeAlpha Credit Scoring Model

This is a separate CodeAlpha Machine Learning internship project for **Task 1: Credit Scoring Model**.

The project predicts whether an applicant is likely creditworthy based on financial-history features.

## Open In VS Code

Open this folder in VS Code:

```text
CodeAlpha_Credit_Scoring_Model
```

## Run Commands

Run these commands in the VS Code terminal from inside the project folder.

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate virtual environment

For Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

For Command Prompt:

```bash
.\.venv\Scripts\activate.bat
```

### 3. Install libraries

```bash
pip install -r requirements.txt
```

### 4. Train the model

```bash
python src/train_model.py
```

### 5. Run demo prediction

```bash
python run_demo.py
```

### 6. Run dashboard

```bash
streamlit run app.py
```

## Project Outputs

After training, these files are created:

- `data/credit_scoring_synthetic.csv`
- `models/credit_scoring_model.joblib`
- `reports/credit_scoring_metrics.txt`
- `reports/credit_confusion_matrix.png`
- `reports/credit_feature_importance.csv`

## GitHub Repository Name

Use this repository name:

```text
CodeAlpha_Credit_Scoring_Model
```
