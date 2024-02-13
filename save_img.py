from imports import *


img = cv2.imread("img/m1.png")

img_crop = img[100:400,50:600] 

cv2.imwrite("img/m1_crop.png",img_crop)