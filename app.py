import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('model_mobil.pkl', 'rb'))

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Harga Mobil",
    page_icon="🌸",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background-color: #FFF0F5;
}

h1, h2, h3 {
    color: #D63384;
}

.stButton>button {
    background-color: #FF69B4;
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #FF1493;
    color: white;
}

input {
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)

# Judul
st.markdown(
    """
    <h1 style='text-align: center;'>
    🌸 Prediksi Harga Mobil 🌸
    </h1>
    """,
    unsafe_allow_html=True
)

st.write(
    "<p style='text-align:center; color:#C71585;'>"
    "Sistem prediksi harga mobil menggunakan Linear Regression"
    "</p>",
    unsafe_allow_html=True
)

# Layout 2 kolom
col1, col2 = st.columns([1,1])

# =========================
# INPUT
# =========================
with col1:

    st.markdown("""
    <div style="
        background-color:#FFD1DC;
        padding:25px;
        border-radius:20px;">
    """, unsafe_allow_html=True)

    st.subheader("🚗 Input Spesifikasi Mobil")

    engine_size = st.number_input('Engine Size', min_value=0.0, step=0.1)
    horsepower = st.number_input('Horsepower', min_value=0)
    wheelbase = st.number_input('Wheelbase', min_value=0.0)
    width = st.number_input('Width', min_value=0.0)
    length = st.number_input('Length', min_value=0.0)
    curb_weight = st.number_input('Curb Weight', min_value=0.0)
    fuel_capacity = st.number_input('Fuel Capacity', min_value=0.0)
    fuel_efficiency = st.number_input('Fuel Efficiency', min_value=0.0)
    power_perf_factor = st.number_input('Power Performance Factor', min_value=0.0)

    predict_button = st.button("💖 Prediksi Harga Mobil")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# OUTPUT
# =========================
with col2:

    st.markdown("""
    <div style="
        background-color:#FFE4E1;
        padding:25px;
        border-radius:20px;">
    """, unsafe_allow_html=True)

    st.subheader("💰 Perkiraan Harga Mobil")

    if predict_button:

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

        st.markdown(
            f"""
            <div style="
                background-color:#FFB6C1;
                padding:35px;
                border-radius:20px;
                text-align:center;
                font-size:40px;
                font-weight:bold;
                color:#8B004B;">
                💸 ${prediction[0]:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("### ✨ Detail Input")
        st.write(f"Engine Size : {engine_size}")
        st.write(f"Horsepower : {horsepower}")
        st.write(f"Fuel Efficiency : {fuel_efficiency}")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        background-color:#FFC0CB;
        padding:20px;
        border-radius:20px;
        text-align:center;
        color:#8B004B;
        font-weight:bold;
        font-size:18px;">
        🌸 SISTEM INI DIBUAT OLEH 🌸 <br><br>
        NAMA : ISI NAMA KAMU <br>
        NIM : ISI NIM KAMU
    </div>
    """,
    unsafe_allow_html=True
)
