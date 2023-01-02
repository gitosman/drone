######################################
### Author: Peter Richards 
### Date: 02/01/2023 
### Name: landmarks
### Description: contains Landmarks class which is used to refer to each landmark in the pose model outputs in a simpler and more intuitive way.
######################################

import mediapipe as mp
mp_pose = mp.solutions.pose
class Landmarks():
    def __init__(self, results):
        self.NOSE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
        self.LEYI = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER]
        self.LEYE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE]
        self.LEYO = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER]
        self.REYI = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER]
        self.REYE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE]
        self.REYO = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE_OUTER]
        self.LEAR = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR]
        self.REAR = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR]
        self.LMTH = results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_LEFT]
        self.RMTH = results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT]
        self.LSDR = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        self.RSDR = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        self.LLBW = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        self.RLBW = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
        self.LWST = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        self.RWST = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        self.LPNK = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY]
        self.RPNK = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY]
        self.LIDX = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX]
        self.RIDX = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX]
        self.LTHM = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB]
        self.RTHM = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB]
        self.LHIP = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        self.RHIP = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
        self.LKNE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
        self.RKNE = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
        self.LANK = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE]
        self.RANK = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE]
        self.LHEL = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL]
        self.RHEL = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL]
        self.LFIX = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
        self.RFIX = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
            