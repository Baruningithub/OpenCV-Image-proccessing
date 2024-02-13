from imports import *

image = cv2.imread('img/rgb.jpg')

cols,rows = image.shape[:2]

src_pts = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1],[cols-1,rows-1]])

dst_pts = np.float32([[0, 0], [cols-1,0], [int(0.33*cols),rows-1], [int(0.8*cols),rows-1]])

M = cv2.getPerspectiveTransform(src_pts, dst_pts)

projected_image = cv2.warpPerspective(image, M, (300, 300)) 

cv2.imshow('Original Image', image)
cv2.imshow('Projected Image', projected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
