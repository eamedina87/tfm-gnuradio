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
import os
from gnuradio import gr

class power_analyzer_ff(gr.sync_block):
    """
    docstring for block power_analyzer_ff
    """
    def __init__(self, sample_rate, center_frequency, vector_length, directory):
        self.vlen = vector_length
        self.samp_rate = sample_rate
        self.center_freq = center_frequency
        self.freq_delta = sample_rate/(vector_length-1)
        self.directory = directory
        print("delta: %.0f " % self.freq_delta)
        gr.sync_block.__init__(self,
            name="power_analyzer_ff",
            in_sig=[(numpy.float32,self.vlen)],
            out_sig=None)

    def set_center_freq(self, center_frequency):
        self.center_freq = center_frequency

    def work(self, input_items, output_items):
        file_base = "power_%.0fMHz_%.0fMsps_%dFFT" % (self.center_freq // 1e6, self.samp_rate // 1e6, self.vlen)
        filename = "{dir}/{file}.txt".format(dir=self.directory, file=file_base)
        filename_temp = "{dir}/{file}_tmp.txt".format(dir=self.directory,file=file_base)
        #print(filename)
        in0 = input_items[0]
        start_freq = self.center_freq - self.samp_rate / 2
        #print("start_freq %.2f " % start_freq)
        #shifted = numpy.fft.fftshift(in0)
        for i, value in enumerate(in0):
            iterator = numpy.nditer(value, flags=['f_index'])
            file_exists = False
            try:
                file = open(filename, 'r')
                file_exists = True
            except IOError:
                file = open(filename, 'w+')    
            file_index = 0
            if file_exists:
                try:
                    file_index = int(file.readline()) #read number of values per row
                except Exception:
                    file_index = 0
                #print("file index: %d" % file_index)
            temp_file = open(filename_temp, 'w+')
            temp_file.write("%d\n" % (file_index+1))
            while not iterator.finished:
                current_freq = (iterator.index * self.freq_delta) + start_freq
                cached_power = 1000
                if file_exists:
                    try:
                        cached_power = float(file.readline().split("@")[0]) #read power
                    except Exception:
                        cached_power = 1000
                power = iterator[0]
                if cached_power != 1000:
                    #print("cached power %.2f@%.6f" % (cached_power, current_freq))
                    #print("current power %.2f" % (power))
                    power = ((cached_power * file_index) + power) / (file_index+1)
                #print("new power %.2f %d %.5f" % (power, iterator.index, current_freq))
                temp_file.write("%.2f@%.6f" % (power, current_freq/1e6))
                if (iterator.index != self.vlen-1):
                    temp_file.write("\n")
                iterator.iternext()
            file.close()
            temp_file.close()
            os.remove(filename)
            os.rename(filename_temp, filename)
        return len(input_items[0])

