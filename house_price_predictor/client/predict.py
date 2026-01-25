from pydantic import BaseModel,Field,field_validator
from fastapi import FastAPI ,HTTPException
from typing import List,Literal
import json
import pickle
import os 
app=FastAPI()
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
    bath:int=Field(description="Enter the bathroom",gt=0,lt=10)
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


@app.post("/predict")
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
    return {"estimated_price":estimated_price}
