# 영상 합성 및 스티칭 예제(c3_stitch.py)
# 영상 스티칭
import cv2
import os
path = os.path.join('../input/', 'img3.jpg')
img3 = cv2.imread(path)

h, w, c = img3.shape

# stitch 입력 생성
stepW = int(w/3)
overlap = int(stepW*0.3)
sp1 = img3[:, :stepW + overlap, :]
sp2 = img3[:, stepW - overlap:(stepW*2) + overlap, :]
sp3 = img3[:, (stepW*2) - overlap:, :]
sp1 = cv2.resize(sp1, (320,240))
sp2 = cv2.resize(sp2, (320,240))
sp3 = cv2.resize(sp3, (320,240))
imgs1 = []; imgs1.append(sp1); imgs1.append(sp2)
imgs2 = []; imgs2.append(sp2); imgs2.append(sp3)
imgs3 = []; imgs3.append(sp1); imgs3.append(sp2); imgs3.append(sp3)

# stitch 생성 및 실행 cv2.createStitcer()
stitcher =cv2.createStitcher(cv2.STITCHER_PANORAMA)
status1, pano1 = stitcher.stitch(imgs1)
if status1 != cv2.Stitcher_OK:
    print("Can't stitch imgs1, error code =%d" % status1)
    exit(-1)
status2, pano2 = stitcher.stitch(imgs2)
if status2 != cv2.Stitcher_OK:
    print("Can't stitch imgs2, error code =%d" % status2)
    exit(-1)
status3, pano3 = stitcher.stitch(imgs3)
if status3 != cv2.Stitcher_OK:
    print("Can't stitch imgs3, error code =%d" % status3)
    exit(-1)
#cv2.imshow('stitch', stitcher)
# 키보드 입력을 기다린 후 모든 영상창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()