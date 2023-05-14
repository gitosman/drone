######################################
### Author: Peter Richards 
### Date: 02/01/2023 
### Name: gesture_detection
### Description: gesture detection class using MediaPipe Pose model with PyTorch framework
### including full annotations. Working in the presence of occlusion and lack of human in frame. including FPS counter.
######################################
import mediapipe as mp
import cv2 
import time 
import numpy as np

import pose_classifier
import landmarks
import horizon

# import Poseclass from command.
cmd = pose_classifier.Poseclass()
hzn = horizon


# access pose model and drawing tools.
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# choose camera: Number | Camera
#                     0 | Front facing camera 
#                     1 | Rear facing camera
cap = cv2.VideoCapture(0)

# initialise pose model to required mode.
pose =  mp_pose.Pose(min_detection_confidence=0.5, 
                    min_tracking_confidence=0.5,
                    static_image_mode=False,
                    model_complexity=1,
                    smooth_landmarks=True,
                    enable_segmentation=False,
                    smooth_segmentation=True,)  

# initialise fps variables.
t0 = 0
t1 = 0      


# begin video processing.
while cap.isOpened():
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    # If loading a video, use 'break' instead of 'continue'.
    continue
  dimensions = image.shape
  w = dimensions[1]
  h = dimensions[0]

  # To improve performance, optionally marking the image as not writeable to pass by reference.
  image.flags.writeable = False

  # pass image to models.

  
  ret, frame = cap.read()
  width = int(cap.get(3))
  height = int(cap.get(4))

  img = cv2.line(frame, ((width//2)-40, 0), ((width//2)-40, height), (255, 0, 0), 5)
  img2 = cv2.line(frame, ((width//2)+40, 0), ((width//2)+40, height), (255, 0, 0), 5)

  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  pose_results = pose.process(image)

  if (pose_results.pose_landmarks is None):
    # call 'search for user' function.
    print("LOST DETECTION")
    continue


  lm = landmarks.Landmarks(pose_results)
  mp_drawing.draw_landmarks(
      frame,
      pose_results.pose_landmarks,
      mp_pose.POSE_CONNECTIONS,
      landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
      
  RIGHT = False
  LEFT = False
  NOSE = ((lm.NOSE.x) - 0.5)*2
  r = 0.125
  l = -0.125
  pose_results = pose.process(image)
  cv2.imshow('frame', frame)

  hzn.horizon(NOSE, r, l)

  if cv2.waitKey(1) & 0xFF == 27:
    break

cv2.destroyAllWindows()
cap.release()





