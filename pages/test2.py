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
