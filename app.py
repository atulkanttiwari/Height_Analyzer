import streamlit as st
import pandas as pd
import pickle

st.title("Height Prediction App 📏")

# Load the pipeline
try:
    with open('height_predictor_pipeline.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please train the model and generate 'height_predictor_pipeline.pkl'.")
    st.stop()

# Inputs
weight = st.number_input("Enter Weight (kg)", min_value=1.0, max_value=200.0, value=75.0)
gender = st.selectbox("Select Gender", ["Male", "Female"])

if st.button("Predict Height"):
    # Convert gender to number
    gender_num = 1 if gender == "Male" else 0
    
    # Create a DataFrame for prediction (must match training column names)
    input_df = pd.DataFrame([[weight, gender_num]], columns=['Weight', 'Gender'])
    
    # Predict
    prediction = model.predict(input_df)[0]
    
    st.success(f"Predicted Height: {prediction:.2f} cm")