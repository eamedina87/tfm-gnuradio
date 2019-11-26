#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python
export PATH=/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python:$PATH
export LD_LIBRARY_PATH=/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/swig:$PYTHONPATH
/usr/bin/python2 /home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python/qa_detector.py 
