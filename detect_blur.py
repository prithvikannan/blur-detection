import cv2
import os

THRESHOLD = 110

directory = 'images'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        path = os.path.join(directory, filename)
        print(path)
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        score = cv2.Laplacian(image, cv2.CV_64F).var()
        if score > THRESHOLD:
            print "Not Blur"
        else:
            print "Blur"
        continue
    else:
        continue



    # to run: python detect_blur.py --images images