#영상 명암비 조절 예제 (c2_contrast.py)

# 관련 라이브러리 선언
import numpy as np
import os
import cv2

# 영상 읽기
path = os.path.join('../input', 'lime.jpg')
img1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 영상 명암비 조절 변수 선언 및 초기화
multi_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
log_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
invol_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
sel_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
multi_v = 2; gamma1 = 0.1; gamma2= 0.6
thres1 = 5; thres2 = 100
max_v_log = 255 / np.log(1 + 255)
max_v_invol = 255 / np.power(255, gamma1)
max_v_sel = 100 / np.power(thres2, gamma2)

for i in range(256):
    val = i * multi_v
    if val > 255 : val = 255
    multi_lut[i] = val
    log_lut[i] = np.round(max_v_log * np.log(1+i))
    invol_lut[i] = np.round(max_v_invol * np.power(i, gamma1))
    if i < thres1 : sel_lut[i] = i
    elif i > thres2 : sel_lut[i] = i
    else: sel_lut[i] =  np.round(max_v_sel * np.power(i, gamma2))

# 명암비 조절
ress = []
ress.append(cv2.LUT(img1, multi_lut)) # 상수곱 변환
ress.append(cv2.LUT(img1, log_lut)) # 로그 변환
ress.append(cv2.LUT(img1, invol_lut)) # 거듭제곱 변환
ress.append(cv2.LUT(img1, sel_lut)) # 구간 변환

# 결과 영상 출력
displays = [("input1", img1),
            ("res1", ress[0]),
            ("res2", ress[1]),
            ("res3", ress[2]),
            ("res4", ress[3])]
for (name, out) in displays:
    cv2.imshow(name, out)

# 키보드 입력을 기다린 후 모든 영상창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
