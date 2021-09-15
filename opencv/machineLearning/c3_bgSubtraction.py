# 전경-배경 분할 예제(c3_bgSubtraction.py)
# 전경-배경 분할 수행자 선언
import cv2
import os

bgMethod1 = cv2.createBackgroundSubtractorMOG2()
bgMethod2 = cv2.createBackgroundSubtractorKNN()
bgMethod1_blur = cv2.createBackgroundSubtractorMOG2()
bgMethod2_blur = cv2.createBackgroundSubtractorKNN()
imgIndex = 1

path = os.path.join('../input/', 'drop.avi')
cap = cv2.VideoCapture(path)
cv2.namedWindow('CAM_Window')

while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break
    # 전경 배경 분리 수행
    frame = cv2.resize(frame, (320,240))

    if imgIndex != 1:
        bgMOG = bgMethod1.getBackgroundImage()
        bgKNN = bgMethod2.getBackgroundImage()
        bgMog_blur = bgMethod1_blur.getBackgroundImage()
        bgMog_blur = bgMethod2_blur.getBackgroundImage()
    fgMOG = bgMethod1.apply(frame, learningRate=-1)
    fgKNN = bgMethod2.apply(frame)
    fgMOG_blur = bgMethod1_blur.apply(cv2.blur(frame, (5,5)), learningRate =-1)
    fgKNN_blur = bgMethod2_blur.apply(cv2.blur(frame,(5,5)))
    imgIndex +=1

    cv2.imshow('CAM_Window', frame)

    if cv2.waitKey(10) >= 0:
        break

cap.release()
cv2.destroyWindow('CAM_Window')