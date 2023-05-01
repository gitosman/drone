import cv2
import time
#import nanocamera as nano

#import ERROR_MANAGER as error

class Image_processing(object):

    def __init__(self, boost):
        self.boost = boost
        camera = None
        frame = None
        CAMERAOFF = True
        CAMERAON = False
        camera_error = False
        video_error = False
        self.height = 0
        self.width = 0
		
    def camera_init(self, jetson_status):
        if jetson_status == 'LOW_VOLTAGE': #OR ANY OTHER LIMITING FACTOR
            #error.urgent.CAM_FAILURE = True
            camera_error = True
			
        else:
			#initialise camera.
            #camera = nano.Camera(flip=0, width=640, height=480, fps=120)
            camera = cv2.VideoCapture(0)
            #get size of image
            self.height = int(camera.get(4))
            self.width = int(camera.get(3))
            
            CAMERAON = True

        return camera

    def video_stream(self, jetson_status, camera):
            if camera.isOpened():
                success, frame = camera.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                else:   
                
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    
                    cv2.imshow("Video Frame", frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        camera.release()
                        cv2.destroyAllWindows  
                             
            return frame
    
    def boost(self, frame):
        if self.boost == True:
            frame.flags.writeable = False #improves performance?
        else:
            return None
        return #some performance measure

    def close_cam(self, camera):
		# close the camera instance
        camera.release()
		# remove camera object
        del camera
        CAMERAOFF = True
        return CAMERAOFF