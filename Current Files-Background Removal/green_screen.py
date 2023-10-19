import cv2
import numpy as np

# Load the video with the green screen
video_capture = cv2.VideoCapture('video_with_green_screen.mp4')

# Create an output video writer with transparency support
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output_video.avi', fourcc, 30, (640, 480), isColor=False)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for green in HSV format
    lower_green = np.array([35, 80, 80])
    upper_green = np.array([85, 255, 255])

    # Create a mask that isolates the green color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Invert the mask to select the non-green pixels
    mask_inv = cv2.bitwise_not(mask)

    # Extract the subject from the frame
    subject = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Set the green screen background to transparent
    frame[np.where(mask > 0)] = [0, 0, 0]

    # Write the frame to the output video
    output.write(frame)

    cv2.imshow('Green Screen Removal', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
output.release()
cv2.destroyAllWindows()
