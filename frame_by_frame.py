#extracts frames and shows them in a window
#press 0 to move to next frame
import cv2

video = cv2.VideoCapture('filename.avi')

frames = video.get(cv2.CAP_PROP_FRAME_COUNT)#it's giving me too many frames
print('total frames = ', frames)
fps = video.get(cv2.CAP_PROP_FPS)
count = 0
while count < 8 :
    frame_id = int(fps*count)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()
    cv2.imshow('frame', frame); cv2.waitKey(0)
    cv2.imwrite('my_video_frame.png', frame) 
    count +=1

#for each frame
    #separate the background from the human
    #remove the backgroud/remove everything but the dancer from the frame