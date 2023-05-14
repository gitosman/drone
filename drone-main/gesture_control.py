import time


class Gesture_control(object):
    def __init__(self):
        return
    def gesture_detection(self, lm):
        # check visibility of user wrists to determine if idle.
        if lm != None:
            if ((lm.LWST.visibility > 0.5) or (lm.RWST.visibility > 0.5)):
                
                # check for each of the 5 other positions.
                    if (((lm.LWST.y < lm.LLBW.y) and (lm.RWST.y < lm.RLBW.y)) and 
                    ((lm.LWST.x < lm.RWST.x) and (lm.RWST.x > lm.LWST.x))):
                            pose_char = "X"
                            print("crossed arms",end="\r")
                
                    elif ((lm.LWST.y < lm.LSDR.y) and (lm.RWST.y < lm.RSDR.y)):
                            pose_char = "B"
                            print("both arms up",end="\r")
                
                    elif ((lm.RWST.y < lm.RSDR.y) and (lm.LWST.y > lm.LSDR.y)):
                            pose_char = "R"
                            print("right arm up",end="\r")
                
                    elif ((lm.LWST.y < lm.LSDR.y) and (lm.RWST.y > lm.RSDR.y)):
                            pose_char = "L"
                            print("left arm up",end="\r")
                
                    elif (lm.LLBW.y >= lm.LSDR.y) and (lm.RLBW.y >= lm.RSDR.y):
                            pose_char = "i"
                            print("idle",end="\r")
                    else:
                            pose_char = "N"
                            print("NO_USER",end="\r")
            else:
                pose_char = "i"
                print("idle",end="\r")

        else:
            pose_char = "N"
            print("NO_USER",end="\r")
            
            return pose_char
    
    def confidence(self, pose_char, wait_time_sec):
        
        pastpose = pose_char
        time.sleep(wait_time_sec)
        currentpose = pose_char
        if pastpose == currentpose:
            
            confident = True
        else:
            
            confident = False

        return confident