import cv2
import numpy as np 

img = cv2.imread("img/rgb.jpg")

 
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert to gray scale
cv2.imwrite("img/rgb_bw.jpg",img_gray)
# cv2.imshow("window",img_gray)

# img[:,:,2]=0 # removing red
# img[:,:,0]=0 # removing blue

# imgBlue = img[:,:,0]
# imgGreen = img[:,:,1]
# imgRed  = img[:,:,2]

# cv2.imshow("window",img) 

# m_img = np.hstack((imgBlue,imgGreen,imgRed))
# cv2.imshow("window1",m_img)


# print(img.shape)
# cv2.waitKey(0)
