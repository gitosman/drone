import datetime
from pymavlink import mavutil


f = open("error.txt", "w")
now = datetime.datetime.now()
date = now.strftime(f"%d-%m-%Y")
error_time = now.strftime(f"%H:%M:%S")
f.write(date)

class CRITICAL(object):
    def __init__(self, module):
        self.module = module
    
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

class URGENT(object):
    def __init__(self, module):
        self.module = module

    #Jetson error
    def jetson_error():

        f.write("Jetson error at {error_time}")

class SERIOUS(object):
    def __init__(self, module):
        self.module = module

    #ardupilot error
    def ardupilot_error():

        f.write("Ardupilot error at {error_time}")


f.close()
