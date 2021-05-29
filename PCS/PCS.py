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


if __name__ == "__main__" :

    cap = cv2.VideoCapture(0)

    model = cv2.CascadeClassifier('models/haarcascade_upperbody.xml') # The Classifier Model

    Found = False

    last_time = 0

    threshold = 10

    days = 15


    try: 

        parent = '/home/pi/Desktop/Recorded/'
        
        while os.listdir(parent) <= days:

            ret, image = cap.read() # Capturing the Frame

            # Condition if it captures the frame
            if ret: 
        
                if Found == False:

                    Found, image = detector(image)


                elif Found == True and time.time() - last_time > threshold:

                    last_time = time.time()

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

        print("\n\nThe Program had cought an error:\n{}\n:(".format(error))


    finally:        
    
        print("\n\nClosing the Program\n")
        
        cv2.destroyAllWindows()
        cam.release()

        print("Sucessfully Closed the Program.\n\
              Thanks for using the PSI Camera :)")