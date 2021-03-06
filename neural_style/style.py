import argparse
import os
import sys
import time
import re

import numpy as np
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
import torch.onnx

import utils
from transformer_net import TransformerNet
import streamlit as st


DEVICE =torch.device("cuda" if torch.cuda.is_available() else "cpu")

@st.cache
def load_model_style_transfer(model_path):
    with torch.no_grad():
        style_model = TransformerNet()
        state_dict = torch.load(model_path)
        
        for k in list(state_dict.keys()):
            if re.search(r'in\d+\.running_(mean|var)$', k):
                del state_dict[k]
        style_model.load_state_dict(state_dict)
        style_model.to(DEVICE)
        style_model.eval()
        return style_model




@st.cache
def stylize(style_model, content_img,out_img):


    content_image = utils.load_image(content_img)
    content_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    content_image = content_transform(content_image)
    content_image = content_image.unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        output = style_model(content_image).cpu()
    
    # img = output[0].clone().clamp(0, 255).numpy()
    # img = img.transpose(1, 2, 0).astype("uint8")
    utils.save_image(out_img, output[0])
    
    