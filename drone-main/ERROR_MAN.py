# Authors : Dilan Parjiea
# Description : Program which writes to a text file which logs any errors which could occur, with these error functions being called up by other programs

import datetime
from pymavlink import mavutil


f = open("error.txt", "a")
now = datetime.datetime.now()
date = now.strftime(f"%d-%m-%Y")
error_time = now.strftime(f"%H:%M:%S")
f.write(date)
f.write("\n") 
 
#camera error
def camera_error():
        
    f.write("Camera error at {error_time}\n")
    
#storage error
def storage_error():

    f.write("Storage error at {error_time}\n")

#altitude error -> goes above a certain altitude
def altitude_error():

    f.write("Altitude error at {error_time}\n")

#ML error
def ml_error():

    f.write("ML error at {error_time}\n")


#Jetson error
def jetson_error():

    f.write("Jetson error at {error_time}\n")


#ardupilot error
def ardupilot_error():

    f.write("Ardupilot error at {error_time}\n")

def arming_error():
        
    f.write("Arming error at {error_time}\n")
       
def disarming_error():
        
    f.write("Disarming error at {error_time}\n")
        
f.close()
