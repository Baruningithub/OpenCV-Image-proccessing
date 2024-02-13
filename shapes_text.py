from imports import *

img = np.zeros((720,720,3))

# rectangle
cv2.rectangle(img,pt1=(100,100),pt2=(400,400),color=(0,255,0),thickness=-1)

#circle 
cv2.circle(img,center=(100,100),radius=50,color=(255,255,0),thickness=5)

# line 
cv2.line(img,pt1=(0,0),pt2=(720,720),color=(0,0,255),thickness=4)

#text 
cv2.putText(img,org=(400,400),text="HEllo",fontScale=4,color=(255,25,0),thickness=2,
            lineType=cv2.LINE_AA,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)


cv2.imshow("window",img)
cv2.waitKey(0)
