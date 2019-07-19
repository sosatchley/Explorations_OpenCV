# Loading Images
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('C:\\Users\\Shane\\Documents\\Repos\\Explorations_OpenCV\\Resources\\watch.jpg', 0)
cv2.imshow('Watch', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img, cmap = 'gray', interpolation = "bicubic")
plt.xticks([]), plt.yticks([])
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
