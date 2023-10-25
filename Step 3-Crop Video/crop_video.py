import cv2

# Function to crop black pixels from a frame
def crop_black_pixels(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create a mask for black pixels (threshold for low-intensity values)
    mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)[1]

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize an empty list to store the cropped regions
    cropped_regions = []

    # Iterate through the contours and crop non-black regions
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 10 and h > 10:  # Define a minimum size for the region to be considered
            cropped_region = frame[y:y+h, x:x+w]
            cropped_regions.append(cropped_region)

    return cropped_regions

# Open the video file
video_capture = cv2.VideoCapture('output_video.avi')

# Get video frame dimensions
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))

# Create a VideoWriter object to save the output video with 'mp4v' codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = 'cropped_video.avi'
out = cv2.VideoWriter(output_video, fourcc, 30, (frame_width, frame_height), isColor=True)

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
#cropped_video_capture = cv2.VideoCapture('cropped_video.mp4')

while True:
    ret, frame = output_video.read()
    if not ret:
        break

    cv2.imshow('Cropped Video', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the cropped video capture and close the display window
cropped_video_capture.release()
cv2.destroyAllWindows()

