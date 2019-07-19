# Loading Video Source
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
path = 'C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\output.avi'
out = cv2.VideoWriter(path, fourcc, 20.0, (640, 480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('Grayframe', gray)
    cv2.imshow('ColorFrame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
