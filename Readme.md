\# Coin Detection using OpenCV



This project detects and classifies coins in real time using computer vision techniques with OpenCV.



\## Project Overview



The project implements two different approaches for coin detection:



\### 1. Hough Circle Detection

\- Detects circular objects from the webcam.

\- Measures coin diameter in pixels.

\- Classifies coins based on their detected size.



\### 2. Template Matching

\- Compares detected objects with reference coin images.

\- Identifies coin types using image similarity.

\- Supports different coin scales.



\## Technologies Used



\- Python

\- OpenCV

\- NumPy



\## Project Structure



```text

Coin-Detection-OpenCV

│

├── coin\_detection\_hough.py

├── coin\_detection\_template\_matching.py

├── data

│   ├── new-coin.jpg

│   ├── old-coin.jpg

│   └── half-coin.jpg

├── README.md

└── requirements.txt

```



\## Installation



```bash

pip install -r requirements.txt

```



\## Run



\### Hough Circle Detection



```bash

python coin\_detection\_hough.py

```



\### Template Matching



```bash

python coin\_detection\_template\_matching.py

```



\## Features



\- Real-time webcam processing.

\- Coin detection and classification.

\- Multiple computer vision techniques.

\- Comparison between Hough Circles and Template Matching.



\## Author



Ahmed Sherkawy

