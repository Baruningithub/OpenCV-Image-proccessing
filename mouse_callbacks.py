from imports import *

img = np.zeros((512,512,3))

events = {
    0:"mouse hovered",
    1:"lmb down",
    4:"lmb up",
    2:"rmb down",
    5:"rmb up",
    3:"scroll button down",
    6:"scroll button up",
    7:"double lmb",
    8:"double rmb",
    9:"double sb",
    10:"scrolling",
    11:"scrolling h"
}
def draw(event,x,y,flags,params):
    if event in events:
        print(events[event])
    else:
        print(event)
    
cv2.imshow("win",img)

cv2.namedWindow(winname="win")
cv2.setMouseCallback("win",draw)

cv2.waitKey(0)
