import streamlit as st
import joblib
import numpy as np

model = joblib.load("C:/Users/anuj0/Downloads/House Price India/model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learning for predicting house prices based on given features of the house. You can enter the inputs below, then click the 'Predict' button to get the estimated house price.")

st.divider()

Bedrooms = st.number_input("Number of bedrooms", min_value=0, value=0)
Bathrooms = st.number_input("Number of bathrooms", min_value=0, value=0)
LivingArea = st.number_input("Living Area (sq ft)", min_value=0, value=2000)
Floors = st.number_input("Number of floors", min_value=0.0, value=1.5, step=0.1)
Condition = st.number_input("Condition (1=poor, 5=excellent)", min_value=0, value=3)
Number_oF_Schools = st.number_input("Number of schools nearby", min_value=0, value=0)

st.divider()

Predict_Button = st.button("Predict!")

if Predict_Button:
    st.balloons()  
    
    x = np.array([[Bedrooms, Bathrooms, LivingArea, Floors, Condition, Number_oF_Schools]])

    prediction = model.predict(x)

    st.write(f"Predicted House Price: ${prediction[0]:,.2f}")
    
else:
    st.write("Please enter the values and click 'Predict!' to get the price prediction.")




#order of x['number of bedrooms', 'number of bathrooms', 'living area', 'lot area',
       #'number of floors', 'condition of the house',
       #'Area of the house(excluding basement)', 'Area of the basement',
       #'Number of schools nearby', 'Distance from the airport']