from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
import pickle 
import numpy as np

class Input(BaseModel):
    air_temperature_k: float
    process_temperature_k: float 
    rotational_speed_rpm: float
    torque_nm: float 
    tool_wear_mins: int
    product_type: str 


# Maintenance prediction model and preprocessing loading
model = pickle.load(open('maintenance-failure-model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

app =FastAPI()


@app.post('/predict_failure')
def predict_failure(data: Input):
    input_list = [[
        data.air_temperature_k,
        data.process_temperature_k,
        data.rotational_speed_rpm,
        data.torque_nm,
        data.tool_wear_mins,
        encoder.transform([[data.product_type]])[0][0],
    ]]
    print(input_list)

    prediction = model.predict(input_list)

    print(prediction)
    mapping = {
        0: 'Heat Dissipation Failure',
        1: 'No Failure',
        2: 'Overstrain Failure',
        3: 'Power Failure',
        4: 'Random Failures',
        5: 'Tool Wear Failure' 

    }

    return {"prediction": mapping[prediction.item()]}





