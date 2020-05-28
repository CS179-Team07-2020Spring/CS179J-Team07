from jetbot import Robot        #use jetbot provide function to control the basic movement of the robot
import math
from time import sleep
from helper_function import *
from helper_movement import *

robot = Robot()     #init the class 









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

        prob_left = 0       #need to use a function to read from the model
        prob_right = 0

        #if no object
        if(prob_left <0.5 and prob_right < 0.5):     #use to check is there object in front
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
        else:    #sense object in front
            

            #case one, left angle is smaller than right angle, so turn left to avoid the object
            if(prob_left > 0.5):    #thinking to use machine learning model to determine do the car need to turn left
                while(prob_left > 0.5):
                    spin_left()
                    #prob_left = #need update
                    sleep(0.1)
                    curr_angle = check_angle(curr_angle - (spin_time/0.1) * 360)  #make sure the angle is between -180 to 180 degree
                
                straight()
                sleep(0.5)
                update_info_straight(curr_x, curr_y,curr_angle,0.5)
                    
                

            #case two, right angle is smaller than left angle, so turn right to avoid the object
            elif(prob_right > 0.5):
                while(prob_right > 0.5):
                    spin_right()
                    #prob_right = #update
                    sleep(0.1)
                    curr_angle = check_angle(curr_angle + (spin_time/0.1) * 360)  #make sure the angle is between -180 to 180 degree
                
                straight()
                sleep(0.5)
                update_info_straight(curr_x, curr_y,curr_angle,0.5)     #use to update the information when the car go straight


    

