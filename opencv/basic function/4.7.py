# 10.5 아날로그 시계 시침, 분침 그리기
import cv2
import time
from math import *
import numpy as np

cv2.namedWindow('Clock')
img = np.zeros((512,512,3), np.uint8)
while True:
    cv2.circle(img, (256, 256), 250, (125,125,125), -1)

    now = time.localtime()
    hour = now.tm_hour
    min = now.tm_min


    # 시침의 이동량
    Ang_Min = min *6
    # 분침의 이동량
    Ang_Hour = hour*30 + min*0.5

    #12시를 시초선으로 시침, 분침의 이동량을 라디안 값으로 변환(각도*파이/180.0)
    radian = (90-Ang_Hour) * 3.141592 / 180.0 # 시침 각도
    radian2 = (90 - Ang_Min) * 3.141592 / 180.0 # 분침 각도

    # 시침 그리기
    x_pos = int(150 * cos(radian))
    y_pos = int(150 * sin(radian))
    print(x_pos, y_pos)
    cv2.line(img, (256,256), (256+x_pos, 256-y_pos), (0,255,0), 6)
    # 분침 그리기
    x_pos = int(200 * cos(radian2))
    y_pos = int(200 * sin(radian2))
    print(x_pos, y_pos)
    cv2.line(img, (256,256), (256+x_pos, 256-y_pos), (0,255,0), 1)

    cv2.imshow('Clock', img)
    if cv2.waitKey(10) >= 0:
        break

cv2.destroyAllWindows()