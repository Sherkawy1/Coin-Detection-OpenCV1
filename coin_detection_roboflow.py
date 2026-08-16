import cv2
import requests
import base64


API_KEY = "****"  #Your API Code on Roboflow
MODEL_ID = "egyptian-coins"
MODEL_VERSION = "4"
API_URL = f"https://detect.roboflow.com/{MODEL_ID}/{MODEL_VERSION}"


COIN_NAMES = {
    "one": "One Pound",
    "half": "Half Pound",
    "quarter": "Quarter Pound",
}


cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("We can't open the camera ")
    exit()

print("Program started")

frame_count = 0
last_predictions = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("We can't open the camera ")
        break

    frame_count += 1


    if frame_count % 5 == 0:

        _, img_encoded = cv2.imencode(".jpg", frame)
        img_base64 = base64.b64encode(img_encoded).decode("utf-8")

        try:
            response = requests.post(
                API_URL,
                params={"api_key": API_KEY},
                data=img_base64,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=10
            )
            result = response.json()
            last_predictions = result.get("predictions", [])

        except Exception as e:
            print(f"Error at API address {e}")

    for pred in last_predictions:
        x, y = int(pred["x"]), int(pred["y"])
        w, h = int(pred["width"]), int(pred["height"])
        raw_name = pred["class"]
        cls_name = COIN_NAMES.get(raw_name, raw_name)
        conf = pred["confidence"]

        x1, y1 = x - w // 2, y - h // 2
        x2, y2 = x + w // 2, y + h // 2

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{cls_name} {conf:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Egyptian Coin Detection - to exit enter 'q' ", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print ("Programe ended")