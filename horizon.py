import cv2

def horizon(NOSE, r, l):
    LEFT = False
    RIGHT = False
    SEARCH = False
    IN = False
    DEG = NOSE*37.5 #can use this value for the yaw -> gives this relative to the field of view of the camera
    #print(NOSE)
    if abs(NOSE) < 1:
        if NOSE > r:
            print("RIGHT")
            #print(DEG)
            LEFT = False
            RIGHT = True
            IN = False
        if NOSE < l:            
            print("LEFT")
            #print(DEG)
            RIGHT = False
            LEFT = True
            IN = False
        if (RIGHT == False) and (LEFT == False):
            print("IN")
            IN = True


    else:
        SEARCH = True
        print("SEARCH") #will be search mode -> continue yaw until find nose

    return LEFT, RIGHT, SEARCH, DEG, IN  