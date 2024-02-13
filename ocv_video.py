from imports import *

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('img/output.mp4', fourcc, 20.0, (640,  480))

while True:
    ret , frame = cap.read()

    out.write(frame)
    cv2.imshow("webcam",frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()