from imports import *

img = cv2.imread("img/flip.webp")

im_flip_v= cv2.flip(img , 0)
im_flip_h= cv2.flip(img , 1)
im_flip_m= cv2.flip(img , -1)

m_img = np.hstack((im_flip_h,im_flip_v,im_flip_m))

cv2.imshow("window",img)

cv2.imshow("window1",m_img)

cv2.waitKey(0)