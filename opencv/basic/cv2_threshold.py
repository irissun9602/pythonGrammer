# 1. 영상 이진화 예제
import numpy as np
import os
import cv2

# 영상 읽기
path = os.path.join('./input', 'lime.jpg')
img1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

types = [cv2.THRESH_BINARY,
          cv2.THRESH_BINARY_INV,
          cv2.THRESH_TRUNC,
          cv2.THRESH_TOZERO,
          cv2.THRESH_TOZERO_INV,
          cv2.THRESH_OTSU,
          cv2.THRESH_TRIANGLE,

          cv2.ADAPTIVE_THRESH_MEAN_C,
          cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
          cv2.ADAPTIVE_THRESH_MEAN_C,
          cv2.ADAPTIVE_THRESH_GAUSSIAN_C
          ]

# 임계치 설정
thres = 70
# 이진화의 최댓값
maxVal=255
ress = []

# threshold 함수를 이용한 이진화 수행
for i in range(0,7):
    ret, res = cv2.threshold(img1, thres, maxVal, types[i])
    ress.append(res)
# adaptiveThreshold 함수를 이용한 이진화 수행(임계치 설정 추가)
ress.append(cv2.adaptiveThreshold(img1,maxVal, types[7], types[0], 11, 0))
ress.append(cv2.adaptiveThreshold(img1,maxVal, types[8], types[0], 11, 0))
ress.append(cv2.adaptiveThreshold(img1,maxVal, types[9], types[0], 61, 0))
ress.append(cv2.adaptiveThreshold(img1,maxVal, types[10], types[0], 61, 0))

#결과 출력
displays = [("input", img1), ("res1", ress[0]), ("res2", ress[1]), ("res3", ress[2]),
            ("res4", ress[3]), ("res5", ress[4]), ("res6", ress[5]), ("res7", ress[6]),
            ("res8", ress[7]), ("res9", ress[8]), ("res10", ress[9]), ("res11", ress[10])
            ]

for (name, out) in displays:
    cv2.imshow(name, out)
    cv2.imwrite("./code_res_imgs"+"/threshold/"+name+".jpg", out)

cv2.waitKey(0)
