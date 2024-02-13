from imports import *
from random import randint
img = cv2.imread("img/gradient.png")

flag=False
ix=-1
iy=-1

def draw(event,x,y,flags,params):
    global flag,ix,iy
    
    if event == 1:
        flag=True
        ix=x
        iy=y

    elif event == 0:

        if flag:
            img_copy = img.copy()  
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 0, 0), thickness=2)
            cv2.imshow("win", img_copy)
    
    elif event == 4:
        flag=False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=2)
        
        # crop tool
        ran = randint(1,100)
        img_crop = img[iy:y,ix:x]
        cv2.imshow(f"win {ran}",img_crop)
        cv2.waitKey(0)


cv2.namedWindow(winname="win")
cv2.setMouseCallback("win",draw)
cv2.imshow("win",img)
cv2.waitKey(0)
