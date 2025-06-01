import os

import joblib
import streamlit as st
import numpy as np
import pickle

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Load model
working_dir = os.path.dirname(os.path.abspath(__file__))

#model = pickle.load(open("C:/Users/Ashu/Desktop/Multiple Disease Prediction System/Models/heart_disease_model.pkl", "rb"))
#model = joblib.load(open('C:/Users/Ashu/Desktop/Multiple Disease Prediction System/Models/heart_model.sav', 'rb'))
model = joblib.load(open('Models/heart_model.sav', 'rb'))
# Title
st.title("❤️ Heart Disease Prediction")

st.markdown("Enter the following details to check your heart disease risk.")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120)
gender = st.radio("Gender", ["Male", "Female"])
sex = 1 if gender == "Male" else 0

cp = st.selectbox("Chest Pain Type (cp)", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
cp_map = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
cp_val = cp_map[cp]

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
fbs_val = 1 if fbs == "Yes" else 0

restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
ecg_map = {"Normal": 0, "ST-T Wave Abnormality": 1, "Left Ventricular Hypertrophy": 2}
restecg_val = ecg_map[restecg]

thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220)
exang = st.radio("Exercise-Induced Angina?", ["Yes", "No"])
exang_val = 1 if exang == "Yes" else 0

oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=6.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
slope_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
slope_val = slope_map[slope]

ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])
thal_map = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}
thal_val = thal_map[thal]

# Prediction
if st.button("Predict Heart Disease"):
    input_data = np.array([[age, sex, cp_val, trestbps, chol, fbs_val, restecg_val, thalach,
                            exang_val, oldpeak, slope_val, ca, thal_val]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High risk of Heart Disease detected.")
    else:
        st.success("✅ No significant risk of Heart Disease detected.")
