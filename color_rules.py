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

'''Load image'''
im = Image.open('/Users/Nicki/Desktop/01_1_front copy.jpg')
hsv_image = cv2.cvtCol(im, COLOR_BGR2HSV)

'''Pull rgb values for all pixels in image'''
pixels = list(im.getdata())
print(pixels)

# hsv_values = []
# for data in pixels:
#     hsv_values = colorsys.rgb_to_hsv(data[0][0][0])
#     print(np.asarray(hsv_values))
#
'''Count occurences of each rgb  value'''
counter = Counter(pixels)

'''Turn rgb counts into dictionary'''
color_occurence = dict(counter)
# print(color_occurence)

# color_occurence_v2 = {}
# for key, value in color_occurence.items():
#     color_occurence_v2[value].append(key)
#     print(color_occurence_v2)

'''Reverse key, value pairs in color occurence dictionary,
   so that key = number of occurences and value = rgb value'''
new_dict = {}
for key, values in color_occurence.items():
    new_dict[values] = key


'''Order dictionary in order of highest appearing color to least frequent color'''
ordered_pixels = list((OrderedDict(sorted(new_dict.items(),reverse=True))))

'''Assign top three colors to variables'''
top_one = ordered_pixels[0]
top_two = ordered_pixels[1]
top_three = ordered_pixels[2]
# print(new_dict[top_one],new_dict[top_two],new_dict[top_three])

'''Reveal rgb values for top three colors'''
one_rgb = new_dict[top_one]
two_rgb = new_dict[top_two]
three_rgb = new_dict[top_three]


'''Convert top three colors to HSV'''
color_one = colorsys.rgb_to_hsv(one_rgb[0],one_rgb[1],one_rgb[2])
color_two = colorsys.rgb_to_hsv(two_rgb[0],two_rgb[1],two_rgb[2])
color_three = colorsys.rgb_to_hsv(three_rgb[0],three_rgb[1],three_rgb[2])

print(color_one, color_two, color_three)


# '''Assign red, green, blue values'''
# r,g,b = pixels[0]
#
# '''Convert rgb to hsv'''
# h,s,v = colorsys.rgb_to_hsv(r,g,b)
# print(h,s,v)

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
