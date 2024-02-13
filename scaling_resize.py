import cv2
import numpy as np 

img = cv2.imread("img/j.png")

img_re = cv2.resize(img,(256,256))

img_50 = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2)) # 50% size

img_new = cv2.resize(img,(img.shape[1]*5,img.shape[0]*5)) 

res_lin = cv2.resize(img,None,fx=5, fy=5, interpolation = cv2.INTER_LINEAR)
res_cub = cv2.resize(img,None,fx=5, fy=5, interpolation = cv2.INTER_CUBIC)

cv2.imshow("linear",res_lin) 
cv2.imshow("cubic",res_cub) 
cv2.imshow("wo intpol",img_new)


# print(type(img))
cv2.waitKey(0)