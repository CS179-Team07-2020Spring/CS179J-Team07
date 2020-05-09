import time
import torch.nn.functional

def calibration(camera, speed, robot, distance):     #require to have preprocess and model function predefined, preprocess use to covert the image format to match the learning library, the model is use to evaluate the possibility of the car still not travel the line yet
    
    count_false = 0         #use to keep track on how many times it find it is the end of calibration, let if the number is less than 50, this is to deal with some defect one or twice
    start_time = time.time()    #get the current time before the calibration action start
    robot.forward(speed)        #control the speed of the robot
    while(count_false < 50):
        value = camera.value        #read the camera value
        value = preprocess(value)   #use to convert the picture into the correct format
        value = model(value)        #use to access the possibility of the device still doing calibration

        value = torch.nn.functional.softmax(value, dim=1)       #convert the value into possibility

        prob_not_end = float(value.flatten()[0])            #obtain the first element of the prob

        if prob_not_end < 0.5:
            count_false = count_false + 1

        time.sleep(0.01)            #wait slightly before obtaining another sample data
    total_time = time.time() - start_time           #calculate the total time it run
    robot.stop()        #to stop the robot to indicate it has done the calibration
    return distance / total_time       #return how much it travel per sec
