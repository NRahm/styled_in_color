import cv2
import numpy as np
from collections import Counter
from PIL import Image

'''Read in and scale down image'''
img = cv2.pyrDown(cv2.imread('/Users/Nicki/Desktop/test_images/02_7_additional.jpg', cv2.IMREAD_UNCHANGED))
shape = img.shape
print(shape)

'''Turn image into B/W to find contours'''
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)
#blur = cv2.blur(threshed_img,(1,1))

'''Find Bounding Box'''
canny_out = cv2.Canny(threshed_img,0,img.flatten().mean())
y,x = canny_out.nonzero()
top_left = x.min(), y.min()
bottom_right = x.max(), y.max()
print(top_left, bottom_right)


'''Establish Bounding Box Coordinates'''
x1 = top_left[0]
y1 = top_left[1]

x2 = bottom_right[0]
y2 = bottom_right[1]

'''Show image with generated bounding box'''
cv2.rectangle(img,top_left,bottom_right,(0,0,255))
cv2.imshow("contours", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

cv2.destroyAllWindows()

'''Load image'''
im = Image.open('/Users/Nicki/Desktop/test_images/02_7_additional.jpg')

'''Pull rgb values for all pixels in image'''
pixels = list(im.getdata())

size = im.size

width = size[0]
height = size[1]

person = img[x1:x2, y1:y2]

ans = []
for y in range(y1, y2):  #looping through each rows
    for x in range(x1, x2): #looping through each column
        ans.append([x, y])

print(len(ans))


#area_of_interest = img[top_left[0]:bottom_right[0],top_left[1]:bottom_right[1]]
# '''background = Needs to be written'''
#
# '''Not my code'''
# mask = np.zeros(img.shape[:2],np.uint8)
# background = np.zeros((1,65),np.float64)
# foreground = np.zeros((1,65),np.float64)
# rect = (x1, y1, x2, y2)
# cv2.grabCut(img, mask, rect, background, foreground, 5, cv2.GC_INIT_WITH_RECT)
# new_mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# cropped_image = img*new_mask[:,:,np.newaxis]
# #
#
# '''Next steps: grab & save cropped_image, grab & save left & right backgrounds'''
# '''Bin HSV into 12 colors from 24, write euclidean distance metrics'''


# new_list = []
# for i in hsv_pixels:
#     for j in i:
#         new_list.append(j)
#
# final_list = [list(i) for i in new_list]
#
# counter = Counter(final_list)
#
# '''Count occurences of each rgb  value'''
# counter = Counter(pixels)
#
# '''Turn rgb counts into dictionary'''
# color_occurence = dict(counter)
# # print(color_occurence)
#
# # color_occurence_v2 = {}
# # for key, value in color_occurence.items():
# #     color_occurence_v2[value].append(key)
# #     print(color_occurence_v2)
#
# '''Reverse key, value pairs in color occurence dictionary,
#    so that key = number of occurences and value = rgb value'''
# new_dict = {}
# for key, values in color_occurence.items():
#     new_dict[values] = key
#
#
# '''Order dictionary in order of highest appearing color to least frequent color'''
# ordered_pixels = list((OrderedDict(sorted(new_dict.items(),reverse=True))))
#
# '''Assign top three colors to variables'''
# top_one = ordered_pixels[0]
# top_two = ordered_pixels[1]
# top_three = ordered_pixels[2]
# # print(new_dict[top_one],new_dict[top_two],new_dict[top_three])
#
# '''Reveal rgb values for top three colors'''
# one_rgb = new_dict[top_one]
# two_rgb = new_dict[top_two]
# three_rgb = new_dict[top_three]
#
#
# '''Convert top three colors to HSV'''
# color_one = colorsys.bgr_to_hsv(one_rgb[0],one_rgb[1],one_rgb[2])
# color_two = colorsys.bgr_to_hsv(two_rgb[0],two_rgb[1],two_rgb[2])
# color_three = colorsys.bgr_to_hsv(three_rgb[0],three_rgb[1],three_rgb[2])
#
# print(color_one, color_two, color_three)
#
#cv2.rectangle(cropped_image,top_left,bottom_right,(0,0,255))
# cv2.imshow("contours", cropped_image)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()

# '''Count occurences of each hsv value'''
# counter = Counter(list(hsv_pixels))
#
# '''Turn hsv counts into dictionary'''
# color_occurence = dict(counter)
#
# '''Reverse key, value pairs in color occurence dictionary,
#    so that key = number of occurences and value = rgb value'''
# new_dict = {}
# for key, values in color_occurence.items():
#     new_dict[values] = key
#
# '''Order dictionary in order of highest appearing color to least frequent color'''
# ordered_pixels = list((OrderedDict(sorted(new_dict.items(),reverse=True))))
#
# '''Assign top three colors to variables'''
# top_one = ordered_pixels[0]
# top_two = ordered_pixels[1]
# top_three = ordered_pixels[2]
#
# print(top_one,top_two,top_three)


# #
# ans = np.array(ans)
# print(ans)

# '''Convert colors from BGR to HSV'''
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# for x in hsv:
#     hsv_pixels = []
#     hsv_pixels.append(x)
#
# new_list = []
# for i in hsv_pixels:
#     for j in i:
#         new_list.append(list(j))
#
# final_list = [list(i) for i in new_list]
# print(final_list)
# Counter(final_list)
