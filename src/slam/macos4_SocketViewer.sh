#!/bin/sh
# Download, build and install socket.io-client-cpp from source for SocketViewer
# enter the path to your working directory below!!
cd /path/to/working/dir
git clone https://github.com/shinsumicco/socket.io-client-cpp
cd socket.io-client-cpp
git submodule init
git submodule update
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_UNIT_TESTS=OFF ..
make -j4
make install
brew install protobuf
