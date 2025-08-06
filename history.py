import streamlit as st
import plotly.express as px
from auth import get_history

def show_history():
    username = st.session_state.get("username")
    st.header("📜 Riwayat Klasifikasi Anda")
    if username:
        history = get_history(username)
        if history:
            st.write(f"Anda telah melakukan klasifikasi sebanyak {len(history)} kali.")
            fig = px.histogram(x=history, labels={'x': 'Stadium'}, title="Distribusi Riwayat Klasifikasi")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Belum ada riwayat klasifikasi.")
    else:
        st.warning("Anda belum login.")