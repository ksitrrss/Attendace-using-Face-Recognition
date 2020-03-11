# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np
import time
import datetime



# Create Local Binary Patterns Histograms for face recognization
#recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_alt2.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

f=open("Database.txt", 'a')
f.write("\nDATE \t TIME \t \t \t TEACHER NAME \t \t STUDENT NAME\n ")
print('Executing the script')
f.close()

# Local variable Declaration
lecture=0
count1=0
count2=0
count3=0
count4=0
sample=0
take=1
# Loop
while True:

     
    now = datetime.datetime.now()

    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id,i= recognizer.predict(gray[y:y+h,x:x+w])

        print(i)
        print(Id)

        if i < 65:
            sample=sample+1                         
            # Check the ID if exist 
            if(Id == 1 and take ):
                take =0
                count1=1
                Id = "ROH-NI"
                print('Take Attendance ')
                lecture=1
##                sample =0
                time.sleep(10)
            #If not exist, then it is Unknown
            elif(Id == 2):
                count4=1
                Id = "sagar"
                Id1=Id
            elif(Id == 3):
                count3=1
                Id = "uday"
                Id2=Id
        else:
                print(Id)
                Id = "suhil"
                

        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    if lecture == 1 or lecture == 2 or lecture == 3:

        if sample > 50:
            sample =0

            f=open("Database.txt", 'a')
            if lecture == 1 and count4 == 1 :
                f.write(str(now)+'\t'+"prajwal"+'\t' +str(count4)+'\t'+str(Id)+'\n')
            if lecture == 1 and count3 == 1 :
                f.write(str(now)+'\t'+"prajwal"+'\t' +str(count3)+'\t'+str(Id2)+'\n')
##            if lecture == 1 and count4 == 1 :
##                f.write(str(now)+'\t'+"prabhu"+'\t' +str(count4)+'\t'+str(Id1)+'\n')

            f.close()
            break
                            
# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
