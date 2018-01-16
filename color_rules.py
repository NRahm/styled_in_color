import pandas as pd
import numpy as np
from PIL import Image
from collections import Counter
from collections import OrderedDict
import colorsys
import cv2

# image = cv2.imread('/Users/Nicki/Desktop/download.jpg')
# cv2.imshow('image', image)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
#
# cv2.cvtCol(image, COLOR_BGR2HSV)

im = Image.open('/Users/Nicki/Desktop/download.jpg')
pixels = list(im.getdata())

# print(pixels[0])
# r,g,b = pixels[0]
# print(r,g,b)
# print(colorsys.rgb_to_hsv(r,g,b))

# hsv_values = []
# for data in pixels:
#     hsv_values = colorsys.rgb_to_hsv(data[0][0][0])
#     print(np.asarray(hsv_values))
#
counter = Counter(pixels)

color_occurence = dict(counter)
# print(color_occurence)

# color_occurence_v2 = {}
# for key, value in color_occurence.items():
#     color_occurence_v2[value].append(key)
#     print(color_occurence_v2)

new_dict = {}
for key, values in color_occurence.items():
    new_dict[values] = key

ordered_pixels = list((OrderedDict(sorted(new_dict.items(),reverse=True))))

top_one = ordered_pixels[0]
top_two = ordered_pixels[1]
top_three = ordered_pixels[2]
print(new_dict[top_one],new_dict[top_two],new_dict[top_3])

# pixel_occurences = (list(color_occurence.values()))
# sorted_pixels = sorted(pixel_occurences, reverse=True)
#
#
# def change_color_numbers():
#     '''This changes the RGB values to HSV values'''
#     pass
#
# def bin_colors():
#     '''This organizes pixel concentrations into bins and prints
#        the top three most occuring colors'''
#     pass
#
# def color_mapping():
#     '''This takes in a dictionary of colors and values,
#        to be mapped against the three highest pixel color
#        concentration
# pass
