import cv2
import time
import nanocamera as nano

import ERROR_MANAGER as error

class Image_processing():

	def __init__(self):
		camera = None
		CAMERAOFF = True
		CAMERAON = False
		



	def camera_init(self, jetson_status):
		if jetson_status != LOW_VOLTAGE #OR ANY OTHER LIMITING FACTOR
			#initialise camera.
			camera = nano.Camera(flip=0, width=640, height=480, fps=120)
			CAMERAON = True
		else:
			
    			error.urgent.cam_failure = True
			
	return camera, CAMERAON



	def video_stream(self, cam_error, jetson_status, camera):
		while True:
			try:
				# read the camera image
				frame = camera.read()
				#display the frame
				#cv2.imshow("Video Frame", frame)
				#if cv2.waitKey(25) & 0xFF == ord('q'):
				#	break
			#except KeyboardInterrupt:
				#break

	return frame



	def close_cam(self, camera)
		# close the camera instance
		camera.release()
		# remove camera object
		del camera
		CAMERAOFF = True
	return CAMERAOFF

