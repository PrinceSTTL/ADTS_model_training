from roboflow import Roboflow
rf = Roboflow(api_key="QGUv3ByU8poaQtZKKOFf")
project = rf.workspace("twowheelerposeestimation-pa5v2").project("abcdef-dvr3i")
version = project.version(1)
dataset = version.download("yolov8")
