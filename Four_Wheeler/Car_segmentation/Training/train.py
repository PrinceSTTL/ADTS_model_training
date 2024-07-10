from ultralytics import YOLO
model = YOLO("yolov8n.yaml")


results = model.train(data="..\Data\Annotated_Data\version-1-car-segmentation\data.yaml", epochs=100, imgsz=640 , conf=0.5)
model.save("../Models/model.pt")