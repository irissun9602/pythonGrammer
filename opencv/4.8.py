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
while True:
    if ypos+30 <height:
        cv2.circle(img, (256, 30+ypos), 10, (255, 0, 0), -1)
        times +=1
        ypos = int((9.8 * times**2)/2)
        print(time, ':', ypos)
        time.sleep(1)
    cv2.imshow('Clock', img)
    if cv2.waitKey(100) >= 0:
        break

cv2.destroyAllWindows()
