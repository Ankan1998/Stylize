import streamlit as st
from PIL import Image
import os

import style

st.title("Style Transfer with Pytorch")

img = st.sidebar.selectbox(
    "Select image", 
    ("amber.jpg",)
)

style_name = st.sidebar.selectbox(
    "Select style image", 
    ("candy", "mosaic", "rain_princess", "udnie")
)

model = os.path.join('saved_models', style_name + '.pth')
input_img = "images/content-images/" + img
out_img = "images/output-images" + style_name + "-" + img

st.write("### Source Image:")
image = Image.open(input_img)
st.image(image, width = 400, use_column_width=True)

clicked = st.button("Run Style Transfer")
if clicked:
    model = style.load_model_style_transfer(model)
    style.stylize(model, input_img, out_img)

    st.write("### Stylized Image:")
    image = Image.open(out_img)
    st.image(image, width = 400, use_column_width=True)



#print(model)
# r'\saved_models\candy.pth