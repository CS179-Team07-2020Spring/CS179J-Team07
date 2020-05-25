import math
dis_threshold = 0.1
def check_angle(angle):     #use to convert the angle to be between -180 to 180 degree
    return angle % 360

def angle_range_convert(angle): # input is [0,360] the car need to spin
    angle = angle % 360
    
    if angle <= 180 :
        return angle
    else:
        return (angle  - 360) 

def update_info_straight(curr_x,curr_y,curr_angle, time):    #for keep space
    speed = 1       #currently defalut 1, can use calibration to change that
    curr_x = curr_x + math.cos(math.radians(curr_angle)) * time * speed
    curr_y = curr_y + math.sin(math.radians(curr_angle)) * time * speed

    return curr_x,curr_y

def reach_destination(curr_x, x, curr_y, y):  
    distance_apart = math.sqrt((curr_x - x)**2 + (curr_y - y)**2)       #use to calculate the distance from the destination to current lcoation
    if(distance_apart < dis_threshold): #within a range, then it mean it is close to the destination, then it return true.
        return True
    else:
        return False

def convert_angle(delta_x,delta_y):
    if(delta_x == 0):      #special case when x = 0 
        if(delta_y == 0):          #reach the destination
            return None
        elif(delta_y > 0):     
            return 90
        else:
            return -90
    temp = delta_y / delta_x
    
    if(delta_x > 0): #in case from -90 to 90 degree
        return math.degrees(math.atan(temp))
    else:
        
        if(delta_y > 0):  #case for 90 to 180 degree
            return 180 + math.degrees(math.atan(temp))
        else:       #case for -180 to -90 degree
            return math.degrees(math.atan(temp)) + 180 - 360


