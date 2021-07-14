import streamlit as st
from PIL import Image

import style

st.title("Style Transfer with Pytorch")



style_name = st.sidebar.selectbox(
    "Select style image", 
    ("candy", "mosaic", "udnie")
)
