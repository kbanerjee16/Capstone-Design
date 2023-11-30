import cv2
import numpy as np

def make_green_part_transparent(image_path, output_path):
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
    cv2.imwrite(output_path, img_bgra)

# Example usage:
input_image_path = "frame2.png"
output_image_path = "green.png"
make_green_part_transparent(input_image_path, output_image_path)
