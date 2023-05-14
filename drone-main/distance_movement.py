from pymavlink import mavutil
import time
from mav_init import master
from distance_measure import distance_to_user

def distance_movement():

    range_lower = 1
    range_upper = 10
    distance_to_lower = distance_to_user - range_lower
    distance_to_upper = distance_to_user - range_upper

    if distance_to_user < range_lower:

         master.mav.command_long_send(
            10,
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_SET_POSITION_TARGET_LOCAL_NED,
            0,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            int(0b110111110110), #ignores everything that isn't in the direction to move forwards or backward
            distance_to_lower,
            0,0,
            1, #1m/s
            0,0,0,0,0,0,0
         )
    
    elif distance_to_user > range_upper:

        master.mav.command_long_send(
        10,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_SET_POSITION_TARGET_LOCAL_NED,
        0,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        int(0b110111110110), #ignores everything that isn't in the direction to move forwards or backward
        distance_to_upper,
        0,0,
        1, #1m/s
        0,0,0,0,0,0,0
        )       
    
    else:

        master.mav.command_long_send(
        10,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_SET_POSITION_TARGET_LOCAL_NED,
        0,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        int(0b111111111111), #ignores everything 
        0,
        0,0,
        0, 
        0,0,0,0,0,0,0
    )  
