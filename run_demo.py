"""Quick command-line demo for the credit scoring model.

Run from the project root:
    python run_demo.py
"""

from src.predict import build_credit_input, predict_creditworthiness


def main() -> None:
    """Create one sample applicant and print the model prediction."""

    sample_applicant = build_credit_input(
        age=32,
        annual_income=72000,
        employment_years=7.0,
        savings_balance=16500,
        existing_debt=18000,
        requested_loan=22000,
        credit_history_years=9.0,
        missed_payments_12m=0,
        credit_utilization=0.31,
        previous_defaults=0,
    )
    result = predict_creditworthiness(sample_applicant)

    print("Credit Scoring Result")
    print(f"Prediction: {result['label']}")
    print(f"Creditworthy probability: {result['probability']:.2%}")


if __name__ == "__main__":
    main()
