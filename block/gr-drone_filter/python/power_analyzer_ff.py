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

class power_analyzer_ff(gr.sync_block):
    
    def __init__(self, vector_size):
        self.vlen = vector_size
        gr.sync_block.__init__(self,
            name="power_analyzer_ff",
            in_sig=[(np.complex64,self.vlen)],
            out_sig=None)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        print(in0.len)
        for value in in0
            print(value)
        return len(output_items[0])

