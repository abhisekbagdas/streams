import streamlit as st
import os
from PIL import Image
from rembg import remove

print("ok")
st.title("Remove Backgroung")

upload_file = st.file_uploader("Upload your image")

if upload_file:
  st.spinner("Removing Background...")
  img = Image.open(upload_file)
  st.subheader("Orignal Image")
  st.image(img, use_container_width = True)

  if st.button("Remove Background"):
    with st.spinner("Removing Background..."):
      output = remove(img)
    st.subheader("Background Removed")