import streamlit as st
import math

st.title("Menghitung :blue[Volume Tabung] :sunglasses:")

r = st.number_input("Masukan Jari-Jari (cm): ",0)
t = st.number_input("Masukan Tinggi (cm): ",0)

if st.button("Hitung Volume", type="primary"):
  v = math.pi*(r**2)*t
  st.succes(f'Volume tabung adalah {v:.2f}')
