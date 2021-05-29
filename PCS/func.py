#Importing Lib.(s)
import time
import os
#import threading
import cv2

from datetime import datetime as dtm
from gpiozero import Buzzer as Buzz
#from flask import Flask, render_template, Response
#from flask_basicauth import BasicAuth

def detector(frame):
        
    g_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converting the frame to Greyscale

    detection = model.detectMultiScale(g_frame, 1.3, 5) # Running the Classifier with g_frame as input (see its assignment above)

        
    try:

        found = detection.shape[0]

    else:

        found = 0

    for (x, y, w, h) in detection:
        
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)    

    if found > 0:
        obj = True
     
    elif found == 0:
        obj = False

    return obj, frame


def file_check():

    exist = False
            
    parent = '/home/pi/Desktop/Recorded/'

    dates_f = os.listdit(parent)
            
    today = str(dtm.now().day) + ' of ' + str(dtm.now().month) + 'th'

    folder = os.path.join(parent, today)

    for i in dates_f:

        if i == today:
            exist = True

    if exist == False:

        os.mkdir(folder)

    return folder


def recorder(obj, frame):

    obj.write(frame)

def space_protocol():

    parent = '/home/pi/Desktop/Recorded/'

    folders = os.listdir(parent)
    
    for i in folders:
    
        shutil.rmtree(i)

    print("Space-Protocol Sucessfully ran :)")


if __name__ == "__main__":

    print("THIS NOT THE MAIN PROGRAM TO RUN")
