from jetbot import Robot        #use jetbot provide function to control the basic movement of the robot
import math
from time import sleep

#need to implement function:
    #no_object() : use to return true or false depend is object detect within a range
    #update_info() : use to update the information of the current location, input needed: curr_x, curr_y, curr_angle, maybe the information on how the car going? Output: overwrite current x,y,and angle, output true if it function correctly
    #obj_info(): use to return distance and angle that detect the object. input: nothing. output: distance to the object, the left and right angle of the object
    #reach_destination(curr_x, x, curr_y, y) : use to determine if the robot car reach to the destination. Does not have to be exact but need to be close to a range. Input is current location and target location. Output is Ture if it reach target, else false
    #turn_no_obj() : use to control the trun while no object in camera. input: current location, target location, current angle, target_angle. output: control the motor, return the value use to control the motor
    #turn_obj() : use to control the trun when an object appear. input: distance to object, left and right inform of the object. Output: control the motor, return the value use to control the motor

def convert_angle(x,y):
    if(y == 0):      #special case when y = 0 
        if(x == 0):          #reach the destination
            return None
        elif(x > 0):     
            return 90
        else:
            return -90
    temp = x/y
    if(y > 0): #in case from -90 to 90 degree
        return math.degrees(math.atan(temp))
    
    else:
        if(x > 0):  #case for 90 to 180 degree
            return 180 - math.degrees(math.atan(temp))
        else:       #case for -180 to -90 degree
            return math.degrees(math.atan(temp)) - 180

def no_object():    #keep space for the function for now
    return True

def update_info(x,y,curr_angle):    #for keep space
    return True

def reach_destination(curr_x, x, curr_y, y):    #for keep space
    distance_apart = math.sqrt((curr_x - x)**2 + (curr_y - y)**2)       #use to calculate the distance from the destination to current lcoation
    if(distance_apart < 1):
        return True
    else:
        return False

def object_info():      #for keep space
    #return the distance of the object, the left and right most angle that detect  of the object
    return 1,2,3

def turn_no_obj(current_location, target_location, current_angle, target_angle) :     
    #control the motor
    #return the value use to control the motor for calculation
    return 1,2

def turn_obj(distance_to_object, left, right) :
    #contorl the motor
    #return the value use to control the motor for calculation
    return True

def simple_PL(x,y):     #input a coordinate to travel to, +x = go to right, +y = go straight

    curr_x = 0          #use to keep track on the x of the car current status
    curr_y = 0          #use to keep track on the y of the car current status
    curr_angle = 0      #use to keep track on the angle of the car current status, range from -180 to 180. 0 indicate straight

    robot = Robot()     #init the class 

    #need to care about two case, if there is no object case and if there is object in front case
    while(not reach_destination(curr_x, x, curr_y, y)):

        #if no object
        if(no_object()):     #use to check is there object in front
            
            if(curr_angle != convert_angle(x - curr_x, y - curr_y)):#not pointing at the correct angle
                #adjust to the left while going straight if angle is negative and right if angle is positive
                #need to test how much to adjust, in theory higher angle require more adjestment and lower require lesser turning
                sleep(0.5)
                update_info(curr_x,curr_y,curr_angle)

            else:
                #go straight 
                sleep(0.5)
                update_info(curr_x,curr_y,curr_angle)
        
        #if there is object detected
        if(not no_object()):    #sense object in front
            obj_distance, obj_left_angle, obj_right_angle = object_info() #left and right angle use to identify to turn left or right to avoid the object, distance use to determine how much to turn

            #case one, left angle is smaller than right angle, so turn left to avoid the object
            if(obj_left_angle <= obj_right_angle):
                #adust to the left while going straight, need to detemine how much to turn depend on the distance
                sleep(0.5)
                update_info(curr_x,curr_y,curr_angle)

            #case two, right angle is smaller than left angle, so turn right to avoid the object
            elif(obj_left_angle > obj_right_angle):
                #adust to the right while going straight, need to detemine how much to turn depend on the distance
                sleep(0.5)
                update_info(curr_x,curr_y,curr_angle)


    

