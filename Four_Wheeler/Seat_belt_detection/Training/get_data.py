from roboflow import Roboflow
rf = Roboflow(api_key="AajdbwNf87WlBa4RsObZ")
project = rf.workspace("seatbelt-detection-5orx2").project("seatbelt-detection-tlnlh")
version = project.version(7)
dataset = version.download("yolov5")
