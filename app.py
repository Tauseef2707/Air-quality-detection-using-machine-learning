import streamlit as st
import pandas as pd
import joblib

st.title("Air Quality Prediction System")

# Load model
model = joblib.load("air_quality_model.pkl")

# User input
pm25 = st.number_input("PM2.5 value", 0.0, 1000.0, 50.0)
pm10 = st.number_input("PM10 value", 0.0, 1000.0, 60.0)
no2 = st.number_input("NO2 value", 0.0, 1000.0, 30.0)
so2 = st.number_input("SO2 value", 0.0, 1000.0, 10.0)

if st.button("Predict AQI"):
    data = [[pm25, pm10, no2, so2]]
    prediction = model.predict(data)
    st.success(f"Predicted AQI: {prediction[0]}")
