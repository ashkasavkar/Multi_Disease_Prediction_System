import streamlit as st
import numpy as np
import pickle
from pages import Diabetes, Heart

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Load the model and label encoder
model, le = pickle.load(open('C:/Users/Ashu/Desktop/Multiple Disease Prediction System/Models/disease_model.pkl','rb'))


# Define symptoms
symptoms = ['Fever', 'Cough', 'Fatigue', 'Headache', 'Sore Throat', 'Loss of Smell',
            'Chest Pain', 'Vomiting', 'Diarrhea', 'Dizziness', 'Sweating',
            'Weight Loss', 'Blurred Vision', 'Joint Pain']

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "main"

if "predicted_disease" not in st.session_state:
    st.session_state.predicted_disease = None
    
# Main page: select general symptoms and predict disease
def general_symptom_page():
    st.title("🩺 Multi-Disease Prediction System")
    st.markdown("### Select the symptoms you are experiencing:")

    selected_symptoms = st.multiselect("Select Symptoms", symptoms)

    if st.button("Predict Disease"):
        if not selected_symptoms:
            st.warning("Please select at least one symptom.")
            return

        input_vector = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
        pred_encoded = model.predict([input_vector])[0]
        prediction = le.inverse_transform([pred_encoded])[0]

        st.session_state.predicted_disease = prediction

        # Navigate to disease-specific page or result page
        if prediction == "Diabetes":
            st.session_state.page = "Diabetes"
        elif prediction == "Heart Disease":
            st.session_state.page = "Heart"
        #elif prediction == "Typhoid":
        #    st.session_state.page = "typhoid"
        #elif prediction == "COVID-19":
        #    st.session_state.page = "covid19"
        else:
            st.session_state.page = "result"

# Result page for diseases without detailed forms
def result_page():
    st.title("🧾 Prediction Result")
    st.success(f"🎯 Predicted Disease: **{st.session_state.predicted_disease}**")

    if st.button("Back to Home"):
        st.session_state.page = "main"
        st.session_state.predicted_disease = None

# Main routing logic
def main():
    if st.session_state.page == "main":
        general_symptom_page()

    elif st.session_state.page == "Diabetes":
        Diabetes.run() 

    elif st.session_state.page == "Heart":
        Heart.run()
    elif st.session_state.page == "result":
        result_page()
    #elif st.session_state.page == "Typhoid":
    #    typhoid_page.run()

    #elif st.session_state.page == "covid19":
    #    covid19_page.run()


if __name__ == "__main__":
    main()