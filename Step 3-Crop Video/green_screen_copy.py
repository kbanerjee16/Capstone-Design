import cv2
import numpy as np

# Load the video file
input_video = 'video_with_zoom_green_screen.mp4'
cap = cv2.VideoCapture(input_video)

# Define the lower and upper bounds for the green screen color (in HSV format)
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to identify the green screen area
    mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    # Invert the mask (black-out the green screen)
    mask_inv = cv2.bitwise_not(mask)

    # Create a solid black background
    black_background = np.zeros_like(frame)

    # Extract the subject (foreground) from the frame
    subject = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine the subject with the black background
    result = cv2.add(subject, black_background)

    cv2.imshow('Green Screen Removal', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
