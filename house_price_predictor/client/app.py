import streamlit as st 
import requests
from pydantic import BaseModel,Field,field_validator
from fastapi import FastAPI ,HTTPException
from typing import List,Literal
import json
import pickle
import os 
import numpy as np

# This gets the exact folder where app.py is located
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "columns.json")
with open(file_path,"r") as f:
    data=json.load(f)
    all_columns = [col.lower() for col in data["data_columns"]]
    locations=data["data_columns"][3:]

pickle_file=os.path.join(current_dir,"banglore_home_price_model.pickle")

with open(pickle_file,"rb") as f:
    model=pickle.load(f)

class user_input(BaseModel):
    total_sqft:float=Field(description="Enter the area ",gt=0)
    bath:int=Field(description="Enter the bathroom",gt=0,lt=15)
    bhk:int=Field(description="Enter the Bhk ",gt=0,lt=20)
    location:str

    @field_validator("bath","bhk",mode="before")
    @classmethod
    def float_to_int(cls,value):
        if isinstance(value, float):
            return int(value)
    
    @field_validator("location")
    @classmethod
    def validate_location(cls,value):
      valid_locations=locations    
      if value not in valid_locations:
          raise ValueError("Location must be from the  given columns ")



def predict(userinput:user_input):
    
    x=np.zeros(len(all_columns))
    x[0]=userinput.total_sqft
    x[1]=userinput.bath
    x[2]=userinput.bhk
    if userinput.location:
        loc_name = userinput.location.lower()
        location_index=all_columns.index(userinput.location.lower())
        x[location_index]=1
    estimated_price=round(model.predict([x])[0],2)
    return estimated_price

#For Streamlit:

#giving the header for our App
st.header("HOUSE-PRICE-PREDICTION")

#making the fields for the input 

input_area=st.number_input("Enter Area:")

#for bhk
input_bhk=st.number_input("Enter BHK's")

#for bathrooms
input_bathrooms=st.number_input("Enter Bathrooms")

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
    try:
            userinput=user_input(**payload)
         
            estimated_price=predict(userinput)
            st.success(f"Predicted Price is rs.{estimated_price} lakhs")
    except Exception as e:
            
            if hasattr(e, 'errors'):
                error_data = e.errors()
                error_msg=error_data[0].get('msg')
                error_field = error_data[0].get('loc')[-1] 
                st.error(f"Error in {error_field}: {error_msg}")
            
