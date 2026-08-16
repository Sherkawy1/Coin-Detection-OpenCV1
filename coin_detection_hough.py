import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    gray_blurred = cv2.medianBlur(gray, 7)

    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT,
        dp=1, #accuracy
        minDist=80,
        param1=50, #to get frames
        param2=40, # to check the ratio of being sure that it's circle
        minRadius=20,
        maxRadius=200
    )

    if circles is not None:
        circles = np.uint16(np.around(circles)) #flout

        for circle in circles[0, :]:
            cx, cy, radius = circle[0], circle[1], circle[2]
            diameter = radius * 2

            if 130 <= diameter <= 134:
                name = "New Coin"
            elif 154 <= diameter <= 158:
                name = "Old Coin"
            elif 138 <= diameter <= 144:
                name = "Half Coin"
            else:
                name = None


            cv2.circle(frame, (cx, cy), radius, (0, 255, 0), 2)

            cv2.circle(frame, (cx, cy), 2, (0, 0, 255), 3)


            if name is not None:
                cv2.putText(frame, name, (cx - radius, cy - radius - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()