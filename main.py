import cv2
from cvzone.HandTrackingModule import HandDetector

# Open Webcam
cap = cv2.VideoCapture(0)

# Initialize the Hand Detector (Track only one hand)
detector = HandDetector(maxHands=1, detectionCon=0.8)

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect hand and draw landmarks and bounding box
    hands, img = detector.findHands(img)

    gesture = "No Gesture"

    if hands:
        hand = hands[0]

        # Get list of which fingers are up [Thumb, Index, Middle, Ring, Pinky]
        fingers = detector.fingersUp(hand)

        # Defining static gestures based on finger states
        if fingers == [1, 1, 1, 1, 1]:
            gesture = "Open Palm"
        elif fingers == [0, 0, 0, 0, 0]:
            gesture = "Fist"
        elif fingers == [0, 1, 1, 0, 0]:
            gesture = "Peace Sign"
        elif fingers == [1, 0, 0, 0, 0]:
            gesture = "Thumbs Up"

        # Draw a label on the screen with the recognized gesture
        label = f"Gesture: {gesture}"
        cv2.rectangle(img, (10, 10), (370, 50), (0, 0, 0), -1)  # background box
        cv2.putText(img, label, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)

    # Output
    cv2.imshow("Hand Gesture Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
