import streamlit as st
from auth import login, register_user
from home import show_home
from main import show_main
from history import show_history
import re

st.set_page_config(page_title="Retinopati Diabetik", layout="wide")

if 'login_state' not in st.session_state:
    st.session_state.login_state = False
if 'register_mode' not in st.session_state:
    st.session_state.register_mode = False
if 'notification' not in st.session_state:
    st.session_state.notification = ""

if not st.session_state.login_state:
    if st.session_state.register_mode:
        st.title("📝 Register Pengguna Baru")
        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")
        confirm_pass = st.text_input("Ulangi Password", type="password")

        if st.button("Daftar"):
            if not new_user or " " in new_user:
                st.error("Username tidak boleh kosong atau mengandung spasi.")
            elif new_pass != confirm_pass:
                st.error("Password dan konfirmasi tidak cocok.")
            else:
                success, message = register_user(new_user, new_pass)
                if success:
                    st.success(message)
                    st.session_state.notification = " Pendaftaran berhasil. Silakan login."
                    st.session_state.register_mode = False
                else:
                    st.error(message)

        if st.button("🔙 Kembali ke Login"):
            st.session_state.register_mode = False

    else:
        st.title("🔐 Login Pengguna")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(username, password):
                st.session_state.login_state = True
                st.session_state.username = username
                st.session_state.notification = f" Selamat datang, {username.capitalize()}!"
                st.success("Login berhasil!")
                st.rerun()
            else:
                st.error("Login gagal. Username atau password salah.")
        if st.button("🆕 Daftar Akun Baru"):
            st.session_state.register_mode = True

else:
    if st.session_state.notification:
        st.sidebar.success(st.session_state.notification)
        st.session_state.notification = ""

    menu = st.sidebar.selectbox("📌 Navigasi", ["🏠 Beranda", "📊 Klasifikasi", "📜 Riwayat", "🚪 Logout"])
    if menu == "🏠 Beranda":
        show_home()
    elif menu == "📊 Klasifikasi":
        show_main()
    elif menu == "📜 Riwayat":
        show_history()
    elif menu == "🚪 Logout":
        st.session_state.login_state = False
        st.session_state.username = ""
        st.session_state.notification = ""
        st.rerun()
