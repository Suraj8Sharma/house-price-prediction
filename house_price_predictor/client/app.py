import streamlit as st 
import requests
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

input_area=st.number_input("Enter Area:",placeholder=70)

#for bhk
input_bhk=st.number_input("Enter BHK's",placeholder=2)

#for bathrooms
input_bathrooms=st.number_input("Enter Bathrooms",placeholder=2)

#for location
input_location=st.selectbox(label="Enter Your Location",options=locations)

#submission buttom 
if st.button("Predict"):
    payload={
        "total_sqft":input_area,
        "bhk":input_bhk,
        "bath":input_bathrooms,
        "location":input_location,
        
    }
    #sending the request
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code==200:
            prediction=response.json().get("estimated_price")
            st.success(f"Predicted Price is rs.{prediction} lakhs")
        elif response.status_code==422:
            
            # If Pydantic validation fails on the FastAPI side, it returns a 422 error
            error_data =response.json().get('detail')
            error_msg=error_data[0].get('msg')
            error_field = error_data[0].get('loc')[-1] 
            st.error(f"Error in {error_field}: {error_msg}")
            
    except:
        
        st.error("Wait! Is your FastAPI server running?")