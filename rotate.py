import os
from PIL import Image

# Đường dẫn thư mục ảnh đầu vào và đầu ra
input_folder = 'dataset/images/train/plastic'     # Thay bằng đường dẫn thư mục chứa ảnh gốc
output_folder = 'rotated/plastic'  # Thư mục lưu ảnh đã xoay

# Tạo thư mục đầu ra nếu chưa tồn tại
os.makedirs(output_folder, exist_ok=True)

# Góc cần xoay
angles = [90,180]

# Duyệt qua từng file trong thư mục đầu vào
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)

    # Bỏ qua nếu không phải là ảnh
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        continue

    try:
        with Image.open(input_path) as img:
            for angle in angles:
                rotated_img = img.rotate(angle, expand=True)
                name, ext = os.path.splitext(filename)
                output_filename = f"{name}_rotated_{angle}{ext}"
                output_path = os.path.join(output_folder, output_filename)
                rotated_img.save(output_path)
                print(f"Lưu ảnh: {output_path}")
    except Exception as e:
        print(f"Lỗi khi xử lý ảnh {filename}: {e}")

print("Hoàn tất xoay và lưu ảnh.")
