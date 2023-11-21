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
    
    # Save the uploaded image as a temporary file
    temp_image_path = os.path.join("static", "tempimage.jpg")
    with open(temp_image_path, "wb") as f:
        uploaded_img.seek(0)  # Rewind the file pointer to the beginning
        f.write(uploaded_img.read())
    
    # Display the temporary image using st.image
    st.image(temp_image_path, caption="adsfad Image", use_column_width=True)

    # Create a URL for the uploaded image
    app_url = "https://imaginariumweaver.streamlit"  # Change this to your app's URL
    image_url = f"{app_url}/app/~/+/static/temp_image.jpg"

    # Display the URL as a clickable link
    st.markdown(f"[![Click to view uploaded image]({image_url})]({image_url})")

    # Convert the PIL Image to base64 encoding
    buffered = BytesIO()
    image.save(buffered, format="JPEG")  # Change format as needed
    image_base64 = base64.b64encode(buffered.getvalue()).decode()

    body = {
        "theme": "create a magical story of everly and mr.deer",
        "mainCharacterImage": image_base64  # Include the base64 encoded image
    }

    file_name = uploaded_img.name
    st.write(f"Uploaded filename: {file_name}")
else:
    st.warning("Please upload an image.")  
