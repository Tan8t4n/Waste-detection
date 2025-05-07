import os
from PIL import Image

# Cấu hình thư mục
input_folder = "temp/battery"            # Thư mục chứa ảnh gốc
output_folder = "resized/battery"   # Thư mục lưu ảnh đã resize
target_size = (416, 416)           # Kích thước đích (width, height)

# Tạo thư mục đầu ra nếu chưa có
os.makedirs(output_folder, exist_ok=True)

# Duyệt qua tất cả các file trong thư mục đầu vào
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                img = img.convert("RGB")  # Chuyển đổi sang RGB để đảm bảo tương thích
                resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
                resized_img.save(output_path)
                print(f"Đã resize: {filename}")
        except Exception as e:
            print(f"Lỗi khi xử lý {filename}: {e}")