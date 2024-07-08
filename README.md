# **Training a YOLO Model for Foul Detection on Four-Wheelers and Two-Wheelers**

## **Introduction**

This documentation provides a comprehensive guide on how to train a YOLO (You Only Look Once) model for detecting fouls on four-wheelers and two-wheelers. The process involves capturing video from cameras on tracks, extracting frames, annotating the frames using Roboflow, and training the YOLO model with the annotated dataset.

## **Prerequisites**

- Basic knowledge of Python programming
- Familiarity with computer vision and deep learning concepts
- Installed software: Python, OpenCV, and Roboflow account

## **Setup**

### **Installing Necessary Libraries**

Ensure you have Python and pip installed.

## **Step 1: Capture Video**

Capture video from cameras on the track using any camera capturing tool:

## **Step 2: Upload Video to Roboflow for Frame Extraction and Annotation**

### **Create a Project in Roboflow**

1. **Sign in to** [**Roboflow**](https://roboflow.com/)**:**
    - Create an account if you don’t have one.
    - Log in to your account.
2. **Create a New Project:**
    - Click on "Create New Project."
    - Enter the project name (e.g., "Foul Detection") and select the project type as "Object Detection."

### **Upload Video for Frame Extraction**

1. **Upload Video:**
    - In your Roboflow project, click on "Upload" and select the video file you captured.
    - Roboflow will automatically extract frames from the video.
2. **Frame Settings:**
    - Configure the frame extraction settings, such as frame rate and resolution, as per your requirements.
    - Confirm and proceed with the extraction.

## **Step 3: Annotate Images in Roboflow**

For more specific for different tasks like:

1. Object classification ([link](https://docs.google.com/document/d/1bGWjtrYTSI6sAWNBuwzMASktHdliMnCn8tMS54TN4bs/edit))
2. Object segmentation ([link](https://docs.google.com/document/d/1aSrDVKe-tIuqp7jj2GMvsEh3vwbSW-DHz5UrUhoZpz0/edit))
3. Keypoint detection ([link](https://docs.google.com/document/d/1Bos0X0atIFyg29ROQuyjTuXtBcFCZrpLiGn3OkfqXXI/edit?usp=sharing))

### **Annotate Your Images**

1. **Access the Annotation Tool:**
    - Once frames are extracted, go to the "Annotate" section in your Roboflow project.
    - You will see the extracted frames ready for annotation.
2. **Label the Objects:**
    - Use the annotation tools to draw bounding boxes around fouls on four-wheelers and two-wheelers.
    - Label each bounding box appropriately (e.g., "foul_four_wheeler" and "foul_two_wheeler").
3. **Save Annotations:**
    - After annotating the frames, save your annotations.
    - Ensure all frames are accurately labeled to improve model performance.

### **Export the Annotated Dataset**

1. **Export Dataset:**
    - Once annotation is complete, go to the "Dataset" section in Roboflow.
    - Click on "Generate" to prepare the dataset for export.
2. **Select YOLO Format:**
    - Choose the YOLO format for exporting your dataset.
    - Configure any additional export settings if required.
3. **Download Dataset:**
    - Click "Download" to get the dataset, which will include images and corresponding YOLO-format annotation files.

For more detail refer this [BLOG](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/)

## **Step 4: Train YOLO Model**

### **Preparing the Training Environment**

1. Install ultralytics:

pip install ultralytics

pip install pillow

1. Train the Model:

yolo task=detect \\

mode=train \\

model=yolov8s.pt \\

data={dataset.location}/data.yaml \\

epochs=100 \\

imgsz=640

Model will be saved on {HOME}/runs/detect/train/weights/best.pt

Monitor the training process and adjust parameters if necessary.

##

##

## **Step 5: Evaluate and Test the Model(optional)**

1. **Evaluate Performance:**
    - Use the validation dataset to evaluate the model's performance.
    - Calculate metrics such as mAP (mean Average Precision).

yolo task=detect \\

mode=val \\

model={HOME}/runs/detect/train/weights/best.pt \\

data={dataset.location}/data.yaml

1. **Test the Model:**
    - Test the trained model on new images or video to see how well it performs in detecting fouls on four-wheelers and two-wheelers.

yolo task=detect \\

mode=predict \\

model={HOME}/runs/detect/train/weights/best.pt \\

conf=0.25 \\

source={dataset.location}/test/images

##

##

## **Step 6: Deployment**

1. **Export the Trained Model:**
    - Save the trained weights and configuration files.

from ultralytics import YOLO

model=YOLO("{HOME}/runs/detect/train/weights/best.pt")

1. **Integrate into Applications:**
    - Use the trained model in your applications for real-time foul detection on four-wheelers and two-wheelers on the tracks.

im1=Image.open("bus.jpg")

results=model.predict(source=im1,save=True # save plotted images
