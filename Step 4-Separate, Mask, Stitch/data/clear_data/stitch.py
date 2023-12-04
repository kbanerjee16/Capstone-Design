import cv2
import numpy as np

#cap = cv2.VideoCapture('video_with_zoom_green_screen.mp4')
#frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Load the two images
image1 = cv2.imread('clear_frame3.png')


#cv2.imshow("one image", image1)

# Specify the output video file and its properties
output_video_path = 'output_video.mov'  # Change the file extension to .mov
fps = 15 #cap.get(cv2.CAP_PROP_FPS)  # Frames per second
width, height = image1.shape[1], image1.shape[0]
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for .mov format
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Write the images to the video file
currentFrame = 0
while currentFrame < 923:
    image = cv2.imread("clear_frame" + str(currentFrame) + ".png")
    video_writer.write(image)
    currentFrame += 1

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
    if cv2.waitKey(1000 // int(fps)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
