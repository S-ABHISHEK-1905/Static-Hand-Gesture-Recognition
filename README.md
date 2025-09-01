# Static-Hand-Gesture-Recognition
## Overview of Project

This project demonstrates real-time hand gesture recognition using cvzone (built on top of MediaPipe) and OpenCV.
It can detect and classify four distinct static gestures:

🖐 Open Palm

✊ Fist

✌ Peace Sign (V-sign)

👍 Thumbs Up

The system uses a webcam feed, performs hand landmark detection, and applies gesture classification logic to recognize the gestures. The recognized gesture is displayed live on the video stream.

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

## Gesture Logic Explanation
We use cvzone.HandDetector to get:

lmList — list of 21 landmark points (each point: (x, y, z) in pixel coords),
<img width="850" height="412" alt="image" src="https://github.com/user-attachments/assets/826c2391-7dc2-4ac8-85c6-4e8803a25949" />

bbox — hand bounding box,

fingersUp(hand) — helper that returns [Thumb, Index, Middle, Ring, Pinky] with 1 = finger up, 0 = finger down.

Using those outputs we classify the required four static gestures with deterministic rules:

### Open Palm

Condition: fingers == [1, 1, 1, 1, 1].

Meaning: all five fingers detected as “up”.

Visual feedback: label "Open Palm" displayed on screen.

### Fist

Condition: fingers == [0, 0, 0, 0, 0].

Meaning: fingertips are near or behind knuckles — all fingers down.

Visual feedback: label "Fist" displayed.

### Peace Sign (V-sign)

Condition: fingers[1:3] == [1, 1] and fingers[3:] == [0, 0]. Thumb is allowed to be either 0 or 1 for tolerance.

Meaning: Index and middle fingers extended, ring and pinky folded.

Visual feedback: label "Peace Sign".

### Thumbs Up

Condition: fingers == [1, 0, 0, 0, 0] and orientation sanity check:

Check that the thumb tip Y coordinate is above the wrist Y coordinate by a small margin (i.e., tip is higher on the screen) — ensures thumb is pointing up, not sideways.

Meaning: only thumb raised and pointing upward.

Visual feedback: label "Thumbs Up".



## OUTPUT
https://github.com/user-attachments/assets/8393e84d-f837-4f69-a351-ad70963bd035



