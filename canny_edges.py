from imports import *

image = cv2.imread('img/m2.jpg',cv2.IMREAD_GRAYSCALE)

gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

canny_edges = cv2.Canny(gaussian_blur, 50, 150)  # thresholds


cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', canny_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

