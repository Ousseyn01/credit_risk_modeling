import streamlit as st
import pandas as pd
import joblib

model = joblib.load('xgboost_credit_model.pkl')
encoder = {col : joblib.load(f"{col}_encode.pkl") for col in ["Sex", "Housing", "Saving accounts", "Checking account"]}

st.title("Credit Risk Prediction app")
st.write("Enter applicant information to predict if the credit risk is good or bad.")
#st.write("Sex encoder classes:", encoder["Sex"].classes_)

age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", ["male", "female"])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ["own", "rent", "free"])
saving_accounts = st.selectbox("Saving accounts", ["little", "moderate", "rich", "quite rich"])
checking_account = st.selectbox("Checking account", ["little", "moderate", "rich"])
credit_amount = st.number_input("Credit Amount", min_value=100, value=1000)
duration = st.number_input("Duration (months)", min_value=1, value=12)

sex_map = {"male": 1, "female": 0}
housing_map = {"own": 2, "rent": 1, "free": 0}
saving_map = {"little": 0, "moderate": 1, "rich": 2, "quite rich": 3}
checking_map = {"little": 0, "moderate": 1, "rich": 2}

input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [sex_map[sex]],
    "Job": [job],
    "Housing": [housing_map[housing]],
    "Saving accounts": [saving_map[saving_accounts]],
    "Checking account": [checking_map[checking_account]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

if st.button("Predict Risk"):
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)
    if prediction == 1:
        st.success("The predicted credit risk is : **GOOD**.")
        st.info(f"Probability that customer will repay: {probability[0][1]*100:.2f}%")
    else:
        st.error("The predicted credit risk is : **BAD**.")
        st.info(f"Probability that customer will repay: {probability[0][1]*100:.2f}%")

