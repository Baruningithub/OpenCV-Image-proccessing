from imports import *

img = cv2.imread("img/rgb_bw.jpg")
# img_re=cv2.resize(img,(400,500))

while True:
    img[:,:,1]+=1
    cv2.imshow("win",img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
     
cv2.destroyAllWindows()