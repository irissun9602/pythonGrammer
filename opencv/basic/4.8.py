# 10.6 자유 낙하 운동
import cv2
from math import *
import numpy as np
import time

cv2.namedWindow('Free Fall')

width = 512
height = 960
img = np.zeros((height, width, 3), np.uint8)

times = ypos = 0

#y좌표가 960일때의 위치를 빨간 원으로 표시
cv2.circle(img, (256, 960), 10, (0, 0, 255), -1)

while True:
    if ypos+30 <height:
        cv2.circle(img, (256, 30+ypos), 10, (255, 0, 0), -1)
        times +=1
        ypos = int((9.8 * times**2)/2)
        print(times, ':', ypos)
        time.sleep(1)
    cv2.imshow('Clock', img)
    if cv2.waitKey(100) >= 0:
        break

cv2.destroyAllWindows()
