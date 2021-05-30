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
import threading
import cv2 # Open-CV

from datetime import datetime as dtm
from gpiozero import Buzzer as Buzz # Buzzer

# Flask
from flask import Flask, render_template, Response
from flask_basicauth import BasicAuth

from func.py import * # The Function Module




# App Globals
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'PSK' # Web - Username
app.config['BASIC_AUTH_PASSWORD'] = 'password' # Web - Password
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)




# Main-Function
def main(cap, model, Found, last_time, threshold, days, butt):

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



# Web-App Defings

@app.route('/')
@basic_auth.required
def index():

    return render_template('index.html')



def gen(frm):
    while True:
        ret, img = cv2.imencode('.png', frm)
        
        if ret:
            
            frame = img.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(gen(detector(cv2.VideoCapture(0).read()[1])[1]),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





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

        # Running Main-Function on saperate Thread
        t = threading.Thread(target=main, args=(cap, model, Found, last_time, threshold, days, butt))
        t.daemon = True
        t.start()


        # Running the Web-App on this Thread
        app.run(host='0.0.0.0', debug=False)



    # Closing Program Protocol
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