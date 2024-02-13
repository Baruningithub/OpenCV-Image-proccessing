from imports import *

img = cv2.imread("img/rgb.jpg")

matrix = np.float32([[1,0,100],[0,1,100]])

translated = cv2.warpAffine(img, matrix, dsize=(img.shape[1]+100,img.shape[0]+100))

# print(type(translated))
cv2.imshow('Original Image', img)
cv2.imshow("translated_img",translated)
cv2.waitKey(0)
cv2.destroyAllWindows()