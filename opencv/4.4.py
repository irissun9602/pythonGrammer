# 마우스 이벤트 활용하기

import cv2
import numpy as np


def draw_rectangle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img, (x,y), (x+50,y+50), (255, 0, 0), -1)


img = np.zeros((512, 512, 3), np.uint8) # 행렬 생성, (가로, 세로, 채널(rgb)),bit)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27: #esc키로 종료
        break

cv2.destroyAllWindows()
