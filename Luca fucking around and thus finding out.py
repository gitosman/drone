import time
from pymavlink import mavutil

# Set up connection to flight controller
connection_string = '/dev/tty/THS1'  # Change this to the appropriate connection string for your flight controller
baud_rate = 9600  # Change this to the appropriate baud rate for your flight controller
master = mavutil.mavlink_connection(connection_string, baud=baud_rate)

# Wait for the connection to be established
while not master.is_heartbeat_alive():
    print('Waiting for heartbeat...')
    time.sleep(1)

print('Connection established!')

# # Set up the Jetson Nano to receive MAVLink messages
# nano_ip = '192.168.1.10'  # Change this to the IP address of your Jetson Nano
# nano_port = 14550  # Change this to the port number you want to use on the Jetson Nano
# nano_target_system = 1  # Change this to the appropriate target system ID for your system

master.mav.udp_packet(0, 0, 'QGC', 'MAVLink to Jetson Nano')
master.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)


# Perform parameter initialisation
master.param_set_send('SYSID_MYGCS', 1)  # Set the GCS ID to 1
master.param_set_send('ARMING_CHECK', 0)  # Disable arming checks
master.param_set_send('ARMING_REQUIRE', 0)  # Disable arming requirement
master.param_set_send('RC_MAP_ARM_SW', 0)  # Set arm switch to channel 1

# Wait for parameters to be set
time.sleep(1)

# Perform pre-arming checks
while True:
    msg = master.recv_match(type='SYS_STATUS', blocking=True)
    if msg.onboard_control_sensors_enable == 0b1111111111111111:
        break
    else:
        print('Waiting for sensors to be enabled...')
        time.sleep(1)

# Arm the drone
master.arducopter_arm()
print('Drone armed!')

# Continuously output the attitude of the drone
while True:
    msg = master.recv_match(type='ATTITUDE', blocking=True)
    roll = msg.roll
    pitch = msg.pitch
    yaw = msg.yaw
    print(f'Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}')

# Can be stopped with Ctrl+C

# # Count down
# i: int = 0
# while True:
#     print(i)
#     i = i + 1
#     time.sleep(1)
#     if i == 10:
#         break
#
# #Disarm the Drone
# master.arducopter_disarm()
# print('Drone Disamed')

# # Set up the Jetson Nano as a receiver
# master.mav.mission_request_list_send(nano_target_system, 1)
#
# # Start receiving messages from the flight controller and forwarding them to the Jetson Nano
# while True:
#     msg = master.recv_match()
#     if not msg:
#         continue
#     master.mav.send(msg)
