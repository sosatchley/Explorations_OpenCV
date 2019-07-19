# Blurring and Smoothing
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100,80,50])
    upper_blue = np.array([135,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    # Averaging
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)

    # Gaussian Blurring
    blur = cv2.GaussianBlur(res,(15,15),0)

    # Median Blur
    median = cv2.medianBlur(res,15)

    # Bilateral Blur
    bilateral = cv2.bilateralFilter(res,15,75,75)

    cv2.imshow('original',frame)
    cv2.imshow('Unblurred', res)
    cv2.imshow('Averaging', smoothed)
    cv2.imshow('Gaussian Blurring', blur)
    cv2.imshow('Median Blurring', median)
    cv2.imshow('Bilateral Blurring', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
