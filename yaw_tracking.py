# Authors : Dilan Parjiea

from pymavlink import mavutil
from horizon import DEG
from mav_init import master

def tracking():
    absolute_angle = abs(DEG)
    direction = 0

    if DEG < 0:
        direction = -1
    else:
        direction = 1

    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_CONDITION_YAW,
        0, #confirmation
        absolute_angle, #absolute yaw angle
        0, #angular speed
        direction, #clock-wise or counter clock-wise
        0, #relative
        0,0,0
    )

def yaw_tracking_waiting():

    while True:
        message = master.recv_match(type='COMMAND_ACK', blocking=True)
        if message.command == mavutil.MAV_CMD_CONDITION_YAW and message.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
            print("COMPLETE")
            break
        else:
            return False
    return True
 

