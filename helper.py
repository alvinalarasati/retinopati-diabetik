import numpy as np
import tensorflow as tf
import cv2
from settings import LABEL_MAP

# Load model
MODEL = tf.keras.models.load_model("weights/model_augmented_wcgan.keras")

# Preprocessing identik dengan saat training
def preprocess_for_prediction(image):
    img = cv2.resize(image, (128, 128))
    img = img.astype('float32') / 255.0

    # CLAHE preprocessing dan konversi grayscale
    gray = cv2.cvtColor((img * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(gray)

    # Kembalikan ke RGB dan normalisasi
    img_rgb = cv2.cvtColor(clahe_img, cv2.COLOR_GRAY2RGB) / 255.0

    return np.expand_dims(img_rgb, axis=0)  # shape (1, 128, 128, 3)

# Fungsi klasifikasi
def classify_with_model(image):
    img = preprocess_for_prediction(image)
    preds = MODEL.predict(img)

    # Logging hasil prediksi mentah
    print("Prediksi mentah:", preds[0])

    label = LABEL_MAP[np.argmax(preds)]
    return label, preds[0]
