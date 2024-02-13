from imports import *

img = cv2.imread("img/m1.png")

img_crop = img[100:400,50:600] # [height_slice,width_slice]


print(img.shape)
print(img_crop.shape)

cv2.imshow("window1",img_crop)
cv2.imshow("window",img)


cv2.waitKey(0)

