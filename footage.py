import cv2
import datetime
from image_processing import Image_processing as im_proc

#define where the video file "result" is saved.
filepath ='/home/kite/video_footage/'
#define the size of the image, this is the same 

frame_width = im_proc.width
frame_height = im_proc.height
   
size = (frame_width, frame_height)

# throughout all programs so it will be a constant here.
#put date and time in the video file name
localdatetime = datetime.datetime.localdatetime()
localdate = localdatetime.strftime(f"%d-%m-%Y")
localtime = localdatetime.strftime(f"%H:%M:%S")

filename = str(f"{filepath}Footage_{localtime}_{localdate}")
result = cv2.VideoWriter(filename, 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

def videowriter(frame):
    result.write(frame)
    return

def closevideo():
    result.release()
    return

