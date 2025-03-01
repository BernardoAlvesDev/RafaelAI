# Project: Object Detection and Video Annotation with YOLO

This project demonstrates how to use **YOLO** (v5, v7, or v8, at your choice) for object detection (such as cars and people), generate versions of a video with present/absent background, and finally create a side-by-side comparison video displaying both the original and annotated videos.

---

## Table of Contents

- [Overview](#overview)
- [Folder Structure](#folder-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [YOLO Workflow](#yolo-workflow)
- [Training Your Own Model](#training-your-own-model)
- [Authors](#authors)

---

## Overview

This application allows you to:

1. **Process videos** to draw colored rectangles (annotations) around objects of interest — simulating what the AI “sees” vs. what the human “sees.”  
2. **Generate videos** with a present background (the original video) and an absent background (a black screen with annotations).  
3. **Combine** two videos side-by-side (e.g., the original video and the annotated video) for comparison.  
4. **Integrate** YOLO detection models to automatically identify objects in each frame (cars, people, etc.).

---

## Folder Structure

A sample way to organize your project:

my_project/ ├── data/ │ ├── input/ # Original videos (e.g., car_occlusion.mp4) │ ├── output/ # Resulting videos │ └── yolo_dataset/ # (Optional) for custom training │ ├── images/ │ │ ├── train/ │ │ └── val/ │ └── labels/ │ ├── train/ │ └── val/ ├── models/ │ └── yolo/ # YOLO weights (e.g. yolov5s.pt, best.pt) ├── src/ │ ├── video_processing.py # Functions for annotation and video combination │ ├── yolo_inference.py # YOLO inference code │ └── main.py # Main script that orchestrates everything ├── requirements.txt # Dependencies └── README.md # This file

yaml
Copiar
Editar

> Feel free to adapt this structure according to your project’s size and preferences.

---

## Requirements

- **Python 3.7+**  
- **OpenCV** (for reading/writing videos, drawing rectangles and text)  
- **Ultralytics** or another YOLO repository (if you want to use YOLOv5 or YOLOv8 for detection)  

---

## Installation

1. **Clone** the repository or download the project as a .zip.
2. **Install dependencies** via `requirements.txt` or manually:
   ```bash
   pip install -r requirements.txt
If you’re using YOLOv8 (Ultralytics):

bash
Copiar
Editar
pip install ultralytics
Organize your videos: place your video files in data/input/.
How to Run
Process the video to generate the three versions (present background, absent background, comparison):
Adjust the input and output file names in main.py (or via command-line, if preferred).
Run:
bash
Copiar
Editar
python src/main.py
Once done, you should find the following videos in the data/output/ folder:
fundo_presente.mp4
fundo_ausente.mp4
fundo_comparado.mp4
YOLO Workflow
To automatically detect cars, people, or any objects supported by the model:

Open yolo_inference.py (example name) and set the model path for YOLO (e.g. yolov5s.pt or best.pt).
In main.py, import and call the function that does YOLO inference on each video frame (e.g., run_yolo_inference('data/input/car_occlusion.mp4')).
YOLO returns bounding boxes (car, person, etc.) for each frame. You can then draw these boxes on the video (present or absent background).
Training Your Own Model
If you want to train YOLO (e.g., YOLOv8) for specific classes:

Prepare your images and labels in data/yolo_dataset/:
kotlin
Copiar
Editar
data/
  yolo_dataset/
    images/
      train/
      val/
    labels/
      train/
      val/
    data.yaml         # Defines where 'train' and 'val' are, plus your class list
Train:
bash
Copiar
Editar
yolo detect train data=data/yolo_dataset/data.yaml model=yolov8n.pt epochs=50
The best model will be saved in runs/detect/train/weights/best.pt.
Use this model in your script:
python
Copiar
Editar
from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')
# ...
Authors
You: If you’re adapting and developing this project for your specific needs.
Contributors: Any team members or colleagues who help with labeling, data collection, and implementation.
Note: This project serves as an educational example of how to generate videos with annotations (present/absent backgrounds) and how to integrate YOLO for object detection. Feel free to adapt it for real-world or research applications.
