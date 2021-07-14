import streamlit as st
from PIL import Image
import os

import style

st.title("Style Transfer with Pytorch")



style_name = st.sidebar.selectbox(
    "Select style image", 
    ("candy", "mosaic", "udnie")
)

model = os.path.join('saved_models', style_name + '.pth')

#print(model)
# r'\saved_models\candy.pth