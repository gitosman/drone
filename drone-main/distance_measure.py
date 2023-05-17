# Authors : Dilan Parjiea
# Description : Program which takes in the altitude and uses an equation based on previous data to calculate the ground distance from drone to user, and then
############### use trigonometry and pythagoras to calulate the actual distance from the drone to user

from pymavlink import mavutil
from mav_init import master
import math
from horizon import user_diff

# ALTITUDE (Barometer)
# alt = master.recv_match(type='EXTENDED_SYS_STATE', blocking=True)
# if alt:
#     altitude = (1 - (
#             alt.abs_pressure1 / 101325) ** 0.1903) * 145366.45 / 3048.0  # Calculate altitude using barometric pressure
#     print("Altitude: {:.2f} meters".format(altitude))
    


def distance_to_user():
    # ALTITUDE (GPS)
    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    if msg:
        altitude = msg.alt / 1000.0  # Convert altitude from millimeters to meters
        print("Altitude: {:.2f} meters".format(altitude))
    ground_distance = 0
    ground_distance = (user_diff - 0.914766967) / -0.186686873
    distance_to_user = math.sqrt((altitude**2) + (ground_distance**2))
    print(f"Drone to user : {distance_to_user}")
