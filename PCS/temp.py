import time
import os
import cv2 # Open-CV
import shutil # For Space-Protocol

from datetime import datetime as dtm
from gpiozero import Buzzer as buzz # Buzzer



# The Folder-Path Protocol
def file_check():

    exist = False # Boolean Var. for existing folder of todays' date
            
    parent = '/home/pi/Desktop/Recorded/' # The path!

    dates_f = os.listdir(parent) # Listing all of the folders in Parent path
            
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
    
        shutil.rmtree(os.path.join(parent, i)) # Removing the Non-Empty Folders from Path



    print("Space-Protocol Sucessfully ran :)") # Print statement






# Check if it ran as independent program
if __name__ == "__main__" :
    
    cap = cv2.VideoCapture(0) # Defining and opening Camera object

    # Var.(s)
    Found = False

    last_time = 0

    threshold = 180 # The Sec.(s) of Recorded Videos

    days = 14 # No. of days to keep

    butt = buzz(27) # Buzzer

    sp = 0.125 # Sleep for Buzzer

  
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
        
        while True:

            while len(os.listdir(parent)) <= days: # If it is between the Storage Time

                ret, image = cap.read() # Capturing the Frame



                # Condition if it captures the frame
                if ret: 

                    image = cv2.rotate(image, cv2.ROTATE_180)

                    if time.time() - last_time >= threshold:

                        last_time = time.time()
                        
                        fold = file_check()

                        files = str(int(len(os.listdir(fold))) + 1) # The Vidio-File no.

                        file = str(os.path.join(fold, files)) + '.wmv' # The Video-File name

                        fourcc = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
                        out = cv2.VideoWriter(file, fourcc, 25.0, (640, 480))

                        print("Recording...") # Printing the Statement

                        recorder(out, image)

                    elif time.time() - last_time < threshold:

                        recorder(out, image)

                    cv2.imshow("PCS - Feed", image)
                    if cv2.waitKey(1) and ord('q'):
                        raise RuntimeError("Closed the PCS!")
            


            space_protocol()



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
        cap.release()

        
        # Buzzer
        butt.on()
        time.sleep(sp)
        butt.off()
        
        time.sleep(sp)
        
        butt.on()
        time.sleep(sp)
        butt.off()

        
        
         # Printing the Statement
        print("Sucessfully Closed the Program.\n",
              "Thanks for using the PCS:)")


'''
The End :)
'''