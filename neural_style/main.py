import streamlit as st
from PIL import Image
import os
from tempfile import TemporaryDirectory
import style




st.title("Style Transfer with Pytorch")



uploaded_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])

style_name = st.sidebar.selectbox(
    "Select style image", 
    ("candy", "mosaic", "rain_princess", "udnie")
)

model = os.path.join('saved_models', style_name + '.pth')
#  with TemporaryDirectory(prefix="myapp-") as tmpdir:
if uploaded_file is not None:

    st.write("### Source Image:")
    image = Image.open(uploaded_file)
    st.image(image, width = 300, use_column_width=True)

clicked = st.button("Run Style Transfer")
if clicked:
    model = style.load_model_style_transfer(model)
    out_img = style.stylize(model, image)

    st.write("### Stylized Image:")
    img = Image.fromarray(out_img)
    img.save(filename)
    image = Image.open(out_img)
    st.image(image, width = 400, use_column_width=True)



#print(model)
# r'\saved_models\candy.pth