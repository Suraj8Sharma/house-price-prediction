from fastapi import FastAPI
app = FastAPI()
import pickle
import json
import numpy as np
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# Initialize global variables as None
__data_columns = None
__model = None

# --- MANDATORY FOR FRONTEND CONNECTION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
def load_data():
    print("loading the artificats:")
    global __data_columns
    global __model
    with open("./artificats/columns.json","r") as f:
        __data_columns=json.load(f)["data_columns"]#by this the key named data_columns will be accessed
    with open ("./artificats/banglore_home_price_model.pickle","rb") as f:
        __model=pickle.load(f)
        #loading is done 
    return __data_columns,__model
load_data()
#this is because in frontend we want to build a dropdown menu of this location
def get_location_names():
    data=__data_columns[3:]
    # print(data)
    return data#as first 3 columns are not location names
get_location_names()
#for getting data from the frontend
class HomePriceInput(BaseModel):
    total_sqft: float
    bhk: int
    bath: int
    location: str
def estimate_price(location,sqft,bhk,bath):
    try:
        location_index=__data_columns.index(location.lower())
    except:
        location_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if location_index>=0:
        x[location_index]=1
    return round(__model.predict([x])[0],2)
@app.get("/location_name")
def location_name():
    location=get_location_names()
    return {"location":location}

@app.post("/predict_home_price")
def predict_home_price(data: HomePriceInput):
    # FastAPI has already converted 'data' into a Python object for you!
    # You access them like variables: data.total_sqft, data.location, etc.
    
    estimated_price = estimate_price(
        data.location, 
        data.total_sqft, 
        data.bhk, 
        data.bath
    )
    
    # Return a dictionary (FastAPI converts this to JSON automatically)
    return {"estimated_price": estimated_price}

