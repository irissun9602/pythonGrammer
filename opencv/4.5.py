import cv2
import time

CAMERA_ID = 0
cam = cv2.VideoCapture(CAMERA_ID)
if not cam.isOpened():
    print
    'Can not open the Camera(%d)' % (CAMERA_ID)
    exit()

cv2.namedWindow('CAM_Window')

while(True):
    ret, frame = cam.read()

    now = time.localtime()
    str="%d. %d. %d. %d:%d:%d" %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    cv2.putText(frame, str, (0,100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255.255,0))

    cv2.imshow('CAM_Window', frame)

    if cv2.waitKey(10)>=0:
        break

cam.release()
cv2.destroyWindow('CAM_Window')