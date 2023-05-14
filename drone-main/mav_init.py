import time
from pymavlink import mavutil
import sys
import math

PAC_NO_RC = 1047998

PAC_NO_GPS_NO_BAT = 1043638


# Functions #


def f_timer_count(start):
    elapsed_time = time.time() - start
    return elapsed_time


def f_att(att):
    global roll
    global pitch
    global yaw
    roll = math.degrees(att.roll)
    pitch = math.degrees(att.pitch)
    yaw = math.degrees(att.yaw)
    return roll, pitch, yaw


# def f_altitude(msg):
#     global altitude
#     if msg:
#         altitude = msg.alt / 1000.0  # Convert altitude from millimeters to meters
#         return altitude


def f_battery(battery):
    global battery_voltage
    if battery is not None:
        battery_voltage = battery.voltage_battery / 1000.0  # Convert millivolts to volts
        return battery_voltage


# Creating connection
connection_string = '/dev/ttyTHS1'  # Change this to the appropriate connection string for your flight controller
baud_rate = 57600

def connect():
    master = mavutil.mavlink_connection(connection_string, baud=baud_rate)
    # # Wait for the connection to be established
    print('Waiting for connection')
    master.wait_heartbeat()
    print('Connection established!')

    # Start timer
    start = time.time()
    print('Time started')
    # Use code below when you need the time
    return master

def arm(master):
    # Request all parameters (#21)
    #master.mav.param_request_read_send(
    #    master.target_system, master.target_component,
    #    b'ARMING_CHECK',
    #    -1
    #)
    #while True:
    #    time.sleep(0.01)
    #    try:
    #        message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
    #        print('name: %s\tvalue: %d' % (message['param_id'],
    #                                       message['param_value']))
    #        break
    #    except Exception as error:
    #        print(error)
    #        sys.exit(0)
    while True:
        if master.motors_armed():
                break
        else:
            master.mav.param_set_send(
            master.target_system, master.target_component,
            b'ARMING_CHECK',
            PAC_NO_GPS_NO_BAT,
            mavutil.mavlink.MAV_PARAM_TYPE_UINT16
            )

    # Pre arm Checks
            master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_RUN_PREARM_CHECKS,
            0, 1, 0, 0, 0, 0, 0, 0
            )
            while True:
                ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
                print("balls")
                if ack_msg and ack_msg.command == mavutil.mavlink.MAV_CMD_RUN_PREARM_CHECKS:
                    if ack_msg.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
                        print("Pre-arm checks initiated successfully.")
                    else:
                        print("Failed to initiate pre-arm checks. Error code: {}".format(ack_msg.result))
                    break

    # Arm the drone
            master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0, 1, 0, 0, 0, 0, 0, 0
            ) 

            # wait until confirmation of arming
            print('Waiting to arm')
            master.motors_armed_wait()
            print('Armed!')
            armed = True
            # mode set
            master.mav.command_long_send(
                master.target_system,
                master.target_component,
                mavutil.mavlink.MAV_CMD_DO_SET_MODE,
                0, 1, 4, 0, 0, 0, 0, 0
            )
            

    return armed

def attitude():
    # Continuously output the attitude of the drone
    
    # ATTITUDE
    attitude = master.recv_match(type='ATTITUDE', blocking=True)
    f_att(attitude)
    print(f'Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}')

    # ALTITUDE (GPS)
    # msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    # f_altitude(msg)
    # print("Altitude: {:.2f} meters".format(altitude))

    # BATTERY
    bat = master.recv_match(type='SYS_STATUS', blocking=True)
    f_battery(bat)
    print("Battery Voltage: {:.2f} V".format(battery_voltage))

def disarm():
    # Disarm
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0, 0, 0, 0, 0, 0, 0, 0
    )
    return

# Can be stopped with Ctrl+C #

