# -*- coding: utf-8 -*-
from imageai.Detection import ObjectDetection
import os 
import streamlit as st
from PIL import Image
import numpy as np
import re

st.set_page_config(layout="wide")
st.title("Object Detection")
file = st.sidebar.file_uploader("Please input a file",type=("jpg","png"))

if not file:
    st.warning('Please input a image')
    st.stop()

image=Image.open(file)

if  '.png' in file.name :
    image.save("image.png")

elif  '.jpg' in file.name :
    image.save("image.jpg")
    
exection_path = os.getcwd()

before, after = st.columns(2)

with before:
    st.header('Input data')
    if  '.png' in file.name :
        st.image('image.png')

    elif  '.jpg' in file.name :
        st.image('image.jpg')

with after:
    st.header('Output data')
    with st.spinner('Now Detecting ...'):
        detector = ObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(os.path.join(exection_path,"./yolo.h5"))
        detector.loadModel()
        if  '.png' in file.name :
            detections = detector.detectObjectsFromImage(input_image='image.png',output_image_path=os.path.join(exection_path,"imagenew.png"))
            st.image('imagenew.png')
        elif  '.jpg' in file.name :
            detections = detector.detectObjectsFromImage(input_image='image.jpg',output_image_path=os.path.join(exection_path,"imagenew.jpg"))
            st.image('imagenew.jpg')
