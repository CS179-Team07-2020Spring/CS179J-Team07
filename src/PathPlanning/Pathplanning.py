#use A* algorithm idea to implement path planning function

#need to know the data structure of the map
#Currently assume the map can be use as a gride format

#Let call each blcok of the map a cell
#A cell can be blocked, which can be a obsticle, or unblocked
#Each cell need to record 3 value, 
#   -g value: the cost to travel to that location
#   -h value: the distance from the current cell to destination, need to build a function to calculate it
#   -f value: summation of g and h value, use to order which cell to visit first

#might need to implement a data structure that able to extract min from the data to seearch the lowest f

def readmap(): #convert the map into a 2d array, 0 for no obstacle, -1 for obstacle, and 1 for goal
    return 0

#need to update the size, only for holding space now
row = 10
column = 10
Mapdata[10][10] = readmap()



def calculateDistance(pairCurrLoc, pairTarLoc): #use to calculate the distance from current cell to destination
    return 1

def convertLoc(location, x):        #return the x number of location from the currect location
    return 1

def inrange(location):  #return true if the location pass in is in range, else false
    return True

def pathPlanning(target, current):
    closedList[row][column] = 0     #init the closed list
    openList = None         #the openList is empty to begin with
    MapDetail[row][column] = 0      #use to store the g,h,and f value for each cell and the parent of the cell, need to init those value

    #push the current location to openList   
    openList.push(current)

    #update the Map Detail with the first element, init g,h,f value to be 0 and parent to None
    MapDetail.start(current)    

    findDestination = False

    #while did not find the destination yet and the open list is still not empty, continue to run the checking
    while(not findDestination and openList.empty() == False):
        #read the openList and pop the top location from the open list
        location = openList.top()
        openList.pop()

        #update the location to close list because we won't travel back to this location, this is the shortest location already
        closeList[location.first][location.second] = 1

        #now, need to check all the cell in 8 direction, if it is off the map, skip it, else update the cell value in Map detail if needed
        #assume it start at (0,0), 8 direction are:
        #   (1,0), (1,1), (0,1), (-1, 1), (-1,0), (-1,-1), (0,-1), (1,-1)
        #for each of the cell in 8 direction
        for x in range(8):
            newLoc = convertLoc(location, x) 

            #
            if(inrange(newLoc) == True):

                #if it reach the destination
                if(Mapdata[newLoc.first][newLoc.second] == 1):
                    #now need to check is it the destination, if yes, update the mapdata for this location and break out from the loop
                    MapDetail[newLoc.first][newLoc.second].g =  MapDetail[location.first][location.second].g + 1
                    MapDetail[newLoc.first][newLoc.second].parent = location
                    findDestination = True
                    break

                #if not destination and not (in the close list and  not a obstacle cell )
                elif(closedList[newLoc.first][newLoc.second] == 0 and Mapdata[newLoc.first][newLoc.second] == 0  ):
                    new_g = MapDetail[location.first][location.second].g + 1
                    new_h = MapDetail[newLoc.first][newLoc.second].h
                    new_f = new_g + new_h

                    #if the new f is better than the current f, update the node and push it to open list
                    if(MapDetail[newLoc.first][newLoc.second].f < new_f):

                        #push the result to open list because it either have better value or not in the open list before
                        openList.push(newLoc)

                        #Update the map detatil to keep the value updated
                        MapDetail[newLoc.first][newLoc.second].g = new_g
                        MapDetail[newLoc.first][newLoc.second].h = new_h
                        MapDetail[newLoc.first][newLoc.second].f = new_f
                        MapDetail[newLoc.first][newLoc.second].parent = location

    if(findDestination == False):
        print("cannot find the destination")

    else:
        #find the path, all it need is to trace back using the parent field in MapDetail
        return MapDetail



