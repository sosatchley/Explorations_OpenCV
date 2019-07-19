# Corner Detection
import numpy as np
import cv2

img = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\Map.png')
w,h = img.shape[:-1]
img = cv2.resize(img, (w//2, h//2))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 10, 0.01, 5)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y), 3,(255,255,255), -1)

cv2.imshow('Corner', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
