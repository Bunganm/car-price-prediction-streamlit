import streamlit as st
import pandas as pd
import pickle

# =========================
# LOAD MODEL
# =========================
model = pickle.load(open('model_mobil.pkl', 'rb'))

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Prediksi Harga Mobil",
    page_icon="🌸",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #FFEAF4;
}

/* Judul */
.main-title {
    text-align: center;
    color: #C2185B;
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #AD1457;
    font-size: 20px;
    margin-bottom: 30px;
}

/* Card */
.card {
    background-color: #FFFFFF;
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

/* Harga */
.price-box {
    background-color: #FFB6C1;
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #880E4F;
    margin-top: 20px;
}

/* Footer */
.footer {
    background-color: #F8BBD0;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    color: #880E4F;
    font-weight: bold;
    font-size: 18px;
    margin-top: 30px;
}

/* Tombol */
.stButton>button {
    background-color: #EC407A;
    color: white;
    border-radius: 15px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #D81B60;
    color: white;
}

/* Input */
.stNumberInput input {
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(
    """
    <div class="main-title">
        🌸 Prediksi Harga Mobil 🌸
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Sistem prediksi harga mobil menggunakan metode Linear Regression
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# LAYOUT
# =========================
col1, col2 = st.columns(2)

# =========================
# INPUT SECTION
# =========================
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

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

    predict_button = st.button("💖 Prediksi Harga")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# OUTPUT SECTION
# =========================
with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("💰 Hasil Prediksi Harga")

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
            <div class="price-box">
                💸 ${prediction[0]:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### ✨ Detail Input")

        st.write(f"Engine Size : {engine_size}")
        st.write(f"Horsepower : {horsepower}")
        st.write(f"Fuel Efficiency : {fuel_efficiency}")

    else:

        st.info("Masukkan spesifikasi mobil lalu klik tombol prediksi.")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown(
    """
    <div class="footer">
        🌸 SISTEM INI DIBUAT OLEH 🌸 <br><br>
        NAMA : Bunga Nur Munawaroh <br>
        NPM : 237006110
    </div>
    """,
    unsafe_allow_html=True
)
