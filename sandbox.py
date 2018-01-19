import cv2
import numpy as np

# read and scale down image
img = cv2.pyrDown(cv2.imread('/Users/Nicki/Desktop/01_1_front copy.jpg', cv2.IMREAD_UNCHANGED))

# threshold image
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)
blur = cv2.blur(threshed_img,(1,1))


#HERE!!!#
canny_out = cv2.Canny(threshed_img,0,img.flatten().mean())
y,x = canny_out.nonzero()
top_left = x.min(), y.min()
bot_right = x.max(), y.max()
print(top_left, bot_right)

# # find contours and get the external one
# image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,
#                 cv2.CHAIN_APPROX_SIMPLE)


# top_left1 = x1.min(), y1.min()
# bot_right1 = x1.max(), y1.max()
# print(top_left1, bot_right1)
# display masked image

# # find contours and get the external one
# image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,
#                 cv2.CHAIN_APPROX_SIMPLE)

cv2.rectangle(img,(36, 0),(96, 123),(0,0,255))
cv2.imshow("contours", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

cv2.destroyAllWindows()
