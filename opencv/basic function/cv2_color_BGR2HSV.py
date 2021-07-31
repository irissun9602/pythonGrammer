# HSV 색상 공간에서 밝기 변환 예제
import os
import cv2
# 영상 읽기
path = os.path.join('./input', 'lime.jpg')
img1 = cv2.imread(path, cv2.IMREAD_UNCHANGED)

# 색상 공간 변환
res1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

# 색상 공간 분할 및 병합
res1_split = cv2.split(res1)
res1_split[2] = cv2.add(res1_split[2], 100)
res1_merge = cv2.merge(res1_split)
res1_merge = cv2.cvtColor(res1_merge, cv2.COLOR_HSV2BGR)

ress = []

for i in range(0, 3):
    ress.append(res1_split[i])
ress.append(res1_merge)

# 영상 출력
displays = [("split1", ress[0]), ("split2", ress[1]), ("split3", ress[2]), ("merge", ress[3])]

for (name, out) in displays:
    cv2.imshow(name, out)

cv2.waitKey(0)