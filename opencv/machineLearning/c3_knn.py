# 영상 군집화 예제
# knn 입력 생성
import cv2
import numpy as np

# 영상 읽기
img1 = cv2.imread("../input/img20.jpg", cv2.IMREAD_UNCHANGED)

data = img1.reshape((-1,3))
data = np.float32(data)
# knn 변수 설정
criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
attempts = 10
flags = cv2.KMEANS_RANDOM_CENTERS
for i in range(1, 3):
    # knn 수행
    numK = i *5
    ret, label, center = cv2.kmeans(data, numK, None, criteria, attempts, flags)
    # 결과 영상 출력 및 저장
    center = np.uint8(center)
    res = center[label.flatten()]
    res = res.reshape(img1.shape)
    cv2.imshow('res', res)
    # 키보드 입력을 기다린 후 모든 영상창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()