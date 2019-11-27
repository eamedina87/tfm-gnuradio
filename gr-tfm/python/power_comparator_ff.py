#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 ERICK ADOLFO MEDINA MORENO.
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

import numpy
from gnuradio import gr

class power_comparator_ff(gr.sync_block):

    def __init__(self, sample_rate, center_frequency, vector_length, directory, diff_fixed_db, diff_percentage):
        self.vlen = vector_length
        self.samp_rate = sample_rate
        self.center_freq = center_frequency
        self.freq_delta = sample_rate/(vector_length-1)
        self.directory = directory
        #self.mode = mode
        self.diff_db = diff_fixed_db
        self.diff_percentage = diff_percentage
        gr.sync_block.__init__(self,
            name="power_comparator_ff",
            in_sig=[(numpy.float32,self.vlen)],
            out_sig=None)

    def set_center_freq(self, center_frequency):
        self.center_freq = center_frequency

    #def set_mode(self, mode):
    #    self.mode = mode

    def set_diff_percentage(self, diff_percentage):
        self.diff_percentage = diff_percentage

    def set_diff_db(self, diff_fixed_db):
        self.diff_fixed_db = diff_fixed_db 

    def work(self, input_items, output_items):
        in0 = input_items[0]
        if self.diff_percentage > 0:
            print("Mode mode_percentage")
        elif self.diff_db > 0:
            print("Mode mode_fixed")
        else:
            print("Mode Error")
        return len(input_items[0])
