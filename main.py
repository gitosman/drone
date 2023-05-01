
#local imports
import landmarks as lm
import image_processing as ip
import machine_learning as ml
import gesture_control as gc
import ERROR_MAN as error
import mav_init as mavinit
from mav_init import master
import sup as sup
import yaw_tracking as tc
import footage as foot
import horizon as hzn
#import land as land

#initialise global variables
boost = False
state = 'Off'
jetson_status = 'Good'

imgprocess = ip.Image_processing(boost)
machinelearn = ml.Machine_learning(0.5, 0.5)
gesturecont = gc.Gesture_control()

if __name__ == '__main__':
    #configuration parameters can be fed to their respective programs before running.
    print()

####INITIALISATION####
#initialisation of SW system, (error system, check code for errors).
    #initialise subprograms
    #start error logging
state = 'Initialising Software System'
# not sure if needed
#initialisation of jetson systems such as port usage and gpu and camera. 
state = 'Initialising Jetson Nano'
# not sure if needed
#initialisation of mavlink connection gaining mavlink messages and params. arming.  
    #make connection 
    #read params and messages from fc
    #run param initialisations
    #pre-arm checks
    #arm
state = 'Initialising MAVLINK'
mavinit.mavinit()
if master.isarmed() == False:
    error.arming_error()
else:
    state = 'Armed'
    #move onto SUP
####STARTUP_PROCEDURE####
#start-up procedure/gesture control: check all vital systems on jetson and fc and then take-off, 
# guided by sensors, to searching altitude, search for user by yawing and look for 
# response from user to end start up procedure. yaw tracking should begin once a user is 
# found in order for user to stay in frame.
    #takeoff to altitude. have altitude value to not exceed
    #perform constant yawing in CW direction 
    #stop in place once user is detection

    sup.takeoff()#needs truning into functions and removing infinite loops

    state = "Airborne User-Searching"
    camera = imgprocess.camera_init(jetson_status)
    while camera.isopened():
        frame = imgprocess.video_stream(jetson_status, camera)
        results = machinelearn.ml_process(frame)
        landmarks = lm.Landmarks(results)
        detection = gesturecont.gesture_detection(lm)
        confidence = gesturecont.confidence(2)
        sup.yaw() #wait time for detection to be registered
        if detection == "X" and confidence == True: #break sup on detection of user with crossed arms
            break
        else:
            continue
    state = "Airborne User-Tracking"
####TRACKING_CONTROL####
#tracking control: following should occur once a gesture is received that ends start-up    
# procedure. Yaw tracking should continue as well as distance tracking using sensor and 
# attitude targets 
    #monitor users relative yaw to drone
    #monitor users distance to to drone
    # 
    while camera.isopened():
        frame = imgprocess.video_stream(jetson_status, camera)
        results = machinelearn.ml_process(frame)
        landmarks = lm.Landmarks(results)
        detection = gesturecont.gesture_detection(lm)
        confidence = gesturecont.confidence(1) #wait time for detection to be registered
        hzn.horizon(landmarks.NOSE, 0.125, -0.125)
        if detection == "i" and confidence == True:
            tc.tracking()
            while True:
                if tc.yaw_tracking_waiting == True:
                    break
                else:
                    continue
        else:
            continue
        


####FOOTAGE#### 
#footage recording: once the appropriate gesture is detected, recording of fottage should occur.
        foot.videowriter(frame)
        if detection == "B" and confidence == True: #check if both arms up is detected and if so break 
            break
    #end recording and land if Both hands are up.
    foot.closevideo()
    #land.land()
    error.closeerrorfile()