from imports import *

cap = cv2.VideoCapture("img/v1.mp4")

while True:
    ret , frame = cap.read()
    
    if ret:
        cv2.imshow("video",frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()
cv2.destroyAllWindows()