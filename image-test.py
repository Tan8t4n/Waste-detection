from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load mô hình YOLO đã được huấn luyện (có thể là yolov8n.pt, yolov8s.pt,...)
model = YOLO("best.pt")  # hoặc đường dẫn đến model .pt tùy chỉnh

# Đọc ảnh đầu vào
image_path = "img4398.jpg"
image = cv2.imread(image_path)

# Thực hiện dự đoán
results = model(image)

# Vẽ kết quả lên ảnh
annotated_frame = results[0].plot()

# Hiển thị ảnh kết quả bằng matplotlib
plt.imshow(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("YOLO Detection")
plt.show()
