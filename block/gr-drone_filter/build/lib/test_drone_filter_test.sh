#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/lib
export PATH=/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/lib:$PATH
export LD_LIBRARY_PATH=/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-drone_filter 
