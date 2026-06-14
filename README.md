# Real-Time Hand Detection with MediaPipe

A real-time hand detection and hand landmark tracking application built using Python, OpenCV, and MediaPipe.

## Overview

This project uses a webcam to detect and track hand landmarks in real time. The detected landmarks are displayed on the video feed, allowing visualization of hand movements and finger positions.

## Features

* Real-time webcam hand detection
* Hand landmark tracking
* Multiple hand support
* Landmark connection visualization
* FPS (Frames Per Second) display
* Lightweight and efficient processing

## Technologies Used

* Python
* OpenCV
* MediaPipe

## Installation

### Clone the repository

```bash
git clone https://github.com/devv2308/face_and_hand_detect_together.py.git
cd face_and_hand_detect_together.py
```
### Install dependencies

```bash
pip install mediapipe opencv-python
```

## Required Model

Place the following model file in the project directory:

```text
hand_landmarker.task
```

## Run the Project

```bash
python main.py
```

## Project Structure

```text
face_and_hand_detect_together.py/
│
├── main.py
├── hand_landmarker.task
└── README.md
```

## Output

The application opens your webcam and:

* Detects hands in real time
* Draws hand landmarks
* Connects landmarks to form a hand skeleton
* Displays tracking results on the video stream

## Future Improvements

* Gesture recognition
* Sign language detection
* Hand-controlled applications
* Virtual mouse control
* AI-powered hand action classification

## Author

Devv2308

## License

This project is available for educational and learning purposes.
