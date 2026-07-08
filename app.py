"""Streamlit dashboard for the credit scoring project.

Run from the project root:
    streamlit run app.py
"""

import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from predict import build_credit_input, predict_creditworthiness  # noqa: E402


st.set_page_config(
    page_title="CodeAlpha Credit Scoring Model",
    page_icon="ML",
    layout="wide",
)


def main() -> None:
    """Render the credit scoring app."""

    st.title("CodeAlpha Credit Scoring Model")
    st.caption("Predict applicant creditworthiness from financial history.")

    col_left, col_right = st.columns(2)

    with col_left:
        age = st.slider("Age", min_value=21, max_value=65, value=32)
        annual_income = st.number_input("Annual income", min_value=10000, value=72000, step=1000)
        employment_years = st.slider("Employment years", 0.0, 35.0, 7.0, 0.5)
        savings_balance = st.number_input("Savings balance", min_value=0, value=16500, step=500)
        existing_debt = st.number_input("Existing debt", min_value=0, value=18000, step=500)

    with col_right:
        requested_loan = st.number_input("Requested loan", min_value=1000, value=22000, step=500)
        credit_history_years = st.slider("Credit history years", 0.0, 40.0, 9.0, 0.5)
        missed_payments_12m = st.slider("Missed payments in last 12 months", 0, 12, 0)
        credit_utilization = st.slider("Credit utilization", 0.0, 1.0, 0.31, 0.01)
        previous_defaults = st.selectbox(
            "Previous defaults",
            options=[0, 1],
            format_func=lambda value: "Yes" if value else "No",
        )

    if st.button("Predict Creditworthiness", type="primary"):
        model_input = build_credit_input(
            age=age,
            annual_income=float(annual_income),
            employment_years=float(employment_years),
            savings_balance=float(savings_balance),
            existing_debt=float(existing_debt),
            requested_loan=float(requested_loan),
            credit_history_years=float(credit_history_years),
            missed_payments_12m=int(missed_payments_12m),
            credit_utilization=float(credit_utilization),
            previous_defaults=int(previous_defaults),
        )
        result = predict_creditworthiness(model_input)

        st.metric("Prediction", result["label"])
        st.progress(result["probability"])
        st.write(f"Creditworthy probability: **{result['probability']:.2%}**")

        with st.expander("View engineered model input"):
            st.dataframe(model_input, use_container_width=True)


if __name__ == "__main__":
    main()
