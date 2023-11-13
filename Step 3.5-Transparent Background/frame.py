#extracts frames and shows them in a window
#press 0 to move to next frame
import cv2

def transparant():
    #load image onto opencv
    file_name = "one_frame.png"

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

    return dst

video = cv2.VideoCapture('output_video.avi')#something is wrong with the output video

frames = video.get(cv2.CAP_PROP_FRAME_COUNT)#it's giving me too many frames
print('total frames = ', frames)
fps = video.get(cv2.CAP_PROP_FPS)
count = 0
while count < frames :
    frame_id = int(fps*count)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()
    cv2.imshow('frame', frame); cv2.waitKey(0)
    #make transparant here
    cv2.imwrite('one_frame.png', frame)

    cv2.imshow('transparent_frame', transparant()); cv2.waitKey(0)
    count +=1

#for each frame
    #separate the background from the human
    #remove the backgroud/remove everything but the dancer from the frame