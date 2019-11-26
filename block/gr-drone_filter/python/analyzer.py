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

import numpy
from gnuradio import gr

class analyzer(gr.sync_block):
    """
    docstring for block analyzer
    """
    def __init__(self, sample_rate, center_frequency):
        gr.sync_block.__init__(self,
            name="analyzer",
            in_sig=[numpy.complex64],
            out_sig=None)
        self.sample_rate = sample_rate
        self.center_freq = center_frequency


    def work(self, input_items, output_items):
        in0 = input_items[0]
        print(len(input_items))
        print(input_items[0])
        return len(input_items[0])

