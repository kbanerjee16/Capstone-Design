#explore capabilities of opencv
#goal: Demonstrate recording and storing a video with OpenCV then play that stored video

import cv2
import numpy as np

video = cv2.VideoCapture(0)
if (video.isOpened() == False): 
    print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))
   
size = (frame_width, frame_height)

result = cv2.VideoWriter('bikerace.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

while(True):
    ret, frame = video.read()
  
    if ret == True: 
  
        # Write the frame into the
        # file 'filename.avi'
        result.write(frame)
  
        # Display the frame
        # saved in the file
        cv2.imshow('Frame', frame)
  
        # Press S on keyboard 
        # to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
  
    # Break the loop
    else:
        break

video.release()
result.release()
    
cap = cv2.VideoCapture('bikerace.avi')
  
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")
  
# Read until video is completed
while(cap.isOpened()):
      
# Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Frame', frame)
          
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
  
# Break the loop
    else:
        break
  
# When everything done, release
# the video capture object
cap.release()
  
# Closes all the frames
cv2.destroyAllWindows()