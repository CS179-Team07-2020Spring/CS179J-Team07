#!/bin/sh
# Download, build and install the custom DBoW2 from source
# enter the path to your working directory below!!
cd /path/to/working/dir
git clone https://github.com/shinsumicco/DBoW2.git
cd DBoW2
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local ..
make -j4
make install
