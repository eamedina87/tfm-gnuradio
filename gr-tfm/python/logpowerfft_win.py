#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
from __future__ import division

from gnuradio import gr
from gnuradio import blocks
from gnuradio import fft as fft_lib
import sys, math

try:
    from gnuradio import filter
except ImportError:
    sys.stderr.write('logpwrfft_win required gr-filter.\n')
    sys.exit(1)

class logpowerfft_win(gr.hier_block2):
    """
    docstring for block logpowerfft_win
    """
    def __init__(self, sample_rate, fft_size, ref_scale, frame_rate):
        gr.hier_block2.__init__(self,
            "logpowerfft_win",
            gr.io_signature(1, 1, gr.sizeof_gr_complex),          
            gr.io_signature(1, 1, gr.sizeof_float*fft_size))

            
        self._sd = blocks.stream_to_vector_decimator(item_size=gr.sizeof_gr_complex,
                                                     sample_rate=sample_rate,
                                                     vec_rate=frame_rate,
                                                     vec_len=fft_size)

        fft_window = fft_lib.window_hamming(fft_size)
        fft = fft_lib.fft_vcc(fft_size, True, fft_window, True)
        window_power = sum([x*x for x in fft_window])

        c2magsq = blocks.complex_to_mag_squared(fft_size)
        self._avg = filter.single_pole_iir_filter_ff(1.0, fft_size)
        self._log = blocks.nlog10_ff(10, fft_size,
                                     -20*math.log10(fft_size)              # Adjust for number of bins
                                     -10*math.log10(float(window_power) / fft_size) # Adjust for windowing loss
                                     -20*math.log10(float(ref_scale) / 2))      # Adjust for reference scale
        self.connect(self, self._sd, fft, c2magsq, self._avg, self._log, self)

    def set_decimation(self, decim):
        """
        Set the decimation on stream decimator.
        Args:
            decim: the new decimation
        """
        self._sd.set_decimation(decim)

    def set_vec_rate(self, vec_rate):
        """
        Set the vector rate on stream decimator.
        Args:
            vec_rate: the new vector rate
        """
        self._sd.set_vec_rate(vec_rate)

    def set_sample_rate(self, sample_rate):
        """
        Set the new sampling rate
        Args:
            sample_rate: the new rate
        """
        self._sd.set_sample_rate(sample_rate)

    def set_average(self, average):
        """
        Set the averaging filter on/off.
        Args:
            average: true to set averaging on
        """
        self._average = average
        if self._average:
            self._avg.set_taps(self._avg_alpha)
        else:
            self._avg.set_taps(1.0)

    def set_avg_alpha(self, avg_alpha):
        """
        Set the average alpha and set the taps if average was on.
        Args:
            avg_alpha: the new iir filter tap
        """
        self._avg_alpha = avg_alpha
        self.set_average(self._average)

    def sample_rate(self):
        """
        Return the current sample rate.
        """
        return self._sd.sample_rate()

    def decimation(self):
        """
        Return the current decimation.
        """
        return self._sd.decimation()

    def frame_rate(self):
        """
        Return the current frame rate.
        """
        return self._sd.frame_rate()

    def average(self):
        """
        Return whether or not averaging is being performed.
        """
        return self._average

    def avg_alpha(self):
        """
        Return averaging filter constant.
        """
        return self._avg_alpha
