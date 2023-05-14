import time
#time.sleep(10)
#local imports
import landmarks as lm
import image_processing as ip
#import machine_learning as ml
import gesture_control as gc
import ERROR_MAN as error
import mav_init as mavinit
import commands as sup
import yaw_tracking as tc
import footage1 as foot
import horizon as hzn
#import land as land

#initialise global variables
boost = False
state = 'Off'
jetson_status = 'Good'


#machinelearn = ml.Machine_learning(0.5, 0.5)
gesturecont = gc.Gesture_control()


####INITIALISATION####
#initialisation of SW system, (error system, check code for errors).
    #initialise subprograms
    #start error logging
state = 'Initialising Software System'
print(state)
# not sure if needed
#initialisation of jetson systems such as port usage and gpu and camera. 
state = 'Initialising Jetson Nano'
print(state)
# not sure if needed
#initialisation of mavlink connection gaining mavlink messages and params. arming.  
    #make connection 
    #read params and messages from fc
    #run param initialisations
    #pre-arm checks
    #arm
state = 'Initialising MAVLINK'
print(state)
#master = mavinit.connect()
#arm = mavinit.arm(master)

#while True:
#    if arm == True:
#        state = 'Armed'
#        print(state)
#        break
#    else:
#        continue
    #move onto SUP
####STARTUP_PROCEDURE####
#start-up procedure/gesture control: check all vital systems on jetson and fc and then take-off, 
# guided by sensors, to searching altitude, search for user by yawing and look for 
# response from user to end start up procedure. yaw tracking should begin once a user is 
# found in order for user to stay in frame.
    #takeoff to altitude. have altitude value to not exceed
    #perform constant yawing in CW direction 
    #stop in place once user is detection

#sup.takeoff(master, 3)

#if sup.ack(master).result == 0:
#########################
camera = ip.camera_init()
timeout = 5

starttime = time.time()

while time.time()<starttime+timeout:

    frame = ip.video_stream(camera)
    foot.videowriter(frame)
	
foot.closevideo()
foot.movefile()
#########################

#state = "Airborne User-Searching"
#print(state)
#camera = ip.camera_init()
#while camera.isopened():
#    frame = ip.video_stream(camera)
#    results = machinelearn.ml_process(frame)
#    landmarks = lm.Landmarks(results)
#    detection = gesturecont.gesture_detection(lm)
#    confidence = gesturecont.confidence(2)
#    sup.yaw(master, 1) #wait time for detection to be registered
#    if detection == "X" and confidence == True: #break sup on detection of user with crossed arms
#        break
#    else:
#        continue

#state = "Airborne User-Tracking"
#print(state)
####TRACKING_CONTROL####
#tracking control: following should occur once a gesture is received that ends start-up    
# procedure. Yaw tracking should continue as well as distance tracking using sensor and 
# attitude targets 
    #monitor users relative yaw to drone
    #monitor users distance to to drone
    # 
#    while camera.isopened():
#        frame = imgprocess.video_stream(jetson_status, camera)
#        results = machinelearn.ml_process(frame)
#        landmarks = lm.Landmarks(results)
#        detection = gesturecont.gesture_detection(lm)
#        confidence = gesturecont.confidence(1) #wait time for detection to be registered
#        hzn.horizon(landmarks.NOSE, 0.125, -0.125)
#        if detection == "i" and confidence == True:
#            tc.tracking()
#            while True:
#                if tc.yaw_tracking_waiting == True:
#                    break
#                else:
#                    continue
#        else:
#            continue
        


####FOOTAGE#### 
#footage recording: once the appropriate gesture is detected, recording of fottage should occur.
#        foot.videowriter(frame)
#        if detection == "B" and confidence == True: #check if both arms up is detected and if so break 
#            break
    #end recording and land if Both hands are up.
#    foot.closevideo()
    #land.land()
#    error.closeerrorfile()
