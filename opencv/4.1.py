import cv2
# 이미지 읽어오기ㅌ
img = cv2.imread("1616588556114.jpg", 1)
cv2.namedWindow("image")
# 윈도우 팝업창 띄우기
cv2.imshow("image", img)
cv2.waitKey()
