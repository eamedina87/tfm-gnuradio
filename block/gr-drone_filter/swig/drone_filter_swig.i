/* -*- c++ -*- */

#define DRONE_FILTER_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "drone_filter_swig_doc.i"

%{
#include "drone_filter/power_database_ff.h"
#include "drone_filter/power_analyzer_ff.h"
%}


%include "drone_filter/power_database_ff.h"
GR_SWIG_BLOCK_MAGIC2(drone_filter, power_database_ff);
%include "drone_filter/power_analyzer_ff.h"
GR_SWIG_BLOCK_MAGIC2(drone_filter, power_analyzer_ff);
