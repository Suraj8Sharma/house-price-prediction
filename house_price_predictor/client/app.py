import streamlit as st 

import json
import os 
# This gets the exact folder where app.py is located
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "columns.json")
with open(file_path,"r") as f:
    data=json.load(f)
    locations=data["data_columns"][3:]
#giving the header for our ui
st.header("HOUSE-PRICE-PREDICTION")

#making the fields for the input 

st.text_input("Enter Area:",placeholder=70)

#for bhk
st.text_input("Enter BHK's",placeholder=2)

#for bathrooms
st.text_input("Enter Bathrooms",placeholder=2)

#for location
st.selectbox(label="Enter Your Location",options=locations)

#submission buttom 
if st.button("Predict"):
    pass