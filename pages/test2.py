import streamlit as st
from PIL import Image


uploaded_img = st.file_uploader("Upload a picture of the person/pet you'd like on a card, board, or coloring page", type=['png', 'jpg', 'jpeg', 'gif'])

# Check if an image has been uploaded
if uploaded_img is not None:
    # To read image file buffer with PIL:
    from PIL import Image
    image = Image.open(uploaded_img)
