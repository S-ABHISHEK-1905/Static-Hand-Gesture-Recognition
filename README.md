# Static Hand Gesture Recognition by S.ABHISHEK

<br>

## Overview of Project

This project demonstrates real-time hand gesture recognition using cvzone (built on top of MediaPipe) and OpenCV.
It can detect and classify four distinct static gestures:

🖐 Open Palm

✊ Fist

✌ Peace Sign (V-sign)

👍 Thumbs Up

The system uses a webcam feed, performs hand landmark detection, and applies gesture classification logic to recognize the gestures. The recognized gesture is displayed live on the video stream.

<hr>

<br>

## Technology Justification

#### cvzone (HandTrackingModule)
Built on Google’s MediaPipe, providing 21 landmark points per hand.
High accuracy and lightweight for real-time detection.
Easy-to-use wrapper, making code simpler and cleaner.

#### OpenCV
Efficient real-time video stream processing.
Drawing utilities for bounding boxes, skeletons, and text overlay.

```
Why this choice?
cvzone + MediaPipe provides a ready-to-use with a rich feature set, optimized solution for hand tracking and gesture recognition, making it the best choice for this problem.
```

<hr>

<br>


## Gesture Logic Explanation
We use cvzone.HandDetector to get:

lmList — list of 21 landmark points (each point: (x, y, z) in pixel coords),

<img width="850" height="412" alt="image" src="https://github.com/user-attachments/assets/826c2391-7dc2-4ac8-85c6-4e8803a25949" />

bbox — hand bounding box,

fingersUp(hand) — helper that returns [Thumb, Index, Middle, Ring, Pinky] with 1 = finger up, 0 = finger down.

Using those outputs we classify the required four static gestures with deterministic rules:

<hr>

### 🖐 Open Palm

Condition: fingers == [1, 1, 1, 1, 1].

Meaning: all five fingers detected as “up”.

Visual feedback: label "Open Palm" displayed on screen.

<hr>

### ✊ Fist

Condition: fingers == [0, 0, 0, 0, 0].

Meaning: fingertips are near or behind knuckles — all fingers down.

Visual feedback: label "Fist" displayed.

<hr>

### ✌ Peace Sign (V-sign)

Condition: fingers == [0, 1, 1, 0, 0].

Meaning: Index and middle fingers extended, others folded.

Visual feedback: label "Peace Sign".

<hr>

### 👍 Thumbs Up

Condition: fingers == [1, 0, 0, 0, 0].

Meaning: only thumb raised.

Visual feedback: label "Thumbs Up".


<hr>

<br>

## Setup and Execution Instructions

### 1. Clone Repository
```
git clone https://github.com/S-ABHISHEK-1905/Static-Hand-Gesture-Recognition
cd Static-Hand-Gesture-Recognition
```

### 2. Create Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate      
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Application
```
python main.py
```

The webcam window will open and display the detected gesture in real-time.

<hr>
<br>

## Algorithm

1. Initialize webcam and required libraries (cv2, cvzone, numpy).

2. Create HandDetector object with maxHands=1 and detectionCon=0.8.

3. Capture video frames in a loop.

4. Detect hand(s) using detector.findHands().

5. Extract finger states with detector.fingersUp().

6. Compare finger states to predefined patterns for gestures.

7. Display detected gesture name and hand skeleton on the frame.

8. Continue looping until user presses 'q'.

9. Release webcam and close all windows.

## OUTPUT
https://github.com/user-attachments/assets/8393e84d-f837-4f69-a351-ad70963bd035



