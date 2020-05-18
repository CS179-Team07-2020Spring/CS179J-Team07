#!/bin/sh
# Download, build and install g2o
# enter the path to your working directory below!!
cd /path/to/working/dir
git clone https://github.com/RainerKuemmerle/g2o.git
cd g2o
git checkout 9b41a4ea5ade8e1250b9c1b279f3a9c098811b5a
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_CXX_FLAGS=-std=c++11 -DBUILD_SHARED_LIBS=ON -DBUILD_UNITTESTS=OFF -DBUILD_WITH_MARCH_NATIVE=ON -DG2O_USE_CHOLMOD=OFF -DG2O_USE_CSPARSE=ON -DG2O_USE_OPENGL=OFF -DG2O_USE_OPENMP=ON ..
make -j4
make install
