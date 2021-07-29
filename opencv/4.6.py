import cv2
import numpy as np


def nothing():
    pass


cv2.namedWindow('RGB track bar')
cv2.createTrackbar('Red color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('Green color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('Blue color', 'RGB track bar', 0, 255, nothing)

cv2.setTrackbarPos('Red color', 'RGB track bar', 125)
cv2.setTrackbarPos('Green color', 'RGB track bar', 125)
cv2.setTrackbarPos('Blue color', 'RGB track bar', 125)

img = np.zeros((512, 512, 3), np.uint8)

while True:
    redval = cv2.getTrackbarPos('Red color', 'RGB track bar')
    greenval = cv2.getTrackbarPos('Green color', 'RGB track bar')
    blueval = cv2.getTrackbarPos('Blue color', 'RGB track bar')

    cv2.rectangle(img, (0, 0), (512, 512), (blueval, greenval, redval), -1)
    cv2.imshow('RGB track bar', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
