import streamlit as st
import requests
import json
from PIL import Image
import os
from io import BytesIO
import base64

URL_WEBHOOK = "https://hooks.zapier.com/hooks/catch/17095058/3krt46r/"

uploaded_img = st.file_uploader("Upload a picture of the person/pet you'd like on a card, board, or coloring page", type=['png', 'jpg', 'jpeg', 'gif'])

# Check if an image has been uploaded
if uploaded_img is not None:
    # To read image file buffer with PIL:
    from PIL import Image
    image = Image.open(uploaded_img)

    # Display the uploaded image
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Please verify that this is the correct image. If not, please delete and upload a new image")
else:
    st.warning("Please upload an image.")  

# Convert the PIL Image to base64 encoding
if 'image' in locals():
    buffered = BytesIO()
    image.save(buffered, format="JPEG")  # Change format as needed
    image_base64 = base64.b64encode(buffered.getvalue()).decode()

    body = {
        "theme": "create a magical story of everly and mr.deer",
        "mainCharacterImage": image_base64  # Include the base64 encoded image
    }

file_name = uploaded_img.name
st.write(f"Uploaded filename: {file_name}")
