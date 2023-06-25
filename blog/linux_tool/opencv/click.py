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
