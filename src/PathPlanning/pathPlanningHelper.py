import math
from time import sleep
import numpy as np 
import matplotlib.pyplot as plt
from IPython import display
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
        
# Map is a 2d array that tell the obstacle of the surrounding, 0 indicate it is free to move, 1 indicate that block has obstacle.
#size of map is a pair that tell the x and y size of the map
#initLoc is a pair that show the init location to start
#endLoc is a pair that the distination location
def pathPlanning(Map, size_map, initLoc, endLoc):
    if(Map[initLoc[0]][initLoc[1]] == 1):
        print("init location is obstacle")
        return None,None
    if(initLoc == endLoc):
        print("init location is destination")
        return None,None
    
    #this is the close list, which indicate which path is traveled 
    closeList = [[False for i in range(size_map[1])] for j in range(size_map[0])] 
    
    #init the map to store the data of each node, currently, all the field is None to begin with
    NodeMap = [[node() for i in range(size_map[1])] for j in range(size_map[0])] 
    
    #init the first node information to NodeMap
    NodeMap[initLoc[0]][initLoc[1]].f = 0.0
    NodeMap[initLoc[0]][initLoc[1]].g = 0.0
    NodeMap[initLoc[0]][initLoc[1]].h = 0.0
    
    #put the init item into the openList
    openList = [(0,(initLoc[0],initLoc[1]))]
    
    #color the end node
    Map[endLoc[0]][endLoc[1]] = 4
    
#     cmap = matplotlib.colors.ListedColormap(['purple','black','red','green','yellow'])
#     bounds=[-0.5,0.5,1.5,2.5,3.5,4.5,5.5]
#     norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    

    
    while(len(openList) != 0):
        
        openList = sorted(openList)
        
        #extract the top node
        curr = openList.pop(0)
        i = curr[1][0]
        j = curr[1][1]
        
        Map[i][j] = 3
        
        
        #update the close list for the current visit node
        closeList[i][j] = True
        
        #next, check the 8 direction of the node
        nodeList = gen8dirList(i,j)
        
        while(len(nodeList) != 0):
            
            #obtain the first element, in the form of (x,y) for the location it representing
            item = nodeList.pop(0)
            x = item[0]
            y = item[1]
            
            #the node location need to be in the map to continue, else, skip this node
            if(checkBoundry(x, y, size_map) == True):
                
                #Check is it the destination
                if(item == endLoc):
                    
                    #update the NodeMap information
                    NodeMap[x][y].parent_loc = curr[1]
                    
                    #update the map to see it the cahnge
                    Map[x][y] = 4
                    
                    img = plt.imshow(Map,vmin=0, vmax=4)
                    plt.colorbar(img)
                    plt.show()
                    display.display(plt.gcf())
                    display.clear_output(wait=True)
                    
                    path = findPath(NodeMap, initLoc, endLoc)
                    
                    colorPath(path, Map)
                    img = plt.imshow(Map,vmin=0, vmax=4)
                    plt.colorbar(img)
                    plt.show()
                    display.display(plt.gcf())
                    sleep(2)
                    
                    
                    return path,Map
                
                
                #the location is not destination and not in the close list and it is not obstacle
                elif(closeList[x][y] == False and Map[x][y] != 1):
                    
                    #new G = old node + 1 for the cost to travel to this location
                    if(i == x or j == y):
                        newG = NodeMap[i][j].g + 1
                    else:
                        newG = NodeMap[i][j].g + math.sqrt(2)
                    
                    #new H = the distance to the destination
                    newH = calculateDistance(item,endLoc)
                    
                    #new F = sum of G and H
                    newF = newG + newH
                    
                    
                    #if the current node not in the open list yet or if the newF is better than the old F value, push it to open list
                    if(NodeMap[x][y].f == None or NodeMap[x][y].f > newF):
                        
                        #push it to openList
                        openList.append((newF,(x,y)))
                        
                        #update the NodeMap
                        NodeMap[x][y].f = newF
                        NodeMap[x][y].g = newG
                        NodeMap[x][y].h = newH
                        NodeMap[x][y].parent_loc = curr[1]
                        
                        #update the map for virusal seeing the result
                        Map[x][y] = 2
                        
        img = plt.imshow(Map, vmin=0, vmax=4)
        plt.colorbar(img)
        plt.show()
        display.display(plt.gcf())
        display.clear_output(wait=True)
#         sleep(1)
            
    print("no path to destination")
    return None,Map
    

