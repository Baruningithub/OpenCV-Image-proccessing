from imports import *

img = np.zeros((512,512,3))

def draw(event,x,y,flags,params):
    if event == 1:
        cv2.circle(img,center=(x,y),radius=3,color=(0,0,255),thickness=-1)
        print(f"point at ({x},{y})")
    


cv2.namedWindow(winname="win")
cv2.setMouseCallback("win",draw)

while True:
    
    cv2.imshow("win",img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


cv2.destroyAllWindows()