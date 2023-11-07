import cv2
import numpy as np

# Load the video with the green screen
video_capture = cv2.VideoCapture('video_with_zoom_green_screen.mp4')

# Get the video's width, height, and frames per second
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))
fps = int(video_capture.get(5))

# Define the codec and create an output video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output_video.avi', fourcc, fps, (frame_width, frame_height), isColor=True)

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

    # Create a black background frame
    black_background = np.zeros_like(frame, dtype=np.uint8)

    # Combine the subject and black background to make the green screen background black
    result_frame = cv2.add(subject, black_background)

    # Write the frame to the output video
    output.write(result_frame)

    cv2.imshow('Green Screen Removal', result_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
output.release()
cv2.destroyAllWindows()
