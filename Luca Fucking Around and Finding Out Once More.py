import time
from pymavlink import mavutil

# Creating connection
connection_string = '/dev/tty/THS1'  # Change this to the appropriate connection string for your flight controller
baud_rate = 57600
master = mavutil.mavlink_connection(connection_string, baud=baud_rate)

# Wait for the connection to be established
print('Waiting for connection')
master.wait_heartbeat()
print('Connection established!')


# Arm the drone (1 or 2)
# 1
master.arducopter_arm()

# 2
# master.mav.command_long_send(
#     master.target_system,
#     master.target_command,
#     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
#     0, 1, 0, 0, 0, 0, 0, 0
# )

# wait until confirmation of arming
print('Waiting to arm')
master.motors_armed_wait()
print('Armed!')

# Continuously output the attitude of the drone
while True:
    msg = master.recv_match(type='ATTITUDE', blocking=True)
    roll = msg.roll
    pitch = msg.pitch
    yaw = msg.yaw
    print(f'Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}')

# Can be stopped with Ctrl+C #

