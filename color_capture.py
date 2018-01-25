import numpy as np
import cv2
import itertools
from collections import Counter
from collections import OrderedDict
from PIL import Image
import colorsys

'''FUNCTIONS'''

'''Convert HSV to Color Name'''
def assign_color(hue):
    if hue <= 10 or (hue >= 327 and hue!= 500):
        if hue <= 10:
            color = "Red"
            est_hue = 8
        else:
            color = "Red"
            est_hue = 355
    elif hue >= 11 and hue <= 20:
        color = "Red-Orange"
        est_hue = 16
    elif hue >= 21 and hue <= 40:
        color = "Orange or Brown"
        est_hue = 31
    elif hue >= 41 and hue <= 50:
        color = "Orange-Yellow"
        est_hue = 46
    elif hue >= 51 and hue <= 60:
        color = "Yellow"
        est_hue = 56
    elif hue >= 61 and hue <= 80:
        color = "Yellow-Green"
        est_hue = 71
    elif hue >= 81 and hue <= 140:
        color = "Green"
        est_hue = 111
    elif hue >= 141 and hue <= 169:
        color = "Green-Cyan"
        est_hue = 155
    elif hue >= 170 and hue <= 200:
        color = "Cyan"
        est_hue = 185
    elif hue >= 201 and hue <= 220:
        color = "Cyan-Blue"
        est_hue = 211
    elif hue >= 221 and hue <= 240:
        color = "Blue"
        est_hue = 231
    elif hue >= 241 and hue <= 255:
        color = "Warm-Blue"
        est_hue = 248
    elif hue >= 256 and hue <= 280:
        color = "Cool-Magenta"
        est_hue = 268
    elif hue >= 281 and hue <= 320:
        color = "Magenta"
        est_hue = 300
    elif hue >= 321 and hue <= 330:
        color = "Magenta-Pink"
        est_hue = 326
    else:
        color = "Black or White"
        est_hue = 5000

    return(color, est_hue)


'''Convert rgb to hsv'''
def rgb_hsv(RGB):
    h, s, v = colorsys.rgb_to_hsv((RGB[0]/255), (RGB[1]/255), (RGB[2]/255))
    h = (h * 360)
    s = s * 100
    v = v * 100
    return (int(h),int(s),int(v))

'''Image path'''

image_path = ('/Users/Nicki/Desktop/test_images/05_7_additional.jpg')

'''Read in image with cv2'''
img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

'''Turn image into B/W to find contours'''
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)

'''Find Bounding Box'''
canny_out = cv2.Canny(threshed_img,0,img.flatten().mean())
y,x = canny_out.nonzero()
top_left = x.min(), y.min()
bottom_right = x.max(), y.max()
#print(top_left, bottom_right)

'''Establish Bounding Box Coordinates'''
x1 = top_left[0]
y1 = top_left[1]

x2 = bottom_right[0]
y2 = bottom_right[1]

top = list((x1,y1))
bottom = list((x2,y2))

'''Read in image with PIL for pixel analysis'''
im = Image.open(image_path).convert("RGB")
pix = im.load()

width = im.size[0] #define W and H
height = im.size[1]

pixels = []
image_pixels = {}

'''Dictionary of ROI pixels and values'''
for y in range(top_left[1], bottom_right[1]): #each pixel has coordinates
    row = ""
    for x in range(top_left[0], bottom_right[0]):
        RGB = pix[x, y]
        color = rgb_hsv(RGB)
        if color[2] < 80 and color[1] > 25:
            if color in image_pixels:
                image_pixels[color].append((x,y))
                #image_pixels[RGB].append((x,y))
            else:
                image_pixels[color] = [(x,y)]
                #image_pixels[RGB] = [(x,y)]
        else:
            color = (500,500,500)

'''Attempt to Sort by length of value'''
#
# pixel_list = []
# for key, value in image_pixels.items():
#     listed_values = (key, len(value))
#     pixel_list.append(listed_values)
#
# ordered_hsv_values = sorted(pixel_list, key=lambda x: x[1], reverse=False)
#
# '''Calculate overall pixels being extracted in bounding box'''
# # values = 0
# #for key in image_pixels.keys():
#     values += len(image_pixels[key])
#
# print(values)
#
# new_list = [item[0] for item in image_pixels.keys()]
#
# # trial = set(new_list)
# #
# top_colors = []
# for x in trial:
#     color, est_hue = assign_color(x)
#     top_colors.append([color,est_hue])
#
# print(top_colors)

'''Show image with generated bounding box'''
cv2.rectangle(img,top_left,bottom_right,(255,0,0))
cv2.imshow("contours", img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.destroyAllWindows()
#
# ''''Attempt to take background pixels out of dictionary.'''
# # '''Dictionary of left_background pixels and values'''
# pixels = []
# background = {}
# for x in itertools.chain(range(0,34), range(86,256)): #each pixel has coordinates
#     row = ""
#     for y in range(0,256):
#         RGB = pix[x, y]
#         color = rgb_hsv(RGB)
#         if color in background:
#             background[color].append((x,y))
#         else:
#             background[color] = [(x,y)]
# new_dict = {}
#
# '''Subtract out background'''
# for key, value in image_pixels.items():
#     if key not in background.keys():
#         new_dict[key] = value

'''Find top three colors'''
first = (0,0)
second = (0,0)
thrid = (0,0)

for key, value in image_pixels.items():
    if len(value) > first[1]:
        third = second
        second = first
        first = (key, len(value))
    elif len(value) < first[1] and len(value) > second[1]:
        third = second
        second = (key, len(value))
    elif len(value) < second[1] and len(value) > third[1]:
        third = (key, len(value))

pixel_density = [
    assign_color(first[0][0]),
    assign_color(second[0][0]),
    assign_color(third[0][0])
    ]

print(pixel_density)
colors = list(set(pixel_density))
print(colors)

'''Color Differences'''
distance = abs(colors[0][1]-colors[1][1])
print(distance)

# if distance < 75:
#     outfit_prediction = "Analogous Colors"
#     print("Approved Outfit. Your color choices are analogous." /n
#            "The top two occuring colors in your outfit are analogous to each together."
#            "Your outfit appears harmonious and is pleasing to the eye."
#            "You should flaunt your style.")
# elif distance > 180 and distance <200:
#     outfit_prediction = "Complementary Colors"
#     print("Approved Outfit. Your color choices are complementary." /n
#           "The top two occuring colors in your outfit are complementary to each other,"
#           "you have put together an appealing and eye catching outfit."
#           "You should flaunt your style.")
# elif distance > 365:
#     outfit_prediction = "Safe With Black or White"
#     print("Unapproved Outfit. Your color choices are not complementary."
#            "The algorithm doesn't believe your outfit to be pleasing to the eye."
#            "It is recommended you change your outfit before heading out; however, if
#            "you love your look: you do you!")
# else:
#     outfit_prediction = "Disharmounious Colors"
#     print("Unapproved Outfit. Your color choices are not complementary." /n
#            "The algorithm doesn't believe your outfit to be pleasing to the eye.
#            "It is recommended you change your outfit before heading out; however, if
#            "you love your look: you do you!")
#
# print(outfit_prediction)
