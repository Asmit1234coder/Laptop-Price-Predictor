import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and expected columns
model = joblib.load("randomforesr.pkl")
expected_columns = joblib.load("ExpColumns.pkl")  # this should be list of training columns

st.title("💻 Laptop Predictor")

company = st.selectbox('Brand',['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo',
       'Chuwi', 'MSI','Microsoft', 'Toshiba', 'Huawei',
       'Xiaomi', 'Vero', 'Razer','Mediacom', 'Samsung',
       'Google', 'Fujitsu', 'LG'])

type_name = st.selectbox('Type',['Ultrabook', 'Notebook', 'Netbook', 'Gaming',
       '2 in 1 Convertible','Workstation'])

ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

weight = st.number_input('Weight of the Laptop')

touchscreen = st.selectbox('Touchscreen',['No','Yes'])
ips = st.selectbox('IPS',['No','Yes'])

screen_size = st.slider('Screensize in inches', 10.0, 18.0, 13.0)

resolution = st.selectbox('Screen Resolution',
       ['1920x1080','1366x768','1600x900','3840x2160',
        '3200x1800','2880x1800','2560x1600',
        '2560x1440','2304x1440'])

cpu = st.selectbox('CPU',['Intel Core i5', 'Intel Core i7',
       'AMD', 'Intel Core i3','Other Intel Processor'])

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
gpu = st.selectbox('GPU',['Intel', 'AMD', 'Nvidia'])
os = st.selectbox('OS',['Mac', 'Other OS', 'Windows'])

predict_btn = st.button("🔍 Predict Price")

# --------------------------------------------------

if predict_btn:

    # Convert Yes/No to 0/1
    touchscreen = 1 if touchscreen == "Yes" else 0
    ips = 1 if ips == "Yes" else 0

    # Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Create input dictionary (LIKE YOUR PREVIOUS PROJECT)
    input_data = {
        "Company": company,
        "TypeName": type_name,
        "Ram": ram,
        "Weight": weight,
        "Touchscreen": touchscreen,
        "IPSpanel": ips,
        "ppi": ppi,
        "CPU_brand": cpu,
        "HDD": hdd,
        "SSD": ssd,
        "Gpu_brand": gpu,
        "os": os
    }

    input_df = pd.DataFrame([input_data])

    # One-hot encoding
    input_df = pd.get_dummies(input_df)

    # Match training columns
    input_df = input_df.reindex(columns=expected_columns, fill_value=0)

    # Prediction
    prediction = np.exp(model.predict(input_df)[0])

    st.success(f"💰 Predicted Laptop Price: ₹ {int(prediction)}")