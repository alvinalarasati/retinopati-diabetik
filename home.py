import streamlit as st
from settings import APP_NAME
from datetime import datetime

def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 11:
        return "Selamat pagi"
    elif 11 <= hour < 15:
        return "Selamat siang"
    elif 15 <= hour < 18:
        return "Selamat sore"
    else:
        return "Selamat malam"

def show_home():
    username = st.session_state.get("username", "Pengguna")
    greeting = get_greeting()

    st.title(APP_NAME)
    st.markdown(f"### 👋 {greeting}, **{username.capitalize()}!**")

    st.markdown("""
        Aplikasi ini mengklasifikasikan **stadium Retinopati Diabetik** berdasarkan citra retina
        menggunakan model CNN. Upload citra retina Anda dan dapatkan hasil klasifikasi beserta penjelasannya.
    """)
