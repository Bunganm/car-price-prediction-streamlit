import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('model_mobil.pkl', 'rb'))

# Judul aplikasi
st.title('Prediksi Harga Mobil')

st.write('Masukkan spesifikasi mobil untuk memprediksi harga mobil.')

# Input user
engine_size = st.number_input('Engine Size', min_value=0.0)
horsepower = st.number_input('Horsepower', min_value=0)
wheelbase = st.number_input('Wheelbase', min_value=0.0)
width = st.number_input('Width', min_value=0.0)
length = st.number_input('Length', min_value=0.0)
curb_weight = st.number_input('Curb Weight', min_value=0.0)
fuel_capacity = st.number_input('Fuel Capacity', min_value=0.0)
fuel_efficiency = st.number_input('Fuel Efficiency', min_value=0.0)
power_perf_factor = st.number_input('Power Performance Factor', min_value=0.0)

# Tombol prediksi
if st.button('Prediksi Harga'):

    input_data = pd.DataFrame({
        'Engine_size': [engine_size],
        'Horsepower': [horsepower],
        'Wheelbase': [wheelbase],
        'Width': [width],
        'Length': [length],
        'Curb_weight': [curb_weight],
        'Fuel_capacity': [fuel_capacity],
        'Fuel_efficiency': [fuel_efficiency],
        'Power_perf_factor': [power_perf_factor]
    })

    prediction = model.predict(input_data)

    st.success(f'Prediksi Harga Mobil: {prediction[0]:.2f} ribuan dolar')

#==========================================================================================
#==========================================================================================
#                                   PENJELASAN
#File app.py digunakan untuk membuat aplikasi web sederhana menggunakan Streamlit sehingga pengguna dapat melakukan prediksi harga mobil melalui browser.
#==========================================================================================
#==========================================================================================