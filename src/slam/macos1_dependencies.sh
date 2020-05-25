#!/bin/sh
git clone https://github.com/xdspacelab/openvslam
brew update
# basic dependencies
brew install pkg-config cmake git
# g2o dependencies
brew install suite-sparse
# OpenCV dependencies and OpenCV
brew install eigen
brew install ffmpeg
brew install opencv
# other dependencies
brew install yaml-cpp glog gflags
# (if you plan on using SocketViewer)
# Protobuf dependencies
brew install automake autoconf libtool
# Node.js
brew install node
