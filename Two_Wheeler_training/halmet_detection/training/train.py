from ultralytics import YOLO
model = YOLO("yolov8n.yaml")


results = model.train(data="..\data\anotated_dataset\data.yaml", epochs=100, imgsz=640 , conf=0.5)
model.save("../models/model1.pt")