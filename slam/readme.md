# This is the folder for SLAM.

## To set up for Linux:
> 1. run linux1_dependencies.sh
> 2. run linux2_eigen.sh
> 3. run linux3_opencv.sh
> 4. run DBoW2.sh
> 5. run g2o.sh
> 6. run linux6_SocketViewer.sh
> 7. run openvslambuild.sh
* *You need to change the directories for steps 2-7 so make sure to do that before running.*

## To set up for MacOS:
> 1. run macos1_dependencies.sh
> 2. run DBoW2.sh
> 3. run g2o.sh
> 4. run macos4_SocketViewer.sh
> 5. run openvslambuild.sh
* *You need to change the directories for steps 2-5 so make sure to do that before running.*

**After setting up, run `./run_kitti_slam -h` to see if openVSLAM was successfully built. You should see the allowed options menu.**

### To set up the SocketViewer server:

```bash
$ cd /path/to/openvslam/viewer
$ npm install
$ node app.js
```

Then go to http://localhost:3001/ on your browser.
<br></br>
## Or just start the Docker containers
```bash
docker pull seyeonk/openvslam-socket
docker pull seyeonk/openvslam-server
```

### On Linux
First, launch the server container and open it on http://localhost:3001/
```bash
docker run --rm -it --name openvslam-server --net=host openvslam-server
```
Then launch the OpenVSLAM container:
```bash
docker run --rm -it --name openvslam-socket --net=host openvslam-socket
```

### On MacOS
First, launch the server container and open it on http://localhost:3001/
```bash
docker run --rm -it --name openvslam-server -p 3001:3001 openvslam-server
```
Then inspect the container's IP address and append the `SocketPublisher.server_uri` entry to the OpenVSLAM config.yaml file:
```bash
docker inspect openvslam-server | grep -m 1 \"IPAddress\" | sed 's/ //g' | sed 's/,//g'
```
Ex: if the IPAddress is 172.17.0.2, append `SocketPublisher.server_uri: "http://172.17.0.2:3000"` to the config file.
Then launch the OpenVSLAM container:
```bash
docker run --rm -it --name openvslam-socket openvslam-socket
```
