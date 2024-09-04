from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
import pickle 
import numpy as np
import os 

class Input(BaseModel):
    air_temperature_k: float
    process_temperature_k: float 
    rotational_speed_rpm: float
    torque_nm: float 
    tool_wear_mins: int
    product_type: str 

def modelPipeline(data):
    # Maintenance prediction model and preprocessing loading
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    model_path = os.path.join(base_dir, '../models/maintenance-failure-model.pkl')
    encoder_path = os.path.join(base_dir, '../models/encoder.pkl')

    model = pickle.load(open(model_path, 'rb'))
    encoder = pickle.load(open(encoder_path, 'rb'))
    
    input_list = [[
        data.air_temperature_k,
        data.process_temperature_k,
        data.rotational_speed_rpm,
        data.torque_nm,
        data.tool_wear_mins,
        encoder.transform([[data.product_type]])[0][0],
    ]]
   
    prediction = model.predict(input_list)
    mapping = {
        0: 'Heat Dissipation Failure',
        1: 'No Failure',
        2: 'Overstrain Failure',
        3: 'Power Failure',
        4: 'Random Failures',
        5: 'Tool Wear Failure' 
    }
    return mapping[prediction.item()]

app =FastAPI()


@app.post('/predict_failure')
def predict_failure(data: Input):
    
    prediction = modelPipeline(data)

    return {"prediction": prediction}





