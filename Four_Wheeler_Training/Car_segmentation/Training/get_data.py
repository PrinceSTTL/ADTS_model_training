from roboflow import Roboflow
rf = Roboflow(api_key="yyuB2r08r6GRUmqVwtct")
project = rf.workspace("car-detection-and-segmentation-nnhjj").project("custom-car-segmentation")
version = project.version(1)
dataset = version.download("yolov8")
