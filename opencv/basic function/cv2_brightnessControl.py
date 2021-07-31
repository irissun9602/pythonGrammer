# 밝기 조절
import numpy as np
import os
import cv2

# 영상 읽기
path = os.path.join('../input', 'lime.jpg')
img1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 영상 밝기 조절 변수 선언 및 초기화
v = np.full(shape=img1.shape, fill_value=100, dtype=np.uint8)
v_n = np.full(shape=img1.shape, fill_value =255, dtype=np.uint8)

# 영상 밝기 조절
ress = []
ress.append(np.uint8(img1+v))
ress.append(cv2.add(img1, v))
ress.append(cv2.subtract(v_n, img1))

# 결과 영상 출력
displays = [("input1", img1),
            ("res1", ress[0]),
            ("res2", ress[1]),
            ("res3", ress[2])]
for (name, out) in displays:
    cv2.imshow(name, out)

# 키보드 입력을 기다린 후 모든 영상창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()