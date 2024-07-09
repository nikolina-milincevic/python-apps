# The app detects moving objects in an image
# This app is not very precise when considering recognision of seperate objects,
# but it determines well, when the object is in the picture - important part

import cv2
import time
import glob
import os
from emailing import send_email
from threading import Thread

video = cv2.VideoCapture(1)

time.sleep(1)

first_frame = None
status_list = []
count = 1


def clean_folder():
    print("clean_folder function started")
    images = glob.glob("app9/images/*.png")
    for image in images:
        os.remove(image)
    print("clean_folder function ended")


while True:
    status = 0
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame_gaussian = cv2.GaussianBlur(grey_frame, (21, 21), 0)
    
    if first_frame is None:
        first_frame = grey_frame_gaussian
    
    delta_frame = cv2.absdiff(first_frame, grey_frame_gaussian)
    
    thresh_frame = cv2.threshold(delta_frame, 70, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        if rectangle.any():
            status = 1
            if count < 10:
                cv2.imwrite(f"app9/images/0{count}.png", frame)
            else:
                cv2.imwrite(f"app9/images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("app9/images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = sorted(all_images)[index]            
            
    status_list.append(status)
    status_list = status_list[-2:]
    
    if status_list[0] == 1 and status_list[1] == 0:
        # The following rows are executed in the background while frames
        # are being shown in the video
        email_thread = Thread(target=send_email, args=(image_with_object, ))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True
        
        email_thread.start()
        
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        break

video.release()
clean_thread.start()