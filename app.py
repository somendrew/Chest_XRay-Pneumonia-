import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
install('opencv-python')

import cv2
import os
import numpy as np
import streamlit as st
import tensorflow as tf
#from keras  import load_model

# Load your trained model
model = tf.keras.models.load_model('pneumonia_detection_model.h5') 
# Define labels
labels = ["PNEUMONIA","NORMAL"]

def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (180, 180))
    image = np.array(image) / 255.0
    image = image.reshape(-1, 180, 180, 1)
    return image

def predict(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return labels[int(prediction[0][0] > 0.5)]

def main():
    st.title("Chest X-Ray Pneumonia Detection")
    st.write("Upload an X-Ray image to classify it as Normal or Pneumonia.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        if st.button("Predict"):
            result = predict(image)
            st.success(f'The model predicts: **{result}**')
    
    # Add a footer
    st.markdown("""
        <p style='text-align: center; color: grey'>
            <p style='text-align: center; color: grey'> Developed by Somendra Singh</p>
            <a href='https://www.linkedin.com/in/somendrew/' target='_blank'><img src='https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg' width='20' height='20' alt='LinkedIn'></a>
            <a href='https://www.instagram.com/somendrew/' target='_blank'><img src='https://www.vectorlogo.zone/logos/instagram/instagram-icon.svg' width='20' height='20' alt='Instagram'></a>
            <a href='https://www.kaggle.com/somendrew/' target='_blank'><img src='https://www.vectorlogo.zone/logos/kaggle/kaggle-icon.svg' width='20' height='20' alt='Kaggle'></a>
        </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
