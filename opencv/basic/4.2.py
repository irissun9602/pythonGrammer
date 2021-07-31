# 9.4 이미지 읽어오기 + 선 그리기
import cv2 as cv
import numpy as np
# 이미지 읽어오기
img = cv.imread("../input/1616588556114.jpg", 1)

height = img.shape[0]
width = img.shape[1]

# 앞에 두 인자 좌표값(y,x)를 읽어와 픽셀색깔을 조절합니다.
for y in range(0, height):
    # 좌표순서가 y,x인 것에 유의하세요.
    # blue, green, red 순으로 개별적으로 픽셀값을 조절합니다.
    img.itemset(y, int(width/2), 0, 0)
    img.itemset(y, int(width/2), 1, 0)
    img.itemset(y, int(width/2), 2, 255) # 빨간색

for x in range(0, width):
    img.itemset(int(height/2), x, 0, 255) # 파란색
    img.itemset(int(height/2), x, 1, 0)
    img.itemset(int(height/2), x, 2, 0)

cv.imshow("win", img)

cv.waitKey()
