import pandas as pd
import numpy as np
from PIL import Image
import colorsys
import cv2

'''Read in image'''
im = cv2.imread('/Users/Nicki/Desktop/02_4_full copy.jpg')

'''Convert image to black/white'''
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

'''Reveal image contours'''
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(contours)

'''Draw contoured image'''
image_2 = cv2.drawContours(image, contours, -1, (0,255,0), 3)

'''Show contoured image'''
cv2.imshow('image', image_2)
cv2.waitKey(20000)
cv2.destroyAllWindows()

'''Attempt to pull color of single pixel'''
pixel = im[165,234]
print(pixel)

'''Show original image'''
cv2.imshow('image',im)
cv2.waitKey(2000)
cv2.destroyAllWindows()

'''ignore padding by 15 pixels'''

'''make list of coordinates where pixels are black'''

'''find the rgb values of those same pixels in the original photo'''
