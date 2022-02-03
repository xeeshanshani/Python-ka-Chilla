# import libraries
import cv2 as cv
import numpy as np

img = cv.imread('stamp.png')

cv.imshow('Original', img)
cv.waitKey(0)   
cv.destroyAllWindows()
#py -m pip --upgrade  opencv-python
#py -m pip install opencv-python
