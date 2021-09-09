# 특징 검지 예제(c3_featureDetection.py)
# 특징 검지 및 결과 영상 저장
import cv2
import os
import numpy as np

path = os.path.join('../input', 'img_6_0.png')
img1 = cv2.imread(path)

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
keyPoint = cv2.goodFeaturesToTrack(img1_gray, 25, 0.01, 10)
keyPoint = np.int0(keyPoint)
img2 = cv2.cvtColor(img1_gray, cv2.COLOR_GRAY2BGR)

for i in keyPoint:
    x,y = i.ravel()
    cv2.circle(img2, (x,y), 5, (0,0,255))
    cv2.imshow("goodToTrack", img2)
sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()
fast = cv2.FastFeatureDetector_create()
orb = cv2.ORB_create()
methods =[(sift, 'sift'), (surf, 'surf'), (fast, 'fast'),(orb, 'orb')]
for (method, name) in methods:
    print(name)
    keyPoint = method.detect(img1_gray, None)
    res = cv2.drawKeypoints(img1_gray, keyPoint, img1)
    cv2.imshow(name, res)
    # 영상 저장
    save_dir = '../code_res_imgs/c3_featureDetection'
    cv2.imwrite(save_dir + "/" + name + ".jpg", res)
    while(1):
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break