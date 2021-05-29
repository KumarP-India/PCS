#Importing Lib.(s)
import time
import os
import cv2

from datetime import datetime as dtm


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

    return obj, frame


def file_check():

    exist = False
            
    parent = '/home/pi/Desktop/Recorded/'

    dates_f = os.listdit(parent)
            
    today = str(dtm.now().day) + " of " + str(dtm.now().month) + "th"

    folder = os.path.join(parent, today)

    for i in dates_f:

        if i == today:
            exist = True

    if exist == False:

        os.mkdir(folder)

    return folder


def recorder(obj, frame):

    obj.write(frame)


cap = cv2.VideoCapture(0)

model = cv2.CascadeClassifier('models/haarcascade_upperbody.xml') # The Classifier Model

while True:

    ret, image = cap.read() # Capturing the Frame

    # Condition if it captures the frame
    if ret: 
        
        if Found == False:

            Found, frm = framedetector(image)


        elif Found == True and time.time() - last_time > threshold:

            last_time = time.time()

            fold = file_check()

            files_folder = len(os.listdir(fold)) + 1

            file = str(os.path.join(fold, files_folder)) + '.mp4'


            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(file, fourcc, 25.0, (640, 480))


        elif Found == True and time.time() - last_time <= threshold:

            recorder(out, image)

        if time.time() - last_time == threshold:

            Found = False






    if cv2.waitkey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

        break
        
    
cam.release()