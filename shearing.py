from imports import *

image = cv2.imread('img/rgb.jpg')


# with shear_factor
## 

# shear_factor = 0.1 
# rows, cols = image.shape[:2]

# M = np.float32([[1, shear_factor, 0],  [0, 1, 0]])

# sheared_image = cv2.warpAffine(image, M, (cols, rows))

##

# with 3 source and desination points

rows, cols = image.shape[:2]

src_pts = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
dst_pts = np.float32([[0, 0], [int(0.8 * (cols - 1)), 0], [int(0.4 * (cols - 1)), rows - 1]])

M = cv2.getAffineTransform(src_pts, dst_pts)

sheared_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('Original Image', image)
cv2.imshow('Sheared Image', sheared_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
