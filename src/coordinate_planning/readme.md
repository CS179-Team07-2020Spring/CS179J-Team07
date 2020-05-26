# This is the folder for Coordinate Planning.

This folder include all the file required for coordinate planning function.

Other than the helper_function.py , test2.ipynb and testing.py, all other files required to run on Jetson Nano for the jetbot library. 

Here are the functionality of all the files in this foolder:

1. calibration.py

This file include functions that use to calculate the speed of the car. 

2. coordinate_planning_robot.ipynb , coordinate_planning1.py

coordinate_planning1.py is the first version of the coordinate planning code. coordinate_planning_robot.ipynb is the newer version with the functionality of object avoidance. 

3. helper_function.py

This file include all the helper function that use within coordinate_planning_robot.ipynb. It was extracted out for easier testing.

4. test2.ipynb

This file is used to test the functionality by using a mock environment. 

5. testing.py

This file is used to perform unit test on the helper function. Can use Travis CI to run the test everytime when a push of code happen



