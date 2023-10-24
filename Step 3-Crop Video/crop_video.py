import cv2

# Function to crop black pixels from a frame
def crop_black_pixels(frame):
    # (Your cropping function remains the same)

# Open the video file
video_capture = cv2.VideoCapture('no_background_video.mp4')

# Create a VideoWriter object to save the output video with 'mp4v' codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('cropped_video.mp4', fourcc, 30, (640, 480))

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    cropped_regions = crop_black_pixels(frame)

    for region in cropped_regions:
        output_video.write(region)

# Release the video capture and writer objects
video_capture.release()
output_video.release()

# Open the cropped video for playing
cropped_video_capture = cv2.VideoCapture('cropped_video.mp4')

while True:
    ret, frame = cropped_video_capture.read()
    if not ret:
        break

    cv2.imshow('Cropped Video', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the cropped video capture and close the display window
cropped_video_capture.release()
cv2.destroyAllWindows()

