######################################
### Author: Peter Richards 
### Date: 02/01/2023 
### Name: pose_classifier sandbox
### Description: *** USE AS EXPERIMENTAL PLAYGROUND FOR WORKING ON 'pose_classifier' ***
### contains 'Poseclass' class. containing 'PoseID' function which returns the current user pose as a string when given the results from pose.process.
### to be used as control signals to the drone control module.
###
###                     Pose | pose_char
###             -------------|---------
###             Crossed arms | X
###             Both arms up | B
###             Right arm up | R
###             Left arm up  | L
###             idle         | i
###             NO_USER      | N
###
######################################
import mediapipe as mp
import landmarks

mp_pose = mp.solutions.pose

class Poseclass():
    def __init__(self):
       self.pose_char = None
    
    def PoseID(self, results):

        # import Lanmdmarks class as lm.
        lm = landmarks.Landmarks(results)

        # check visibility of user wrists to determine idle position or other.
        if ((lm.LWST.visibility > 0.5) or (lm.RWST.visibility > 0.5)):
            
            # check for each of the 5 other positions.
                if (((lm.LWST.y < lm.LLBW.y) and (lm.RWST.y < lm.RLBW.y)) and 
                ((lm.LWST.x < lm.RWST.x) and (lm.RWST.x > lm.LWST.x))):
                        pose_char = "X"
                        print("crossed arms")
            
                elif ((lm.LWST.y < lm.LSDR.y) and (lm.RWST.y < lm.RSDR.y)):
                        pose_char = "B"
                        print("both arms up")
            
                elif ((lm.RWST.y < lm.RSDR.y) and (lm.LWST.y > lm.LSDR.y)):
                        pose_char = "R"
                        print("right arm up")
            
                elif ((lm.LWST.y < lm.LSDR.y) and (lm.RWST.y > lm.RSDR.y)):
                        pose_char = "L"
                        print("left arm up")
            
                elif (lm.LLBW.y >= lm.LSDR.y) and (lm.RLBW.y >= lm.RSDR.y):
                        pose_char = "i"
                        print("idle")
                else:
                        pose_char = "N"
                        print("NO_USER")
        else:
            pose_char = "i"
            print("idle")
        
        # return current pose.
        return pose_char


    





    
