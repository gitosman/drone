import cv2
import datetime
import shutil
import image_processing as ip
from pathlib import Path
import time

#define where the video file "result" is saved.
#define the size of the image, this is the same 
#put all of the file stuff in a function


frame_width = 640
frame_height = 480

size = (frame_width, frame_height)

# throughout all programs so it will be a constant here.
#put date and time in the video file name


now = datetime.datetime.now()
localdate = now.strftime(f"%d-%m-%Y")
localtime = now.strftime(f"%H:%M:%S")
filename = str(f"Footage_{localtime}_{localdate}.mp4")


result = cv2.VideoWriter(filename,
			cv2.VideoWriter_fourcc(*'MP4V'),
			38, size)

def videowriter(frame):
	result.write(frame)
	return

def closevideo():
	result.release()
	return

def movefile():
	shutil.move(filename, '/home/kite/Desktop/Test_scripts/video_footage')
	data_file = Path(filename)
	return

#camera = ip.camera_init()
#timeout = 10

#starttime = time.time()

#while time.time()<starttime+timeout:

#	frame = ip.video_stream(camera)
#	videowriter(frame)
	
#closevideo()
#movefile()
