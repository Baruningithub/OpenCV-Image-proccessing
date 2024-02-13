from imports import *

image = cv2.imread('img/flip.webp')

blur = cv2.blur(image, (5, 5))

box_filtered = cv2.boxFilter(image, -1, (5, 5))

gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)

bilateral_filtered = cv2.bilateralFilter(image, 9, 75, 75)

median_blur = cv2.medianBlur(image, 9)

cv2.imshow('Original Image', image)
cv2.imshow('Blur', blur)
cv2.imshow('Box Filter', box_filtered)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Bilateral Filter', bilateral_filtered)
cv2.imshow('Median Blur', median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
