import cv2
import numpy as np

image = cv2.imread('img/boxes.jpg')

# blurred images
# {
# kernel_5 = np.ones((5, 5), np.float32) / 25 
# kernel_10 = np.ones((10, 10), np.float32) / 100


# blurred_image_5 = cv2.filter2D(image, -1, kernel_5)
# blurred_image_10 = cv2.filter2D(image, -1, kernel_10)

# cv2.imshow('Original Image', image)
# cv2.imshow('Blurred Image_5', blurred_image_5)
# cv2.imshow('Blurred Image_10', blurred_image_10)
# }

# kernel = np.array([[0,0,0],[1,1,1],[0,0,0]]) structure of kernel ,i.e middle row must be all 1's

# kernel of this structure of bigger size

s=15
kernel_15 = np.zeros((s,s))
kernel_15[int((s-1)/2)] = np.ones(s)

kernel_15 = kernel_15/s #because only one line is of 1's

motion_blurred = cv2.filter2D(image, -1, kernel_15)

cv2.imshow('Original Image', image)

cv2.imshow("motion blur",motion_blurred)



# motion blurring
cv2.waitKey(0)
cv2.destroyAllWindows()
