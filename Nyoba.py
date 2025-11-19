import streamlit as st
import math

# ================== STYLE ==================
st.set_page_config(page_title="Hitung Luas Bangun Datar", layout="centered")

# CSS pastel aesthetic
# ================== STYLE ==================
st.markdown("""
<style>

body {
    background-color: #F7F3FF;
}

/* Tombol */
div.stButton > button {
    background-color: #E8D9FF;
    color: #5A4B81;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
}
div.stButton > button:hover {
    background-color: #D2BFFF;
    color: black;
}

/* Biar selectbox pakai pointer */
.stSelectbox > div, .stSelectbox div[role="button"] {
    cursor: pointer !important;
}

</style>
""", unsafe_allow_html=True)



# ================== TITLE ==================
st.markdown("<h1 style='text-align:center; color:#5A4B81;'>Program Hitung Luas Bangun Datar</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
# ================== SELECT ==================
with st.container():

    shape = st.selectbox(
        "Pilih Bangun Datar",
        ["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran"]
    )

    # ================== INPUT FORM ==================
    if shape == "Persegi":
        sisi = st.number_input("Masukkan panjang sisi:", min_value=0.0)
        if st.button("Hitung Luas"):
            luas = sisi * sisi
            st.success(f"Luas Persegi = **{luas:.2f}**")

    elif shape == "Persegi Panjang":
        p = st.number_input("Panjang:", min_value=0.0)
        l = st.number_input("Lebar:", min_value=0.0)
        if st.button("Hitung Luas"):
            luas = p * l
            st.success(f"Luas Persegi Panjang = **{luas:.2f}**")

    elif shape == "Segitiga":
        a = st.number_input("Alas:", min_value=0.0)
        t = st.number_input("Tinggi:", min_value=0.0)
        if st.button("Hitung Luas"):
            luas = 0.5 * a * t
            st.success(f"Luas Segitiga = **{luas:.2f}**")

    elif shape == "Lingkaran":
        r = st.number_input("Jari-jari (r):", min_value=0.0)
        if st.button("Hitung Luas"):
            luas = math.pi * r * r
            st.success(f"Luas Lingkaran = **{luas:.4f}**")

# ================== FOOTER ==================
st.markdown("<br><p style='text-align:center; color:#9A8CC4;'>Made with 💗 using Streamlit</p>", unsafe_allow_html=True)
