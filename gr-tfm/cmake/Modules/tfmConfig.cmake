INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TFM tfm)

FIND_PATH(
    TFM_INCLUDE_DIRS
    NAMES tfm/api.h
    HINTS $ENV{TFM_DIR}/include
        ${PC_TFM_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TFM_LIBRARIES
    NAMES gnuradio-tfm
    HINTS $ENV{TFM_DIR}/lib
        ${PC_TFM_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TFM DEFAULT_MSG TFM_LIBRARIES TFM_INCLUDE_DIRS)
MARK_AS_ADVANCED(TFM_LIBRARIES TFM_INCLUDE_DIRS)

