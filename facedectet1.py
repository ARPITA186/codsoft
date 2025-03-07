import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow
face = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
while 1:
    user=input("press Enter key to upload the picture or Type exit to stop ").strip().lower()
    if user =="exit":
        print("Bye!!!!Have a nice day!")
        break
    print("uplaod a picture for face detection:")
    uploading=files.upload()
    namefile= list(uploading.keys())[0]
    picture=cv2.imread(namefile)
    print("picture is here")
    cv2_imshow(picture)
    gray=cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(40,40))
    for (a,b,c,d) in faces:
        cv2.rectangle(picture,(a,b),(a+c,b+d),(128,0,128),2)
    print("Detection completed")
    cv2_imshow(picture)
print("program has completed")

