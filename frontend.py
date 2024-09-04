import streamlit as st
import requests
import json

st.set_page_config(page_title="Maintenance Failure Prediction", layout="centered")
st.title("Maintenance Failure Prediction")
st.markdown("Enter the machine parameters to predict the type of failure.")

air_temperature_k = st.number_input("Air Temperature (K)", min_value=290.0, max_value=310.0, value=298.0, step=0.1)
process_temperature_k = st.number_input("Process Temperature (K)", min_value=290.0, max_value=320.0, value=300.0, step=0.1)
rotational_speed_rpm = st.number_input("Rotational Speed (RPM)", min_value=1000.0, max_value=3000.0, value=1500.0, step=1.0)
torque_nm = st.number_input("Torque (Nm)", min_value=0.0, max_value=100.0, value=40.0, step=0.1)
tool_wear_mins = st.number_input("Tool Wear (mins)", min_value=0, max_value=300, value=100, step=1)
product_type = st.selectbox("Product Type", ["L", "M", "H"])

if st.button("Predict"):
    input_data = {
        "air_temperature_k": air_temperature_k,
        "process_temperature_k": process_temperature_k,
        "rotational_speed_rpm": rotational_speed_rpm,
        "torque_nm": torque_nm,
        "tool_wear_mins": tool_wear_mins,
        "product_type": product_type
    }

    response = requests.post("http://127.0.0.1:8000/predict_failure", json=input_data)
    
    # Handle the response and display the prediction
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.success(f"Predicted Failure: {prediction}")
        if prediction == "No Failure":
            st.balloons()
        else:
            st.error(f"Attention Required: {prediction}")
    else:
        st.error(f"Error: {response.status_code}")
        
# Adding some visuals
st.markdown("---")
st.markdown("### Machine Parameters Overview")
st.markdown("Visual representation of the input parameters")

# Displaying bar charts 
# st.bar_chart({
#     "Temperature (K)": [air_temperature_k, process_temperature_k],
#     "Rotational Speed (RPM)": [rotational_speed_rpm],
#     "Torque (Nm)": [torque_nm],
#     "Tool Wear (mins)": [tool_wear_mins]
# })

st.markdown("---")
st.markdown("### About this app")
st.markdown("This app predicts potential maintenance failures based on machine parameters using a trained machine learning model.")
