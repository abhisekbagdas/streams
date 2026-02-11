import streamlit as st
import os
from PIL import Image
from rembg import remove
import io   # <-- for handling byte streams

print("ok")
st.title("Remove Background")

upload_file = st.file_uploader("Upload your image")

if upload_file:
    img = Image.open(upload_file)
    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Removing Background..."):
            output = remove(img)

        st.subheader("Background Removed")
        st.image(output)

        # Convert the output image to bytes
        img_bytes = io.BytesIO()
        output.save(img_bytes, format="PNG")
        img_bytes = img_bytes.getvalue()

        # Add a download button
        st.download_button(
            label="Download Image",
            data=img_bytes,
            file_name="background_removed.png",
            mime="image/png"
        )
