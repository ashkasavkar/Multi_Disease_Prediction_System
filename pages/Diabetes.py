import streamlit as st
import numpy as np
import pickle

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Load the trained model
model = pickle.load(open("C:/Users/Ashu/Desktop/Multiple Disease Prediction System/Models/diabetes_gender_model.pkl", "rb"))

# Title
st.title("🩺 Diabetes Prediction System")

st.markdown("Provide the following health details to check your diabetes risk.")

# Gender selection
gender = st.radio("Gender", ["Female", "Male"])
gender_val = 0 if gender == "Female" else 1

# Pregnancies (only for females)
if gender == "Female":
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, step=1)
else:
    pregnancies = 0  # auto-set for males
    st.markdown("*Pregnancies not applicable for males (auto-set to 0).*")

# Other health inputs
glucose = st.number_input("Glucose Level", min_value=0, max_value=300)
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200)
skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900)
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=70.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5)
age = st.number_input("Age", min_value=1, max_value=120)

# Predict button
if st.button("Predict Diabetes"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age, gender_val]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ You are likely to have diabetes.")
    else:
        st.success("✅ You are unlikely to have diabetes.")
