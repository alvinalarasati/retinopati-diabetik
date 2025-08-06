import streamlit as st
import numpy as np
from PIL import Image
import cv2
import plotly.express as px

from helper import classify_with_model
from settings import DESKRIPSI_KLASIFIKASI, LABEL_MAP
from auth import save_history

def show_main():
    st.header("📷 Upload Citra Retina")
    username = st.session_state.get("username")

    uploaded_file = st.file_uploader("Upload gambar retina", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="🩺 Citra Retina Anda", use_container_width=True)

        img_np = np.array(image)
        img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        if st.button("🔍 Klasifikasikan", type="primary"):
            label, probs = classify_with_model(img_cv)
            st.success(f"### ✅ Prediksi Stadium: {label}")
            st.markdown(f"**Penjelasan:** {DESKRIPSI_KLASIFIKASI[label]}")

            fig = px.bar(
                x=LABEL_MAP[:len(probs)],  # menyesuaikan jika model output < 5
                y=probs,
                labels={'x': 'Stadium', 'y': 'Probabilitas'},
                title="Distribusi Probabilitas Prediksi"
            )
            st.plotly_chart(fig, use_container_width=True)

            if username:
                save_history(username, label)
