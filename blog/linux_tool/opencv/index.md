---
title: opencv
date: 2020-08-02
tags: [ linux ]
---

```python title="click.py"
import cv2


def draw_rectangle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(img, center=(x, y), radius=5, color=(87, 184, 237), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, center=(x, y), radius=10, color=(87, 184, 237), thickness=1)


img = cv2.imread("./road-line.jpeg")

cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_rectangle)

# Step 3. Execution
while True:
    cv2.imshow("my_drawing", img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```

```python title="trend.py"
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
```
