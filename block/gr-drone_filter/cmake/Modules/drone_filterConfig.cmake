INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DRONE_FILTER drone_filter)

FIND_PATH(
    DRONE_FILTER_INCLUDE_DIRS
    NAMES drone_filter/api.h
    HINTS $ENV{DRONE_FILTER_DIR}/include
        ${PC_DRONE_FILTER_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DRONE_FILTER_LIBRARIES
    NAMES gnuradio-drone_filter
    HINTS $ENV{DRONE_FILTER_DIR}/lib
        ${PC_DRONE_FILTER_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DRONE_FILTER DEFAULT_MSG DRONE_FILTER_LIBRARIES DRONE_FILTER_INCLUDE_DIRS)
MARK_AS_ADVANCED(DRONE_FILTER_LIBRARIES DRONE_FILTER_INCLUDE_DIRS)

