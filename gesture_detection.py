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

import pose_classifier
import landmarks

# import Poseclass from command.
cmd = pose_classifier.Poseclass()

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

  # To improve performance, optionally marking the image as not writeable to pass by reference.
  image.flags.writeable = False

  # pass image to models.
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  pose_results = pose.process(image)

  # FPS calculation.
  t1 = time.time()
  fps = 1/(t1 - t0)
  t0 = t1
  fps = int(fps)
  fps = str(fps)
  
  # Draw the pose and FPS annotation on the image.
  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  font = cv2.FONT_HERSHEY_SIMPLEX
  
  mp_drawing.draw_landmarks(
      image,
      pose_results.pose_landmarks,
      mp_pose.POSE_CONNECTIONS,
      landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

  
  # dev tool window plus fps show.
  cv2.putText(image, fps, (7, 70), font, 3, (100, 0, 100), 3, cv2.LINE_AA)
  
  cv2.imshow('MediaPipe Pose', image)
  if cv2.waitKey(5) & 0xFF == 27:
    break

  # check for a detection and proceed accordingly.
  if (pose_results.pose_landmarks is None):
    # call 'search for user' function.
    print("LOST DETECTION")
    continue

  else:
    lm = landmarks.Landmarks(pose_results)
    if lm.NOSE.visibility <= 0.1:
      # call 'search for user' function.
      print("LOST VISIBILITY")
      continue
    else:
      # pass model results to cmd function in Poseclass.
      pose_num = cmd.PoseID(pose_results)
 
cap.release()
cv2.destroyAllWindows()








