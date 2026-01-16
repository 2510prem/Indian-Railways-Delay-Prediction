import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("Models/delay_prediction_model.pkl", "rb"))

st.set_page_config(page_title="Indian Railways Delay Predictor", layout="centered")

st.title("🚆 Indian Railways Train Delay Predictor")
st.write("Predict expected train delay using machine learning")

# User inputs
train_type = st.selectbox(
    "Train Type",
    ['Express', 'Superfast', 'Rajdhani', 'Shatabdi', 'Passenger', 'Vande Bharat', 'Duranto']
)

source = st.selectbox(
    "Source Station",
    ['NDLS', 'HWH', 'PNBE', 'UMB', 'CSMT', 'CNB', 'DDU', 'MAS', 'BZA', 'SBC']
)

destination = st.selectbox(
    "Destination Station",
    ['NDLS', 'HWH', 'PNBE', 'UMB', 'CSMT', 'CNB', 'DDU', 'MAS', 'BZA', 'SBC']
)

distance = st.slider("Distance (km)", 200, 2000, 800)

day_of_week = st.selectbox(
    "Day of Journey",
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

month = st.slider("Month", 1, 12, 6)

# Predict button
if st.button("Predict Delay"):
    input_df = pd.DataFrame({
        'train_type': [train_type],
        'source': [source],
        'destination': [destination],
        'distance_km': [distance],
        'day_of_week': [day_of_week],
        'month': [month]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"⏱️ Expected Delay: {prediction:.2f} minutes")