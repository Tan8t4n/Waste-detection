import cv2
from ultralytics import YOLO

# Tải mô hình đã được huấn luyện
model = YOLO("best.pt")  # Đường dẫn đến file YOLO đã train

# Mở webcam (0 là webcam mặc định)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.8)   # giá trị từ 0.0 đến 1.0 (tùy webcam)
cap.set(cv2.CAP_PROP_CONTRAST, 0.9)

if not cap.isOpened():
    print("Không thể mở webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Dự đoán với YOLO
    results = model.predict(source=frame, conf=0.7, save=False)

    # Kiểm tra có ít nhất một vật thể được nhận dạng không
    has_detection = False

    for result in results:
        boxes = result.boxes
        if len(boxes) > 0:
            has_detection = True
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0]
                cls = int(box.cls[0])
                label = model.names[cls]

                # Vẽ khung
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # Thêm nhãn
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


    # Hiển thị frame
    cv2.imshow("Waste Detection (YOLO)", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng
cap.release()
cv2.destroyAllWindows()
