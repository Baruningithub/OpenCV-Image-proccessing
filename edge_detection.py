from imports import *

image = cv2.imread('img/m2.jpg',cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator for first derivative in x direction
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel operator for first derivative in y direction
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Apply Scharr operator for first derivative in x direction
scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0)

# Apply Scharr operator for first derivative in y direction
scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)

# Apply Laplacian operator (2nd derivative operation on the image)
laplacian = cv2.Laplacian(image, cv2.CV_64F)

cv2.imshow('Original Image', image)
cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)
cv2.imshow('scharr_x', scharr_x)
cv2.imshow('scharr_y', scharr_y)
cv2.imshow('laplacian', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()

