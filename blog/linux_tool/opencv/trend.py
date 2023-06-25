import cv2
import numpy as np

print(np.pi / 180)

img = cv2.imread("trend.png")
height = img.shape[0]  # 高度
width = img.shape[1]  # 宽度
cut_img = img

gray = cv2.cvtColor(cut_img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

result = cut_img.copy()
minLineLength = 30  # height/32
maxLineGap = 10  # height/40
lines = cv2.HoughLinesP(edges, 1, np.pi / 1, 80, 0, 0)

for line in lines:
    # for x1, y1, x2, y2 in lines[0]:
    for x1, y1, x2, y2 in line:
        if int(y2) != int(y1):
            cv2.line(result, (x1, y1), (x2, y2), (0, 255, 0), 2)
        else:
            ...

cv2.imshow("result", result)
cv2.waitKey(0)
