import cv2

def horizon(NOSE, r, l):
    LEFT = False
    RIGHT = False
    SEARCH = False
    IN = False
    DEG = NOSE*37.5 #can use this value for the yaw -> gives this relative to the field of view of the camera
    #print(NOSE)
    if abs(NOSE) < 1:
        if (RIGHT == False) and (LEFT == False):
            print("IN")
            IN = True
        if NOSE > r:
            print("RIGHT")
            LEFT = False
            RIGHT = True
        if NOSE < l:            
            print("LEFT")
            RIGHT = False
            LEFT = True


    else:
        SEARCH = True
        print("SEARCH") #will be search mode -> continue yaw until find nose

    return LEFT, RIGHT, IN, SEARCH, DEG 