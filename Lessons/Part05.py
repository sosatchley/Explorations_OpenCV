# Image Arithmatics and Logic
import cv2
import numpy as np

# 600 x 480
img1 = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\Volcano_Night.jpg')
img2 = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\Volcano_Day.jpg')

add = img2+img1
betterAdd = cv2.add(img1,img2)
weighted = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

cv2.imshow('Day', img2)
cv2.imshow('Night', img1)
#cv2.imshow('add', add)
cv2.imshow('Better Add', betterAdd)
cv2.imshow('Weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

#------------------------------
# Load images
img1 = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\Volcano_Day.jpg')
img2 = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\mainlogo.png')

cv2.imshow('Image 1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Create ROI in img1 same size as img2
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# convert img2 to gray (Mask of img2, inverse of mask)
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

# Black-out area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only logo region from logo image
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('original', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('mask', img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('threshold', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('inverted', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Blackout', img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Logo no BG', img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
