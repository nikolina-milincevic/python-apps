# The app detects moving objects in an image
# This app is not very precise when considering recognision of seperate objects,
# but it determines well, when the object is in the picture - important part

import cv2
import time
from emailing import send_email

video = cv2.VideoCapture(1)

time.sleep(1)

first_frame = None

while True:
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame_gaussian = cv2.GaussianBlur(grey_frame, (21, 21), 0)
    # This gives grey colour and a blur (noise)
    
    if first_frame is None:
        first_frame = grey_frame_gaussian
    
    delta_frame = cv2.absdiff(first_frame, grey_frame_gaussian)
    # This gives the difference between the current grey frame and the first frame
    
    thresh_frame = cv2.threshold(delta_frame, 70, 255, cv2.THRESH_BINARY)[1]
    # This categorises colour - if a cell has value of 70 or above, 
    # it will be categorised as white 255. The last arg is an algorithm.
    # We may need to change the value 70 - depends on the light in the room.
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # Dilation increases the object area, is used to accentuate features
    
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        # If it is a false object, continue 
        # We can play with that number
        x, y, w, h = cv2.boundingRect(contour)
        # x and y are coordinates of lower left corner
        # w and h are width and height
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            send_email()
        
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        break

video.release()