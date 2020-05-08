import cv2
import numpy as np
import torch
import torchvision

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

