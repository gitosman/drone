import cv2
import datetime
import shutil
from image_processing import Image_processing as im_proc
from pathlib import Path

#define where the video file "result" is saved.
#filepath ='/home/kite/video_footage/'
#define the size of the image, this is the same 
#put all of the file stuff in a function

frame_width = im_proc.width
frame_height = im_proc.height
   
size = (frame_width, frame_height)

# throughout all programs so it will be a constant here.
#put date and time in the video file name


now = datetime.datetime.now()
localdate = now.strftime(f"%d-%m-%Y")
localtime = now.strftime(f"%H:%M:%S")
filename = str(f"footage.mp4")


#filename = str(f"{filepath}Footage_{localtime}_{localdate}.mp4")
result = cv2.VideoWriter(filename, 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
shutil.move('footage.mp4', 'video_footage/')

data_file = Path('footage.mp4')
data_file.rename(str(f"Footage_{localtime}_{localdate}.mp4"))

def videowriter(frame):
    result.write(frame)
    return

def closevideo():
    result.release()
    return

