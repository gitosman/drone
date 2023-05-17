# Authors : Dilan Parjiea
# Description : Program which contains two functions which yaw the drone based on where the user is positioned, and stop yawing when the user is back in frame

from pymavlink import mavutil



def tracking(master, DEG):
    absolute_angle = abs(DEG)
    speed = 0
    if DEG < 0:
        speed = -1
    else:
        speed = 1

    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_CONDITION_YAW,
        0, #confirmation
        absolute_angle, #absolute yaw angle
        speed, #angular speed
        0, #clock-wise or counter clock-wise
        0, #relative
        0,0,0
    )

def yaw_tracking_waiting(master):

    while True:
        message = master.recv_match(type='COMMAND_ACK', blocking=True)
        if message.command == mavutil.MAV_CMD_CONDITION_YAW and message.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
            print("COMPLETE")
            break
        else:
            return False
    return True
 

