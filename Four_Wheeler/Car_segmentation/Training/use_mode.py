from ultralytics import YOLO

model = YOLO("../models/model.pt")
results = model.predict("imageurl")