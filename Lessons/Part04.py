# Image Operations
import cv2
import numpy as np

img = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\watch.jpg', 1)
px = img[55,55]
print(px)
img[55,55] = [0,0,255]
px = img[55,55]
print(px)
px = img[100:150,100:150]
print(px)
img[100:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)

watch_face = img[37:111, 107:194]
#img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
