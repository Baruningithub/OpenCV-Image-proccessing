from imports import *

img = cv2.imread("img/rgb.jpg")

height,width = img.shape[:2]

mat = cv2.getRotationMatrix2D(center=(width//2,height//2),angle=15,scale=1)

img_r = cv2.warpAffine(img, mat, (width,height))

cv2.imshow('Original Image', img)
cv2.imshow("rotated img",img_r)
cv2.waitKey(0)
cv2.destroyAllWindows()