import cv2

# Load the video with the background to be removed
video_capture = cv2.VideoCapture('video_with_background.mp4')

# Load the static background image
background_image = cv2.imread('background.jpg')

# Ensure that the background image and video have the same dimensions
background_image = cv2.resize(background_image, (640, 480))  # Adjust size as needed

# Create an output video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output_video.avi', fourcc, 30, (640, 480))

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize the frame to match the dimensions of the background image
    frame = cv2.resize(frame, (640, 480))

    # Calculate the absolute difference between the current frame and the background
    diff = cv2.absdiff(background_image, frame)

    # Convert the difference to grayscale
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale difference to create a mask
    _, mask = cv2.threshold(diff_gray, 30, 255, cv2.THRESH_BINARY)

    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract the subject from the frame using the mask
    subject = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Write the subject to the output video
    output.write(subject)

    cv2.imshow('Background Removal', subject)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
output.release()
cv2.destroyAllWindows()
