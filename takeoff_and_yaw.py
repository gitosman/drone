from pymavlink import mavutil

alt = 2 #in meters
yaw_speed = 0.4 # in rad/s

# Start a connection listening to a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))

#arms the drone
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)

#Acknowledges the previous message, and returns data about it
msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)

#Takes the drone off to an altitude of 2m
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, alt)

alt = -alt

#Acknowledges the previous message, and returns data about it
msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)

while 1:
    altitude = the_connection.recv_match(
    type='LOCAL_POSITION_NED', blocking=True)

    if altitude.z < alt+0.1:

       while 1:
             the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, 
                                the_connection.target_system,
                                the_connection.target_component,
                                 mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
                                 int(0b010111111110),
                                 0, 0, alt, 0, 0, 0, 0, 0, 0, 0, yaw_speed))

