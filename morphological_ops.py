from imports import *

kernel = np.ones((5,5),np.uint8)

img = cv2.imread("img/j.png")

img_o = cv2.imread("img/opening.png")
img_c = cv2.imread("img/closing.png")


erosion = cv2.erode(img,kernel,iterations=1)

dilation = cv2.dilate(img,kernel,iterations=1)

opening = cv2.morphologyEx(img_o,cv2.MORPH_OPEN,kernel) 

closing = cv2.morphologyEx(img_c,cv2.MORPH_CLOSE,kernel)

gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)


to_show = eval(input("Enter type of morphology: "))

cv2.imshow("window",to_show)
cv2.waitKey(0)