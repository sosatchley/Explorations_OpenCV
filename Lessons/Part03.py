# Drawing and Writing on Image
import numpy as np
import cv2

img = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\watch.jpg', 1)

cv2.line(img, (0,0), (150, 150),(127, 241, 17), 3)
cv2.rectangle(img, (15,25), (200, 150), (0,255,0), 1)
cv2.circle(img, (100,63), 55, (255,0,0), 2)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (127,127,127), 1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
