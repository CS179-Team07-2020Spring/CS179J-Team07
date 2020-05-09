import cv2
import numpy as np
import torch
import torchvision
import torch.nn.functional as F
import time

# input: camera.value; output: nparray [H,W,C]
def cameraToNparray(camera_value):
	image_array = cv2.cvtColor(camera_value, cv2.COLOR_BGR2RGB)
	return image_array

def arrayHWCToCHW(image_array):
	x = image_array.transpose((2, 0, 1))
	return x

def nparrayToTorch(image_array):
	x = torch.from_numpy(image_array).float()
	return x



# can be put into a block
def update(change):
    global blocked_slider, robot
    x = change['new'] 
    x = preprocess(x)
    y = model(x)
    
    # we apply the `softmax` function to normalize the output vector so it sums to 1 (which makes it a probability distribution)
    y = F.softmax(y, dim=1)
    
    prob_blocked = float(y.flatten()[0])
    
    blocked_slider.value = prob_blocked
    
    if prob_blocked < 0.5:
        robot.forward(0.4)
    else:
        robot.left(0.4)
    
    time.sleep(0.001)
        
update({'new': camera.value})  # we call the function once to intialize