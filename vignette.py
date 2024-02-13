from imports import *

#Reading the image and getting properties
pre_img = cv2.imread('img/p1.jpg')
img =cv2.resize(pre_img,(460,560))
rows, cols = img.shape[:2]

# generating vignette mask using Gaussian kernels
kernel_x = cv2.getGaussianKernel(cols,200)
kernel_y = cv2.getGaussianKernel(rows,200)
#rowsXcols
kernel = kernel_y * kernel_x.T

#Normalizing the kernel
kernel = kernel/np.linalg.norm(kernel)

#Genrating a mask to image
mask = 255 * kernel
output = np.copy(img)

# applying the mask to each channel in the input image
for i in range(3):
	output[:,:,i] = output[:,:,i] * mask
cv2.imshow('Original', img)
cv2.imshow('Vignette', output)
cv2.waitKey(0)