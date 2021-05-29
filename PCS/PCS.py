#Importing Lib.(s)
import time
import os
import threading
import cv2

from datetime import datetime as dtm
from gpiozero import Buzzer as Buzz
from flask import Flask, render_template, Response
from flask_basicauth import BasicAuth

from func.py import *




# App Globals (do not edit)
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'PSK'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)


def main(cap, model, Found, last_time, threshold, days, butt):

    try: 

        parent = '/home/pi/Desktop/Recorded/'

        butt.on()
        time.sleep(sp)
        butt.off()

        time.sleep(sp)

        butt.on()
        time.sleep(sp)
        butt.off()
        
        while os.listdir(parent) <= days:

            ret, image = cap.read() # Capturing the Frame

            # Condition if it captures the frame
            if ret: 
        
                if Found == False:

                    Found, image = detector(image)


                elif Found == True and time.time() - last_time > threshold:

                    last_time = time.time()

                    butt.on()
                    time.sleep(sp)
                    butt.off()

                    print("Person Detected")

                    fold = file_check()

                    files = str(int(len(os.listdir(fold))) + 1)

                    file = str(os.path.join(fold, files)) + '.mp4'


                    fourcc = cv2.VideoWriter_fourcc(*'XVID')
                    out = cv2.VideoWriter(file, fourcc, 25.0, (640, 480))

                    print("Recording...")


                elif Found == True and time.time() - last_time <= threshold:

                    Found, image = detector(image)                    

                    recorder(out, image)

                    Found = True

                if time.time() - last_time == threshold:

                    print("Done Recording...")
                    
                    Found = False

            else:
               
               print("No Frame Captured! Re-Runing the Loop :(")

    except Exception as error:

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

        print("\n\nThe Program had cought an error:\n{}\n:(".format(error))


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











if __name__ == "__main__" :
    
    cap = cv2.VideoCapture(0)

    model = cv2.CascadeClassifier('models/haarcascade_upperbody.xml') # The Classifier Model

    Found = False

    last_time = 0

    threshold = 10

    days = 15

    butt = buzz(27)

    try:

        t = threading.Thread(target=main, args=(cap, model, Found, last_time, threshold, days, butt))
        t.daemon = True
        t.start()

        app.run(host='0.0.0.0', debug=False)




    finally:        
    
        butt.on()
        time.sleep(sp)
        butt.off()
        
        time.sleep(sp)
        
        butt.on()
        time.sleep(sp)
        butt.off()
        
        print("\n\nClosing the Program\n")
        
        cv2.destroyAllWindows()
        cam.release()

        butt.on()
        time.sleep(sp)
        butt.off()
        
        time.sleep(sp)
        
        butt.on()
        time.sleep(sp)
        butt.off()

        print("Sucessfully Closed the Program.\n\
              Thanks for using the PSI Camera :)")