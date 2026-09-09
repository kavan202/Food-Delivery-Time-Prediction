import streamlit as st
import joblib
import pandas as pd
import gdown
import os

# Download model file if not exists
MODEL_PATH = "pipe.pkl"
if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/file/d/1mzTd9yn2cWZ4mOG9nshjqhQFBVTFb39Z/view?usp=sharing"
    gdown.download(url, MODEL_PATH)

# Load model
model = joblib.load(MODEL_PATH)

# Streamlit UI
st.title("🍽️Food Delivery Time Prediction 🍕🍔🍟🌭🥪")
st.write("Using XGBooster")

# Input fields
age = st.slider("Delivery preson age",min_value=15.0,max_value=60.0,step=1.0)
rating = st.slider("Rating",min_value=0.0,max_value=5.0,step=0.1)
time_or=st.slider("Current Time",min_value=00.0,max_value=23.0,step=1.0)
dist= st.text_input("Distance(in km)")
weathe=st.selectbox('Weather : ',['Sunny', 'Stormy', 'Sandstorms', 'Cloudy', 'Fog', 'Windy'])
road_traf=st.selectbox('Trafic : ',['High', 'Jam', 'Low', 'Medium'])
v_c=st.selectbox('Vehicale condition : ',[0, 1, 2,3])
t_o_v=st.selectbox('Vehical : ',['motorcycle', 'scooter', 'electric_scooter', 'bicycle'])
multi_d=st.selectbox('Multi deliverys : ',[0, 1,2, 3])
festival=st.selectbox('Festival : ',['No', 'Yes'])
city=st.selectbox('City : ',['Urban', 'Metropolitian', 'Semi-Urban'])

# Delivery_person_Age', 'Delivery_person_Ratings', 'Distance',
#        'Time_Orderd', 'Weatherconditions', 'Road_traffic_density',
#        'Vehicle_condition', 'Type_of_vehicle', 'multiple_deliveries',
#        'Festival', 'City'

# Prediction button
# if st.button("Predict Price", type="primary"):
#     input_data = pd.DataFrame([['age', 'rating','dist','time_or','weathe','road_traf','v_c','t_o_v','multi_d','festival','city']],
#                               columns=['Delivery_person_Age', 'Delivery_person_Ratings', 'Distance',
#        'Time_Orderd', 'Weatherconditions', 'Road_traffic_density',
#        'Vehicle_condition', 'Type_of_vehicle', 'multiple_deliveries',
#        'Festival', 'City'])

# Prediction button
if st.button("Predict Price", type="primary"):
    # 1. Create a dictionary mapping the EXACT model columns to your Streamlit variables
    input_dict = {
        'Delivery_person_Age': [age],
        'Delivery_person_Ratings': [rating],
        'Distance': [float(dist) if dist else 0.0],  # Convert text input to float safely
        'Time_Orderd': [time_or],
        'Weatherconditions': [weathe],
        'Road_traffic_density': [road_traf],
        'Vehicle_condition': [v_c],
        'Type_of_vehicle': [t_o_v],
        'multiple_deliveries': [multi_d],
        'Festival': [festival],
        'City': [city]
    }
    
    # 2. Convert to DataFrame
    input_data = pd.DataFrame(input_dict)
    
    # Make prediction
    prediction = model.predict(input_data)
    st.success(f"Predicted Time: {prediction[0]:.2f} minutes")
