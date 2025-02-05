import streamlit as st
import requests

st.title("Country Category Predictor")

# User inputs for features
country = st.text_input("Enter a Country Name (e.g., India, USA, Germany, Japan)")
b = st.number_input("Enter Child Mortality")
c = st.number_input("Enter Income per person")
d = st.number_input("Enter Inflation rate")
e = st.number_input("Enter Life Expectancy")
f = st.number_input("Enter Total Fertility")
g = st.number_input("Enter GDP per person")
h = st.number_input("Enter Export per person")
i = st.number_input("Enter Import per person")
j = st.number_input("Enter Health Spent per person")

if st.button("Predict Category"):
    # Prepare the request data
    features = [b,c,d,e,f,g,h,i,j]
    response = requests.post("http://43.204.83.178:5000/predict", json={"features": features})

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        message = response.json()["message"]
        st.success(f"The category for {country} is: {prediction}")
        st.write(f"Prediction message: {message}")
    else:
        st.error("Error in prediction request.")
