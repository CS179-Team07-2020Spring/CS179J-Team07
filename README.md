[![Build Status](https://travis-ci.org/CS179-Team07-2020Spring/CS179J-Team07.svg?branch=master)](https://travis-ci.org/CS179-Team07-2020Spring/CS179J-Team07)

# CS179J-Team07



This project is to program a Jetson Nano to have the ability to generate a map using SLAM while traveling and able to use the map that generated to perform path planning. 


### data

Used for storing data to that can use for testing

### document

Used to store our timeline for this project

### research

Used to store extra information we find that can be helpful for the project

### src

All the code for different functions of the project.
More detail on each function can be found in the readme of each function folder in src folder.

## function

- coordinate planning 
  - Enter a coordinate and move to the destination without hitting obstacle 
  - Doesn't use map, only feedback from camera

- deep reinforcement learning
  - Train obstacle dataset while moving around.
  - Continue to increase the accuracy of identifying obstacle
  
- SLAM
  - Generate map when traveling in the area
  - Able to use the map for path planning
  
- Path planning
  - Using the SLAM map as input to find the shortest path to the destination



