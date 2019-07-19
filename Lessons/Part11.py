# Template Matching
import cv2
import numpy as np

img_rgb = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\template_matching.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\template.jpg',0)

w,h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)

cv2.imshow('Detected', img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Test: Use multiple templates to match a webcam feed
