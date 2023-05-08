from pymavlink import mavutil
from distance_measure import distance_to_user
from mav_init import master
import time
import Eulertoquat as euler

def distance_movement():

    distance_range_lower = 1
    distance_range_upper = 10

    if distance_to_user < distance_range_lower:
        pitch = -0.5
        
        master.mav.command_long_send(
            mavutil.time_boot_ms,
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_SET_ATTITUDE_TARGET,
            int(0b000011100101), #bitmask to ignore roll rate, yaw rate, body thrust, throttle and attitude
            euler.euler_to_quat(pitch), # quaternion
            0, #roll rate
            -0.5, # pitch rate
            0, #yaw rate
            0, #thrust
            0 #thrust_body 
        )
    elif distance_to_user > distance_range_upper:
        pitch = 0.5
        
        master.mav.command_long_send(
            mavutil.time_boot_ms,
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_SET_ATTITUDE_TARGET,
            int(0b000011100101), #bitmask to ignore roll rate, yaw rate, body thrust, throttle and attitude
            euler.euler_to_quat(pitch), # quaternion
            0, #roll rate
            0.5, # pitch rate
            0, #yaw rate
            0, #thrust
            0 #thrust_body 
        )

    else:
        pitch = 0
        
        master.mav.command_long_send(
            mavutil.time_boot_ms,
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_SET_ATTITUDE_TARGET,
            int(0b000011100101), #bitmask to ignore roll rate, yaw rate, body thrust, throttle and attitude
            euler.euler_to_quat(pitch), # quaternion
            0, #roll rate
            0, # pitch rate
            0, #yaw rate
            0, #thrust
            0 #thrust_body 
        )
