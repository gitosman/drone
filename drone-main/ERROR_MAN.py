import datetime
from pymavlink import mavutil


f = open("error.txt", "a")
now = datetime.datetime.now()
date = now.strftime(f"%d-%m-%Y")
error_time = now.strftime(f"%H:%M:%S")
f.write(date)
 
#camera error
def camera_error():
        
    f.write("Camera error at {error_time}")
    
#storage error
def storage_error():

    f.write("Storage error at {error_time}")

#altitude error -> goes above a certain altitude
def altitude_error():

    f.write("Altitude error at {error_time}")

#ML error
def ml_error():

    f.write("ML error at {error_time}")


#Jetson error
def jetson_error():

    f.write("Jetson error at {error_time}")


#ardupilot error
def ardupilot_error():

    f.write("Ardupilot error at {error_time}")

def arming_error():
        
    f.write("Arming error at {error_time}")
       
def disarming_error():
        
    f.write("Disarming error at {error_time}")
        
f.close()
