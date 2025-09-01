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
Other deep learning-based approaches (like YOLO/SSD) would require custom dataset training, which is complex and heavy for simple static gestures. cvzone + MediaPipe provides a ready-to-use, optimized solution for hand tracking and gesture recognition, making it the best choice for this problem.
```

## Gesture Logic Explanation

We detect 21 hand landmarks and classify gestures based on finger states (open/closed).

#### Open Palm 🖐

All five fingers extended.
Checked by comparing fingertip positions with lower joints.

#### Fist ✊

All fingers folded.

Fingertip positions are below the knuckles.

#### Peace Sign ✌

Index and middle finger extended, others folded.

#### Thumbs Up 👍

Only the thumb extended, all other fingers folded.

Additional condition: thumb pointing upward relative to palm.
