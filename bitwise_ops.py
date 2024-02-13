from imports import *

img = cv2.imread('img/bit1.png')
img1=cv2.resize(img,(300,300)) # equal size required to perform bitwise ops

img2 = cv2.imread('img/bit2.webp')
mask = cv2.imread('img/bit1.jpg', cv2.IMREAD_GRAYSCALE)


bitwise_and = cv2.bitwise_and(img1, img2)

bitwise_or = cv2.bitwise_or(img1, img2)

bitwise_xor = cv2.bitwise_xor(img1, img2)

bitwise_not = cv2.bitwise_not(img1)

masked_image = cv2.bitwise_and(img1, img1, mask=mask)

cv2.imshow('bitwise_and', bitwise_and)
cv2.imshow('bitwise_or', bitwise_or)
cv2.imshow('bitwise_not', bitwise_not)
cv2.imshow('bitwise_xor', bitwise_xor)
cv2.imshow('masked', masked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(img1.shape)
print(img2.shape)