import streamlit as st
import requests

st.set_page_config(page_title="Model Predictor", layout="centered")
st.title("Model Prediction UI")

API_URL = "http://127.0.0.1:8000/predict"

st.subheader("Enter input features")

f0 = st.number_input("f0", value=0.0)
f1 = st.number_input("f1", value=0.0)

if st.button("Predict"):
    payload = {"f0": float(f0), "f1": float(f1)}
    
    try:
        resp = requests.post(API_URL, json=payload)
        st.write("Response:", resp.json())
    except Exception as e:
        st.error(f"Request failed: {e}")