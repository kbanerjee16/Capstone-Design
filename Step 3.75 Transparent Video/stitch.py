import cv2
import numpy as np

# Load the two images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# Make sure both images have the same dimensions
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# Specify the output video file and its properties
output_video_path = 'output_video.avi'
fps = 1  # Frames per second
width, height = image1.shape[1], image1.shape[0]
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Write the images to the video file
video_writer.write(image1) #replace image1 with path to image
video_writer.write(image2) #replace image2 with path to image

# Release the video writer
video_writer.release()

# Optional: Display the video
cap = cv2.VideoCapture(output_video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Combined Video', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1000 // fps) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
