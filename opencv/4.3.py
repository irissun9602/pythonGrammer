# 10.1 동영상 파일 활용하기

import cv2

cap = cv2.VideoCapture("drop.avi")

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('image', frame)

        key = cv2.waitKey(1) & 0xFF
        if(key == 27):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()