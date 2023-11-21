#takes an image and makes the background transparent

import cv2

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

cap = cv2.VideoCapture('video_with_zoom_green_screen.mp4')
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

currentFrame = 0
while(currentFrame < frames)

    #load image onto opencv
    file_name = "my_video_frame.png" #replace with actual file name or path to file

    #read image
    src = cv2.imread(file_name, 1)

    # Convert image to image gray 
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Applying thresholding technique 
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY) 
  
    # Using cv2.split() to split channels  
    # of coloured image 
    b, g, r = cv2.split(src) 
  
    # Making list of Red, Green, Blue 
    # Channels and alpha 
    rgba = [b, g, r, alpha] 
  
    # Using cv2.merge() to merge rgba 
    # into a coloured/multi-channeled image 
    dst = cv2.merge(rgba, 4) 
  
    # Writing and saving to a new image 
    cv2.imwrite("no_background_frame.png", dst) 

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1