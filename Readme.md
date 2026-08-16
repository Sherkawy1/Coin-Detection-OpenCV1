
# Coin Detection using Computer Vision & AI

This project detects and classifies Egyptian coins in real time using multiple computer vision techniques and deep learning models.

## Project Overview

The project implements three different approaches for coin detection and classification:

### 1. Hough Circle Detection
- Detects circular objects from the webcam using classical computer vision.
- Measures coin diameter in pixels.
- Classifies coins based on their detected size.

### 2. Template Matching
- Compares detected objects with reference coin images stored in the `data/` directory.
- Identifies coin types using image similarity metrics.
- Supports different coin scales.

### 3. Roboflow / YOLO API Detection
- Uses a trained object detection model hosted on Roboflow (`egyptian-coins`).
- Detects and classifies Egyptian coins (One Pound, Half Pound, Quarter Pound) in real time with confidence scores.

## Technologies Used

- Python
- OpenCV
- NumPy
- Requests (for Roboflow API integration)

## Project Structure

```text
Coin-Detection-OpenCV
│
├── coin_detection_hough.py
├── coin_detection_template_matching.py
├── coin_detection_roboflow.py
├── Data/
│   ├── new-coin.jpg
│   ├── old-coin.jpg
│   └── half-coin.jpg
├── Readme.md
└── requirements.txt

```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt

```

> **Note:** Make sure `requests` is included in your `requirements.txt` for the Roboflow API script.

## How to Run

### 1. Hough Circle Detection

```bash
python coin_detection_hough.py

```

### 2. Template Matching

```bash
python coin_detection_template_matching.py

```

### 3. Roboflow API Detection

Set your Roboflow API key inside `coin_detection_roboflow.py` (or set it as an environment variable), then run:

```bash
python coin_detection_roboflow.py

```

## Features

* Real-time webcam processing.
* Multi-approach coin detection (Classical CV vs. Deep Learning API).
* Support for Egyptian coin denomination classification.
* Interactive bounding boxes and confidence score visualization.

## Author

Ahmed Sherkawy

```

```