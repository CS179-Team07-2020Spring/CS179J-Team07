from jetbot import Robot

#use for basic control of the robot
robot = Robot()
def turn_left(leftspeed = 0, rightspeed = 0.6):    # use for easy control of the car
    robot.set_motors(leftspeed, rightspeed)

def turn_right(leftspeed = 0.6, rightspeed = 0):    
    robot.set_motors(leftspeed, rightspeed)

def spin_left(speed = 0.5):
    robot.left(speed)

def spin_right(speed = 0.5):
    robot.right(speed)

def straight(speed = 0.3):
    robot.forward(speed)