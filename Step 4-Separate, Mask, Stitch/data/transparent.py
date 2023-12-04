import cv2
import numpy as np
import os

try:
    if not os.path.exists('clear_data'):
        os.makedirs('clear_data')
except OSError:
    print ('Error: Creating directory of clear_data')

def make_green_part_transparent(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the green color
    lower_green = np.array([40, 40, 40])  # Adjust as needed
    upper_green = np.array([80, 255, 255])  # Adjust as needed

    # Create a mask for the green color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Create an alpha channel with transparency for the non-green parts
    alpha_channel = np.ones(img.shape[:2], dtype=img.dtype) * 255
    alpha_channel[mask == 255] = 0

    # Add the alpha channel to the original image
    img_bgra = cv2.merge((img, alpha_channel))

    # Save the result with a transparent green part
    return img_bgra

# Example usage:

cap = cv2.VideoCapture('video_with_zoom_green_screen.mp4')
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

currentFrame = 0
while(currentFrame < frames):
    input_image_path = "frame" + str(currentFrame) + ".png"
    #output_image_path = "green.png"
    #make_green_part_transparent(input_image_path)
    name = './clear_data/clear_frame' + str(currentFrame) + '.png'
    print ('Creating...' + name)
    cv2.imwrite(name, make_green_part_transparent(input_image_path))

    # To stop duplicate images
    currentFrame += 1
