#import deez 
from pymavlink import mavutil
from horizon import DEG
from Nombre_3 import master

absolute_angle = abs(DEG)
direction = 0

if DEG < 0:
    direction = -1
else:
    direction = 1

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.MAV_CMD_CONDITION_YAW,
    0, #confirmation
    absolute_angle, #absolute yaw angle
    0, #angular speed
    direction, #clock-wise or counter clock-wise
    0, #relative
    0,0,0
)


