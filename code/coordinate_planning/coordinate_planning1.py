from jetbot import Robot        #use jetbot provide function to control the basic movement of the robot
import math
from time import sleep

robot = Robot()     #init the class 

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

# def no_object():    #can build a machine learning model to detect is an object in front
#     return True

def update_info_straight(x,y,curr_angle, time):    #for keep space
    speed = 1       #currently defalut 1, can use calibration to change that
    x = x + math.sin(math.radians(curr_angle)) * time * speed
    y = y + math.cos(math.radians(curr_angle)) * time * speed

    return True

def reach_destination(curr_x, x, curr_y, y):  
    distance_apart = math.sqrt((curr_x - x)**2 + (curr_y - y)**2)       #use to calculate the distance from the destination to current lcoation
    
    if(distance_apart < 1): #within a range, then it mean it is close to the destination, then it return true.
        return True
    else:
        return False

def turn_left(leftspeed = 0.4, rightspeed = 0.6):    # use for easy control of the car
    robot.set_motors(leftspeed, rightspeed)

def turn_right(leftspeed = 0.6, rightspeed = 0.4):    
    robot.set_motors(leftspeed, rightspeed)

def spin_left(speed = 0.5):
    robot.left(speed)

def spin_right(speed = 0.5):
    robot.right(speed)

def straight(speed = 1):
    robot.forward(speed)

def check_angle(angle):     #use to convert the angle to be between -180 to 180 degree
    if(angle > 180):
        return -180 + angle - 180
    elif(angle < -180):
        return 180 + angle + 180
    else:
        return angle

# def object_info():      #maybe able to use machine leaning to learn to turn left or right
#     #return the distance of the object, the left and right most angle that detect  of the object
#     return 1,2,3

# def turn_no_obj(current_location, target_location, current_angle, target_angle) :     
#     #control the motor
#     #return the value use to control the motor for calculation
#     return 1,2

# def turn_obj(distance_to_object, left, right) :
#     #contorl the motor
#     #return the value use to control the motor for calculation
#     return True

def simple_PL(x,y, straight_distance, spin_time, turn_time):     #input a coordinate to travel to, +x = go to right, +y = go straight, straight_distance have unit of distance/time, spin_time and turn_time have unit of time to perform a 360 degree turn

    

    curr_x = 0          #use to keep track on the x of the car current status
    curr_y = 0          #use to keep track on the y of the car current status
    curr_angle = 0      #use to keep track on the angle of the car current status, range from -180 to 180. 0 indicate straight

    

    #need to care about two case, if there is no object case and if there is object in front case
    while(not reach_destination(curr_x, x, curr_y, y)):

        #if no object
        if(no_object()):     #use to check is there object in front
            target_angle = convert_angle(x - curr_x, y - curr_y)
            angle_different = curr_angle - target_angle

            if(abs(angle_different) > 2):#not pointing at the correct angle
                #adjust to the left while going straight if angle is negative and right if angle is positive
                if(angle_different < 0):
                    robot.left(0.5)
                else:
                    robot.right(0.5)

                time_to_turn = spin_time / abs(angle_different)     #calculate how long does the spin need to be

                sleep(time_to_turn)     #sleep to wait until the car turn enough
                curr_angle = target_angle    #x and y did not change, only the angle change to the target value in this case. 

            else:
                #go straight 
                straight()
                sleep(0.1)
                update_info_straight(curr_x,curr_y,curr_angle, 0.1)
        
        #if there is object detected
        if(not no_object()):    #sense object in front
            prob_left = 0       #need to use a function to read from the model
            prob_right = 0

            #case one, left angle is smaller than right angle, so turn left to avoid the object
            if(prob_left > 0.5):    #thinking to use machine learning model to determine do the car need to turn left
                while(prob_left > 0.5):
                    spin_left()
                    #prob_left = #need update
                    sleep(0.1)
                    curr_angle = check_angle(curr_angle - (time_to_turn/0.1) * 360)  #make sure the angle is between -180 to 180 degree
                
                straight()
                sleep(0.5)
                update_info_straight(curr_x, curr_y,curr_angle,0.5)
                    
                

            #case two, right angle is smaller than left angle, so turn right to avoid the object
            elif(prob_right > 0.5):
                while(prob_right > 0.5):
                    spin_right()
                    #prob_right = #update
                    sleep(0.1)
                    curr_angle = check_angle(curr_angle + (time_to_turn/0.1) * 360)  #make sure the angle is between -180 to 180 degree
                
                straight()
                sleep(0.5)
                update_info_straight(curr_x, curr_y,curr_angle,0.5)     #use to update the information when the car go straight


    

