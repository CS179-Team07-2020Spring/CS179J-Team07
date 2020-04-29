from jetbot import Robot        #use jetbot provide function to control the basic movement of the robot
import math


def simple_PL(x,y):     #input a coordinate to travel to, +x = go to right, +y = go straight

    curr_x = 0          #use to keep track on the x of the car current status
    curr_y = 0          #use to keep track on the y of the car current status
    curr_angle = 0      #use to keep track on the angle of the car current status, range from -180 to 180. 0 indicate straight

    robot = Robot()     #init the class 

    #need to care about two case, if there is no object case and if there is object in front case

    #if no object
    while(no_object()):     #use to check is there object in front

        while(curr_angle != convert_angle(x - curr_x , y - curr_y) )
    

def convert_angle(x,y):
    if(y = 0):      #special case when y = 0 
        if(x = 0):          #reach the destination
            return None
        else if(x > 0):     
            return 90
        else:
            return -90

    if(y > 0):
        temp = x/y
        temp2 = math.degrees(math.atan(temp))
        