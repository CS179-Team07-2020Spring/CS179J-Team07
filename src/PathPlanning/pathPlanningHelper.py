import math
from time import sleep
import numpy as np 
import matplotlib.pyplot as plt

import matplotlib

def calculateDistance(curr, dest): #use to calculate the distance from current cell to destination
    temp = math.sqrt((curr[0]-dest[0])**2 + (curr[1]-dest[1])**2)
    return temp

def gen8dirList(i,j): #generate the 8 locations around the current point
    return [(i+1,j),(i+1,j+1),(i,j+1),(i-1,j+1),(i-1,j),(i-1,j-1),(i,j-1),(i+1,j-1)]

def checkBoundry(i,j,size):  #check is the current location in the map boundry
    if(i < 0 or j < 0):
        return False
    if(i >= size[0] or j >= size[1]):
        return False
    return True

def findPath(NodeMap, initLoc, endLoc):   #run at the end of the path planning algorithm to trace back the path
    
    path = []
    currLoc = endLoc
    path.append(currLoc)
    
    
    while(currLoc != initLoc):
        currLoc = NodeMap[currLoc[0]][currLoc[1]].parent_loc
        path.append(currLoc)
        
    
    return path
        
def colorPath(path, Map):
    copyPath = path.copy()
    
    while(len(copyPath) != 0):
        a = copyPath.pop()
        Map[a[0]][a[1]] = 4
        
    return Map

# #use to store the data structe in open list
# #the open list need to sort by the f
# class OpenNode(object):       
#     def __init__(self, f, loc):
#         self.f = f
#         self.loc = loc
        
# x = OpenNode(12, (3,3) )
# assert x.f == 12

#use to store the structure for all node
class node(object):
    def __init__(self, parent_loc = None, f = None,g= None,h= None):
        self.parent_loc = parent_loc
        self.f = f
        self.g = g
        self.h = h
        

    

