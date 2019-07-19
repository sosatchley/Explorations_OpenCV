# Feature Matching (Homography) Brute Force
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\Feature.jpg')
img1 = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\FeatureMatch_Bright.jpg')
img2 = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\FeatureMatch_Dark.jpg')

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches,key = lambda x:x.distance)

img3 = cv2.drawMatches(img, kp1, img2, kp2, matches[:5], None, flags = 2)
plt.imshow(img3)
plt.show()

# Test: Use Homography and edge detection to highlight a detected object in
#   photo or webcam feed
