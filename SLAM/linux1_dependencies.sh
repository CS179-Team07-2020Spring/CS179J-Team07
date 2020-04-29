#!/bin/sh
git clone https://github.com/xdspacelab/openvslam
apt update -y
apt upgrade -y --no-install-recommends
# basic dependencies
apt install -y build-essential pkg-config cmake git wget curl unzip
# g2o dependencies
apt install -y libatlas-base-dev libsuitesparse-dev
# OpenCV dependencies
apt install -y libgtk-3-dev
apt install -y ffmpeg
apt install -y libavcodec-dev libavformat-dev libavutil-dev libswscale-dev libavresample-dev
# eigen dependencies
apt install -y gfortran
# other dependencies
apt install -y libyaml-cpp-dev libgoogle-glog-dev libgflags-dev
# Protobuf dependencies for SocketViewer
apt install -y autogen autoconf libtool
# Node.js
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
apt install -y nodejs
