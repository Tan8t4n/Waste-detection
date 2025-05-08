import os
import shutil
import random

# ====== Cấu hình ======
dataset_path = 'dataset'  
val_ratio = 0.25  

# ====== Tạo thư mục val nếu chưa có ======
val_img_path = os.path.join(dataset_path, 'images/val/paper')
val_lbl_path = os.path.join(dataset_path, 'labels/val/paper')
os.makedirs(val_img_path, exist_ok=True)
os.makedirs(val_lbl_path, exist_ok=True)

# ====== Lấy danh sách ảnh từ train ======
train_img_path = os.path.join(dataset_path, 'images/train/paper')
train_lbl_path = os.path.join(dataset_path, 'labels/train/paper')

image_files = [
    f for f in os.listdir(train_img_path)
    if f.endswith(('.jpg', '.jpeg', '.png'))
]

# ====== Chọn ngẫu nhiên ảnh để tạo validation ======
val_count = int(len(image_files) * val_ratio)
val_images = random.sample(image_files, val_count)

# ====== Sao chép ảnh + label sang thư mục val ======
for img_file in val_images:
    label_file = os.path.splitext(img_file)[0] + '.txt'

    # Đường dẫn gốc
    src_img = os.path.join(train_img_path, img_file)
    src_lbl = os.path.join(train_lbl_path, label_file)

    # Đường dẫn đích
    dst_img = os.path.join(val_img_path, img_file)
    dst_lbl = os.path.join(val_lbl_path, label_file)

    # Sao chép file
    shutil.copyfile(src_img, dst_img)
    if os.path.exists(src_lbl):
        shutil.copyfile(src_lbl, dst_lbl)

print(f"✅ Đã sao chép {val_count} ảnh vào tập validation.")
