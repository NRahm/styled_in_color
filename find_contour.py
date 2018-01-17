import pandas as pd
import numpy as np
from PIL import Image
import colorsys
import cv2

im = cv2.imread('/Users/Nicki/Desktop/01_1_front copy.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print(contours)

image_2 = cv2.drawContours(image, contours, -1, (0,255,0), 3)

cv2.imshow('image', image_2)
cv2.waitKey(2000)
cv2.destroyAllWindows()
