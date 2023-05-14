import cv2
import time
import nanocamera as nano

#import ERROR_MANAGER as error



		
def camera_init():
        
	#initialise camera.
        camera = nano.Camera(flip=2, width=640	, height=480, fps=120)
        #camera = cv2.VideoCapture(0)
        #get size of image
        
    
        return camera

def video_stream(camera):
            
                
        frame = camera.read()  
                             
        return frame
    
def boost(frame):
        if self.boost == True:
            frame.flags.writeable = False #improves performance?
        else:
            return None
        return #some performance measure

def close_cam(camera):
		# close the camera instance
        camera.release()
		# remove camera object
        del camera
        CAMERAOFF = True
        return CAMERAOFF
