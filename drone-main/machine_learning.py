import mediapipe as mp
import time
import landmarks
#import ERROR_MANAGER as error

class Machine_learning(object):

    def __init__(self, detect_conf, track_conf):
        mp_pose = mp.solutions.pose
        mp_drawing = mp.solutions.drawing_utils
        self.pose =  mp_pose.Pose(min_detection_confidence=detect_conf, #0.5 default
                    min_tracking_confidence=track_conf, #0.5 default
                    static_image_mode=False,
                    model_complexity=1,
                    )
        pose_results = None
        

    def ml_process(self, frame):
        start = time.time()
        pose_results = self.pose.process(frame)
        end = time.time()
        compute_time = (end - start)

        return pose_results #, compute_time

    #def gpu_accel
    def landmarks(self, pose_results):
        if (pose_results.pose_landmarks is None):
            #error.urgent.LOST_USER
            print("LOST DETECTION")

        else:
            lm = landmarks.Landmarks(pose_results)

        return lm #, internal error
