import streamlit as st
from PIL import Image
import os
import style
import io
import base64
import shutil


INFILE = "input"
OUTFILE = "output"
if not os.path.isdir(INFILE):
    os.makedirs(INFILE)
if not os.path.isdir(OUTFILE):
    os.makedirs(OUTFILE)

def get_image_download_link(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = io.BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}">Download</a>'
	return href

st.title("Style Transfer with Pytorch")



uploaded_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])

style_name = st.sidebar.selectbox(
    "Select Style", 
    ("candy", "mosaic", "rain_princess", "udnie")
)

model = os.path.join('saved_models', style_name + '.pth')

#print(input_img)
if uploaded_file is not None:
    input_img = INFILE + "/" + uploaded_file.name 
    output_img = OUTFILE + "/" + style_name + "--" + uploaded_file.name
    st.write("### Source Image:")
    
    image = Image.open(uploaded_file)
    image.save(input_img)
    print(type(image))
    st.image(image, width = 300, use_column_width=True)

clicked = st.button("Run Style Transfer")
if clicked:
    
    model = style.load_model_style_transfer(model)
    style.stylize(model, input_img,output_img)

    st.write("### Stylized Image:")
    image = Image.open(output_img)
    st.image(image, width = 400, use_column_width=True)
    
    st.markdown(get_image_download_link(image), unsafe_allow_html=True)





