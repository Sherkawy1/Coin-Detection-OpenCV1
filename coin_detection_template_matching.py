import cv2
import numpy as np

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera index 1! Try index 0 instead.")
    exit()

new_coin = cv2.imread("data/new-coin.jpg", 0)
old_coin = cv2.imread("data/old-coin.jpg", 0)
half_coin = cv2.imread("data/half-coin.jpg", 0)

for name, img in [("new_coin", new_coin), ("old_coin", old_coin), ("half_coin", half_coin)]:
    if img is None:
        print(f"Warning: {name} image not found or path is wrong!")
    else:
        print(f"{name} loaded successfully - size: {img.shape}")

templates = [
    ("New Coin", new_coin),
    ("Old Coin", old_coin),
    ("Half Coin", half_coin)
]

scales = np.linspace(0.2, 1.0, 15) #to compare the ratio of size of the photo

threshold = 0.5

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot read frame from camera")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_h, frame_w = gray.shape[:2]

    for name, temp in templates:

        if temp is None:
            continue

        best_match = None

        for scale in scales:
            resized_temp = cv2.resize(temp, None, fx=scale, fy=scale)
            rw, rh = resized_temp.shape[::-1]

            if rw > frame_w or rh > frame_h:
                continue

            result = cv2.matchTemplate(gray, resized_temp, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if best_match is None or max_val > best_match["score"]:
                best_match = {
                    "score": max_val,
                    "loc": max_loc,
                    "w": rw,
                    "h": rh,
                    "scale": scale
                }

        if best_match is not None:
            print(f'{name}: best score = {best_match["score"]:.3f} at scale {best_match["scale"]:.2f}')

            if best_match["score"] >= threshold:
                x, y = best_match["loc"]
                w, h = best_match["w"], best_match["h"]

                center_x = x + w // 2
                center_y = y + h // 2
                radius = max(w, h) // 2

                cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    name,
                    (center_x - radius, center_y - radius - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

    cv2.imshow("Coins", frame)

    if cv2.waitKey(1) == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()