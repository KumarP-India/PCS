'''
See PCS.py for details! 
'''

#Importing Lib.(s)

import time
import os
#import threading
import cv2

from datetime import datetime as dtm
from gpiozero import Buzzer as Buzz
#from flask import Flask, render_template, Response
#from flask_basicauth import BasicAuth



# The Classification Function
def detector(frame):
        
    g_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converting the frame to Greyscale

    detection = model.detectMultiScale(g_frame, 1.3, 5) # Running the Classifier with g_frame as input (see its assignment above)

        
    try:

        found = detection.shape[0] # Finding the no. of detected objects, if any

    else:

        found = 0 # If it detected none

    
    # Putting the Rectangle aroung detected object(s)
    for (x, y, w, h) in detection: # The dimensions
        
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2) # The Recangle putting in frame   


    # The boolean var. to set to true if it detected the object otherwise false
    if found > 0:
        obj = True 
     

    elif found == 0:
        obj = False


    return obj, frame # Returning boolean var of detected object and Edited frame




# The Folder-Path Protocol
def file_check():

    exist = False # Boolean Var. for existing folder of todays' date
            
    parent = '/home/pi/Desktop/Recorded/' # The path!

    dates_f = os.listdit(parent) # Listing all of the folders in Parent path
            
    today = str(dtm.now().day) + ' of ' + str(dtm.now().month) + 'th' # The todays' Folder name

    folder = os.path.join(parent, today) # # The todays' Folder path



    # Checing if todays' folder exists
    for i in dates_f:

        # If it founds today's name folder it returns exists var to true
        if i == today:
            exist = True



    # If above doesnot founf it then it create it
    if exist == False:

        os.mkdir(folder)



    return folder # returning the path to todays' folder




# The recording Protocol
def recorder(obj, frame):

    obj.write(frame) # Writing the Frame to Videofile




# The Space - Cleaning protocol
def space_protocol():

    parent = '/home/pi/Desktop/Recorded/' # The Parent path

    folders = os.listdir(parent) # Listing the existing Folders


    
    # Loopinf over all of the Folders in Parent path
    for i in folders:
    
        shutil.rmtree(i) # Removing the Non-Empty Folders from Path



    print("Space-Protocol Sucessfully ran :)") # Print statement





# To ensure it doesn't run independently
if __name__ == "__main__":

    raise RuntimeError("\n\nTHIS NOT THE MAIN PROGRAM TO RUN\n\n") # Then Raising the Error with warning    

'''
The End :)
'''