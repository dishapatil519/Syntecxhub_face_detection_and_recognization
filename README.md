# Face Detection and Recognition using OpenCV

## Overview

This project demonstrates **Face Detection and Recognition** using Python. The system detects faces from a webcam in real time and recognizes known faces using a dataset of images.

The project is built using **OpenCV**, a popular computer vision library, and works by training the model using images stored in a folder.

---

## Technologies Used

* Python
* OpenCV
* NumPy

---

## Features

* Detect faces in real time using webcam
* Recognize known faces from stored images
* Draw bounding boxes around detected faces
* Display the name of the recognized person
* Supports multiple faces in one frame

---

## Project Structure

```
FaceRecognitionProject
│
├── face_recognition.py
├── faces
│   ├── akshay.jpg
│   ├── riya.jpg
│
└── README.md
```

The **faces** folder contains images of people that the system will recognize.
The image file name is used as the **person’s label**.

Example:

```
faces
 ├──akshay.jpg
 ├── riya.jpg
```

---

## Installation

Install required libraries using pip:

```
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
```

---

## How to Run the Project

1. Add images of known people in the **faces** folder.
2. Run the Python script:

```
python face_recognition.py
```

3. The webcam will start and detect faces in real time.
4. If a face matches an image in the dataset, the person's name will be displayed.

Press **ESC** to close the application.

---

## Applications

* Security systems
* Attendance systems
* Identity verification
* Smart surveillance systems

---

## Author

Disha Patil

---

## Note

This project is developed for educational purposes and demonstrates the basic concepts of face detection and recognition using computer vision.
