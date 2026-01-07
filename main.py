import cv2
from ultralytics import YOLO
import pytesseract
import mysql.connector
from datetime import datetime
from config import DB_CONFIG, STREAM_URL, TESSERACT_PATH

cap = cv2.VideoCapture(STREAM_URL)

db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

model = YOLO('best.pt')

if not cap.isOpened():
    print("Cannot open ESP32-CAM stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=0.5, verbose=False)

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()

        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            plate_img = frame[y1:y2, x1:x2]

            gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (5,5), 0)
            _, thresh = cv2.threshold(gray, 0,255, cv2.TH_BINARY + cv2.TH_OTSU)

            plate_text = pytesseract.image_to_string(thresh, config='--psm 7')
            plate_text = "".join(c for c in plate_text if c.isalnum())

            if plate_text:
                entry_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                sql = "INSERT INTO car_entries (plate_number, entry_time) VALUES (%s, %s)"
                cursor.execute(sql, (plate_text, entry_time))
                db.commit()

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cursor.close()
db.close()
