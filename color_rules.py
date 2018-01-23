import pandas as pd
import numpy as np
from PIL import Image
from collections import Counter
from collections import OrderedDict
import colorsys
import cv2


'''Load image PIL'''
im = Image.open('/Users/Nicki/Desktop/01_1_front copy.jpg')
width, height = im.size
print(width,height)
# hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
#
#
# for x in hsv:
#     hsv_pixels = []
#     hsv_pixels.append(x)
#
#
# new_list = []
# for i in hsv_pixels:
#     for j in i:
#         new_list.append(j)
#
# final_list = [list(i) for i in new_list]

'''Pull rgb values for all pixels in image'''
pixels = list(im.getdata())
#
# # for x in pixels:
# #     hsv_pixels = []
# #     hsv_pixels.append(cv2.cvtColor(x, cv2.COLOR_BGR2HSV))
# # print(hsv_pixels)
#
# hsv_values = []
# for data in pixels:
#     hsv_values = cv2.COLOR_BGR2HSV(data[0][0][0])
#     print(np.asarray(hsv_values))

# '''Convert to HSV'''
# for item in pixels:
#     pixels_hsv = []
#     hsv_value = cv2.COLOR_BGR2HSV(item)
#     pixels_hsv.append(hsv_value)

'''Count occurences of each rgb  value'''
counter = Counter(pixels)

'''Turn rgb counts into dictionary'''
color_occurence = dict(counter)

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

'''Reveal rgb values for top three colors, NEEDS TO BE WRITTEN
   one = purple, two = lime green, three = hot pink
'''
one_rgb = (153,50,204)
# one_bgr = one_rgb[::-1]
two_rgb = (0,255,0)
# two_bgr = two_rgb[::-1]
three_rgb = (255,20,147)
# three_bgr = three_rgb[::-1]

'''Doesn't seem like I need to normalize'''
# def normalize_rgb(color):
#     normal_num = []
#     for item in color:
#         normal_num.append(item/255)
#
# '''These are RGB values!! Convert top three colors to HSV'''
# color_one = colorsys.rgb_to_hsv((one_rgb[0]/255),(one_rgb[1]/255),(one_rgb[2]/255))
# color_two = colorsys.rgb_to_hsv((two_rgb[0]/255),(two_rgb[1]/255),(two_rgb[2]/255))
# color_three = colorsys.rgb_to_hsv((three_rgb[0]/255),(three_rgb[1]/255),(three_rgb[2]/255))
# print(color_one, color_two, color_three)


'''Changing RGB to HSV line by line'''
def rgb_hsv(RGB):
    r, g, b = RGB[0], RGB[1], RGB[2]
    lowest = min(r,g,b)
    highest = max(r,g,b)
    v = highest
    delta = highest - lowest

    if highest:
        s = delta / highest
    if r == highest:
        h = 60*((g-b)/delta)
    elif g == highest:
        h = 60*(((b-r) / delta)+2)
    else:
        h = 60*(((r-g) / delta)+4)

    if h < 0:
        h = h +360
    else:
        h = h

    return(hsv)

'''16 color bins, need to write in black & white'''
def assign_color(hue):
    if hue <=10 or hue == 355:
        color = "Red"
    if hue >= 11 and hue <= 20:
        color = "Red-Orange"
    if hue >= 21 and hue <= 40:
        color = "Orange or Brown"
    if hue >= 41 and hue <= 50:
        color = "Orange-Yellow"
    if hue >= 51 and hue <= 60:
        color = "Yellow"
    if hue >= 61 and hue <= 80:
        color = "Yellow-Green"
    if hue >= 81 and hue <= 140:
        color = "Green"
    if hue >= 141 and hue <= 169:
        color = "Green-Cyan"
    if hue >= 170 and hue <= 200:
        color = "Cyan"
    if hue >= 201 and hue <= 220:
        color = "Cyan-Blue"
    if hue >= 221 and hue <= 240:
        color = "Blue"
    if hue >= 241 and hue <= 280:
        color = "Blue-Magenta"
    if hue >= 281 and hue <= 320:
        color = "Magenta"
    if hue >= 321 and hue <= 330:
        color = "Magenta-Pink"
    if hue >= 331 and hue <= 354:
        color = "black or white"

    return color
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
