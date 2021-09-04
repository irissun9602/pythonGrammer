# 옵티클 플로우 예제(c3_opticalFlow.py)
# feature point 기반 optical flow 방법
# 비디오 읽기
import cv2
import numpy as np

cap = cv2.VideoCapture("../input/video7.mp4")
# ShiTomasi 코너 검출기 변수 설정
numMaxCorners = 20
feature_params = dict(maxCorners = numMaxCorners, qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize =7)
# 루카스-카나데 기반 옵티클 플로우 변수 설정
lk_params = dict(winSize = (15,15),
                 maxLevel = 2,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10,0.03))

# 초기 프레임에서 특징점 검출
ret, prevFrame = cap.read()
prevFrame = cv2.resize(prevFrame, (320,240))
prevGray = cv2.cvtColor(prevFrame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(prevGray, mask =None, **feature_params)
# 옵티클 플로우를 표현하기 위한 색 및 이미지 생성
flowColor = np.random.randint(0,255, (numMaxCorners, 3))
mask = np.zeros_like(prevFrame)
while(1):
    ret, curFrame = cap.read()
    if ret != True:
        break
    curFrame = cv2.resize(curFrame, (320,240))
    curGgray = cv2.cvtColor(curFrame, cv2.COLOR_BGR2GRAY)
    p1, st, err = cv2.calcOpticalFlowPyrLK(prevGray, curGgray, p0, None, **lk_params)
    # good points 선택
    good_new = p1[st==1]
    good_old = p0[st==1]
    # 특징점 및 기준 프레임 업데이트
    prevGray = curGgray.copy()
    p0 = good_new.reshape(-1,1,2)
    # 특징점 추적 결과 표시
    for i , (new, old) in enumerate(zip(good_new, good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b), (c,d), flowColor[i].tolist(), 2)
        curFrame = cv2.circle(curFrame, (a,b), 5, flowColor[i].tolist(), -1)
    res = cv2.add(curFrame, mask)
    cv2.imshow('frame', res)
    # ESC 버튼 입력시 종료
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
