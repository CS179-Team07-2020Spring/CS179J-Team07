#!/bin/sh
# building openvslam with SocketViewer
# enter the path to your openvslam below!!
cd /path/to/openvslam
mkdir build && cd build
cmake -DBUILD_WITH_MARCH_NATIVE=ON -DUSE_PANGOLIN_VIEWER=OFF -DUSE_SOCKET_PUBLISHER=ON -DUSE_STACK_TRACE_LOGGER=ON -DBOW_FRAMEWORK=DBoW2 -DBUILD_TESTS=ON ..
make -j4
