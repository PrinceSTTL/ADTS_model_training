from ultralytics import YOLO

model = YOLO("../models/model1.pt")
results = model.predict("imageurl")