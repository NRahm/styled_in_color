import pandas as pd
import numpy as np
from PIL import Image
import colorsys
import cv2

'''Read in image'''
im = cv2.imread('/Users/Nicki/Desktop/01_1_front copy.jpg')

'''Convert image to black/white'''
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
blur = cv2.blur(thresh,(3,5))

'''Reveal image contours'''
image, contours, hierarchy = cv2.findContours(blur, cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_NONE)
# #
# # for cnt in contours:
# #     x, y, w, h = cv2.boundingRect(cnt)
# #     cv2.rectangle(im, (x,y), (x+w, y+h), (0,255,0), 2)
# for c in contours:
#     # get the bounding rect
#     x, y, w, h = cv2.boundingRect(c)
#     # draw a green rectangle to visualize the bounding rect
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

image_3 = cv2.drawContours(im, contours, -1, (255, 0, 0), 1)

# '''Not my code'''
# for c in contours:
#     # get the bounding rect
#     x, y, w, h = cv2.boundingRect(c)
#     # draw a green rectangle to visualize the bounding rect
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#     # get the min area rect
#     rect = cv2.minAreaRect(c)
#     box = cv2.boxPoints(rect)
#     # convert all coordinates floating point values to int
#     box = np.int0(box)
#     # draw a red 'nghien' rectangle
#     cv2.drawContours(image, [box], 0, (0, 0, 255))
#
#     # finally, get the min enclosing circle
#     (x, y), radius = cv2.minEnclosingCircle(c)
#     # convert all values to int
#     center = (int(x), int(y))
#     radius = int(radius)
#     # and draw the circle in blue
#     img = cv2.circle(image, center, radius, (255, 0, 0), 2)
#
# print(len(contours))

# '''Draw contoured image'''
# image_2 = cv2.drawContours(image, contours, -1, (255,255,0), 1)

# '''Show contoured image'''
# cv2.imshow('image', im)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()

# '''Attempt to pull color of single pixel'''
# pixel = im[165,234]
# print(pixel)

'''Show original image'''
cv2.imshow('image',im)
cv2.waitKey(50000)
cv2.destroyAllWindows()

# # '''Find upper left pixel location'''
# # for data in contours:
# #     upper_coord = ()
# #     for x, y in data:
# #         if x > 15 and y > 15:
# #             upper_coord = min(x,y)
#
# '''Find lower right pixel location'''
# for data in contours:
#     lower_coord = max(data)
#
#
# print('upper_coord', upper_coord)
#print('lower_coord', lower_coord)

# '''ignore padding by 15 pixels'''
#
# '''make list of coordinates where pixels are black'''
#
# '''find the rgb values of those same pixels in the original photo'''
