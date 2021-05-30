'''
    This Code is created by Prabhas Kumar on 30th may'21 @ 14.15

    This is the part of project <PCS>.

    It is main Multi-threaded Program of <PCS>!

    The Program for transfer to RPi 4(or similar) and programs for applying 
    deep learning or better computer vision and saving there are as R&D for Future! 

    The Source(s) is/are - https://youtu.be/Z1RJmh_OqeA; https://bit.ly/3i299ro;
                           https://bit.ly/3wHr0rH; https://bit.ly/3vzUQhD; 
                           https://bit.ly/34t4tmD; https://bit.ly/2SH4Lnj

    Note - The Source(s) is/are collection of all used in this project!

    Name of program - PCS.py

'''

#Importing Lib.(s)
import time
import os
import cv2 # Open-CV

from datetime import datetime as dtm
from gpiozero import Buzzer as Buzz # Buzzer




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






# Check if it ran as independent program
if __name__ == "__main__" :
    
    cap = cv2.VideoCapture(0) # Defining and opening Camera object

    model = cv2.CascadeClassifier('models/haarcascade_upperbody.xml') # The Classifier Model

    # Var.(s)
    Found = False

    last_time = 0

    threshold = 10 # The Sec.(s) of Recorded Videos

    days = 15 # No. of days to keep

    butt = buzz(27) # Buzzer

  
    try: 

        parent = '/home/pi/Desktop/Recorded/' # The Path

        # Buzzer
        butt.on()
        time.sleep(sp)
        butt.off()

        time.sleep(sp)

        butt.on()
        time.sleep(sp)
        butt.off()
        


        while os.listdir(parent) <= days: # If it is between the Storage Time

            ret, image = cap.read() # Capturing the Frame



            # Condition if it captures the frame
            if ret: 
        
                # If it doesn't found the object
                if Found == False:

                    Found, image = detector(image) # Running the model-Function


                
                # If it Founds the Object and not recodrding
                elif Found == True and time.time() - last_time > threshold:

                    last_time = time.time() # registering the time


                    # Buzzer
                    butt.on()
                    time.sleep(sp)
                    butt.off()



                    print("Person Detected") # Printing the statemet

                    fold = file_check() # Runninf the Folder-Path Protocol

                    files = str(int(len(os.listdir(fold))) + 1) # The Vidio-File no.

                    file = str(os.path.join(fold, files)) + '.mp4' # The Video-File name


                    # Creating Recrding File Object
                    fourcc = cv2.VideoWriter_fourcc(*'XVID')
                    out = cv2.VideoWriter(file, fourcc, 25.0, (640, 480))



                    print("Recording...") # Printing the Statement


                
                # If it's in the recording phase
                if Found == True and time.time() - last_time <= threshold:

                    Found, image = detector(image) # Running Model-Protocol                    

                    recorder(out, image) # Running REcording Protocol

                    Found = True # Chaning the Boolean value, if it changed by Model-Protocol



                # If it's recording Phase just ended
                if time.time() - last_time == threshold:

                    print("Done Recording...") # Printing the Statement
                    
                    Found = False # Changing the Var. for the same




            # If no Frame Captured
            else:
               
               print("No Frame Captured! Re-Runing the Loop :(") # Printing the Statement



    
    # Handling any error occoured in this
    except Exception as error:

        # Buzzer
        butt.on()
        time.sleep(sp)
        butt.off()
        
        time.sleep(sp)

        butt.on()
        time.sleep(sp)
        butt.off()
        
        time.sleep(sp)

        butt.on()
        time.sleep(sp)
        butt.off()


        print("\n\nThe Program had cought an error:\n{}\n:(".format(error)) # Printing the Statement




    finally:        
    
        
        # Buzzer
        butt.on()
        time.sleep(sp)
        butt.off()
        
        time.sleep(sp)
        
        butt.on()
        time.sleep(sp)
        butt.off()
        
        
        
        print("\n\nClosing the Program\n")  # Printing the Statement
        
        
        # Closing the Camera!
        cv2.destroyAllWindows()
        cam.release()

        
        # Buzzer
        butt.on()
        time.sleep(sp)
        butt.off()
        
        time.sleep(sp)
        
        butt.on()
        time.sleep(sp)
        butt.off()

        
        
         # Printing the Statement
        print("Sucessfully Closed the Program.\n\
              Thanks for using the PSI Camera :)")


'''
The End :)
'''