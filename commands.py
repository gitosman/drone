from pymavlink import mavutil
from mav_init import master

def land(): #Lands the drone at its current x,y position
    master.mav.command_long_send(master.target_system, master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_LAND,0, 0, 0, 0, 0, 0, 0, 0)

def takeoff(alt): #Takes off at the desired altitude, the vehicle must be armed and in guided mode for a successfull launch
    master.mav.command_long_send(master.target_system, master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, alt)

def yaw(yaw_speed): #Yaws 180 degrees at the specified yaw speed in rad/s, this function is subject to change
    master.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, 
                                master.target_system,
                                master.target_component,
                                 mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
                                 int(0b010000111111),
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, yaw_speed))

def ack(): #Call the function after sending a command, to receive feedback about it, can't acknowledge yaw()
    msg = master.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)