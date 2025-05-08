from ultralytics import YOLO

if __name__ == '__main__':
    # Load model đã huấn luyện tốt nhất trước đó
    model = YOLO('best.pt')

    # Train lại với dữ liệu đã mở rộng thêm
    model.train(
        data='data.yaml',   
        epochs=50,          
        imgsz=320,
        batch=16,
        workers=8,
        box=0.5,
        cls=1.5,
        dfl=1.0,
        hsv_h=0.03,
        hsv_s=0.5,
        hsv_v=0.6,
        close_mosaic = 5,
        optimizer='AdamW',
        device='cuda',
        name='new_v2'
    )
