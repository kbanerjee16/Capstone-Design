#crops black pixels as it turns the green screen background black, but there is a problem with it
#repeats the video which is good

import cv2
import numpy as np

# Load the video file
input_video = 'video_with_zoom_green_screen.mp4'
cap = cv2.VideoCapture(input_video)

# Define the lower and upper bounds for the green screen color (in HSV format)
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# Get video frame dimensions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create a VideoWriter to save the cropped video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = 'output_video.avi'
out = cv2.VideoWriter(output_video, fourcc, 30, (frame_width, frame_height), isColor=True)

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

    # Crop out the black pixels
    result = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Write the cropped frame to the output video
    out.write(result)

    cv2.imshow('Cropped Video', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()

# Open the cropped video for playing
output_cap = cv2.VideoCapture(output_video)

while True:
    ret, frame = output_cap.read()
    if not ret:
        break

    cv2.imshow('Cropped Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

output_cap.release()
cv2.destroyAllWindows()
