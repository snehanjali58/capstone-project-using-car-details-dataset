# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ScfKxgOwbd55xhZkn7iViRAUj4WEVJGK
"""

#Importing the necessary libararies.
import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('best_model.pkl')

def predict_price(year, km_driven, fuel, seller_type, transmission, owner):
    data = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner]
    })

    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()

    data=sc.fit_transform(data)

    prediction = model.predict(data)
    return prediction[0]



# Streamlit web app layout
st.title('Car Price Prediction App')
st.write("Predict the selling price of a used car based on its characteristics")

# User input fields
year = st.number_input('Year of Manufacture', min_value=1990, max_value=2024, value=2015)
km_driven = st.number_input('Kilometers Driven', min_value=0, max_value=1000000, value=50000)
fuel = st.selectbox('Fuel Type 0(CNG), 1(Disel), 2(Electric),3(LPG),4(Petrol)', [0,1,2,3,4])
seller_type = st.selectbox('Seller Type 0(Dealer), 1(Individual) 2(Trust Dealer)', [0,1,2])
transmission = st.selectbox('Transmission 0(Automatic), 1(Manual)', [0,1])
owner = st.selectbox('Owner 0(1st Owner), 1(4th & above owner), 2(2nd owner), 3(Test Drive), 4(3rd Owner)', [0,1,2,3,4])

# Predict button
if st.button('Predict Price'):
    result = predict_price(year, km_driven, fuel, seller_type, transmission, owner)
    st.success(f"The predicted selling price of the car is: ₹ {np.round(result, 2)}")
