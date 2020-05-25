#!/bin/sh
# Download, build and install OpenCV from source
# enter the path to your working directory below!!
cd /path/to/working/dir
wget -q https://github.com/opencv/opencv/archive/3.4.0.zip
unzip -q 3.4.0.zip
rm -rf 3.4.0.zip
cd opencv-3.4.0
mkdir -p build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local -DENABLE_CXX11=ON -DBUILD_DOCS=OFF -DBUILD_EXAMPLES=OFF -DBUILD_JASPER=OFF -DBUILD_OPENEXR=OFF -DBUILD_PERF_TESTS=OFF -DBUILD_TESTS=OFF -DWITH_EIGEN=ON -DWITH_FFMPEG=ON -DWITH_OPENMP=ON ..
make -j4
make install
