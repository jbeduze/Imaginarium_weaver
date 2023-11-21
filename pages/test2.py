import streamlit as st
from PIL import Image


a = st.file_uploader("upload image")
b = "./app/static/tempimage.jpg"

if a is not None:
  im = Image(a)
  st.image(im)
