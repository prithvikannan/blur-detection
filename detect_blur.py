import cv2
threshold = 110
image = cv2.imread('images/image_005.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
score = cv2.Laplacian(image, cv2.CV_64F).var()

if score > threshold:
    print "Not Blur"
else:
    print "Blur"