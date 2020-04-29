This is the folder for SLAM.

To set up for Linux:
1. run linux1_dependencies.sh
2. run linux2_eigen.sh
3. run linux3_opencv.sh
4. run DBoW2.sh
5. run g2o.sh
6. run linux6_SocketViewer.sh
7. run openvslambuild.sh
* You need to change the directories for steps 2-7 so make sure to do that before running.

To set up for MacOS:
1. run macos1_dependencies.sh
2. run DBoW2.sh
3. run g2o.sh
4. run macos4_SocketViewer.sh
5. run openvslambuild.sh
* You need to change the directories for steps 2-5 so make sure to do that before running.

After setting up, run ./run_kitti_slam -h to see if openVSLAM was successfully built. You should see the allowed options menu.

To set up the SocketViewer server:

- $ cd /path/to/openvslam/viewer
- $ npm install
- $ node app.js

Then go to http://localhost:3001/ on your browser.
