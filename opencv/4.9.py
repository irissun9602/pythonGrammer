# 10.7 포물선 운동

import cv2
from math import *
import numpy as np

init_Vel = float(input("초기 속도를 입력하세요 : "))
init_Ang = float(input("초기 각도를 입력하세요 : "))
cv2.namedWindow('Parabolic Motion')

width = 590
height = 960
img = np.zeros((width, height, 3), np.uint8)

time = xpos = ypos = 0
init_posx = 30
init_posy = 250
Vel_x = int(init_Vel*cos(init_Ang*pi/180.0))
Vel_y = int(-1.0*init_Vel*sin(init_Ang*pi/180.0))

while True:
    if (ypos + 30) < height:
        cv2.circle(img, (init_posx+xpos, init_posy+ypos), 10, (255, 0, 0), -1)
        time += 0.2
        Vel_y = int(Vel_y+9.8*time)

        xpos = int(xpos + Vel_x*time)
        ypos = ypos + int(Vel_y*time) - int((9.8 * time**2)/2)
        print(time, ':', xpos, ypos)

    cv2.imshow('Parabolic Motion', img)

    if cv2.waitKey(100) >= 0:
        break
cv2.destroyWindow('Parabolic Motion')