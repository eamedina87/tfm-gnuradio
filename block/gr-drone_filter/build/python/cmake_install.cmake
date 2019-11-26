# Install script for directory: /home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/drone_filter" TYPE FILE FILES
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python/__init__.py"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python/drone_filter.py"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python/detector.py"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python/test.py"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python/analyzer.py"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/python/power_analyzer_ff.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/drone_filter" TYPE FILE FILES
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/__init__.pyc"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/drone_filter.pyc"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/detector.pyc"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/test.pyc"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/analyzer.pyc"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/power_analyzer_ff.pyc"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/__init__.pyo"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/drone_filter.pyo"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/detector.pyo"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/test.pyo"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/analyzer.pyo"
    "/home/eamedina/Dropbox/UPC/TFM/gnuRadio/block/gr-drone_filter/build/python/power_analyzer_ff.pyo"
    )
endif()

