from ultralytics import YOLO
model = YOLO("yolov8n.yaml")

results = model.train(data="..\data\Annotated_Data\Seatbelt-detection.v1i.yolov8\data.yaml", epochs=100, imgsz=640 , conf=0.5)
model.save("../Models/model.pt")