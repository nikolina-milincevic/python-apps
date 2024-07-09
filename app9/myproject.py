import cv2
import streamlit as st
from datetime import datetime

st.title("Motion detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(1)
    
    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        now = datetime.now()
        my_day = now.strftime("%A")
        my_time = now.strftime("%H:%M:%S")
        
        cv2.putText(img=frame, text=my_day, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 100),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=my_time, org=(50, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(200, 10, 20),
                    thickness=2, lineType=cv2.LINE_AA)
        streamlit_image.image(frame)