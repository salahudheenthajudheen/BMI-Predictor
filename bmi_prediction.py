import streamlit as st

from py_bmi import bmi
st.title("BMI Predictor")
a = st.text_input("Enter Your Height ( in meters )")
b = st.text_input("Enter Your Weight ( in kilograms ")
def predict():
    height = a
    weight = b
    st.success(bmi(weight,height))
if st.button("Calculate"):
    predict()















