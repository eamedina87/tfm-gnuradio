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
from datetime import datetime
from gnuradio import gr

class power_comparator_ff(gr.sync_block):

    def __init__(self, sample_rate, center_frequency, vector_length, directory, mode, diff_fixed_db, diff_percentage):
        self.vlen = vector_length
        self.samp_rate = sample_rate
        self.center_freq = center_frequency
        self.freq_delta = sample_rate/(vector_length-1)
        self.directory = directory
        self.mode = mode
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
        file_base_power = "power_%.0fMHz_%.0fMsps_%dFFT" % (self.center_freq // 1e6, self.samp_rate // 1e6, self.vlen)
        file_base_compare = "compare_%.0fMHz_%.0fMsps_%dFFT_%.0fm_%.0fpc_%.0fdb" % (self.center_freq // 1e6, self.samp_rate // 1e6, 
            self.vlen, self.mode,self.diff_percentage, self.diff_db)
        filename_power = "{dir}/{file}.txt".format(dir=self.directory, file=file_base_power)
        filename_result = "{dir}/{file}.txt".format(dir=self.directory,file=file_base_compare)
        filename_result_temp = "{dir}/{file}_tmp.txt".format(dir=self.directory,file=file_base_compare)
        filename_log = "{dir}/log.txt".format(dir=self.directory)
        #print(filename)
        in0 = input_items[0]
        start_freq = self.center_freq - self.samp_rate / 2
        log_file = open(filename_log, 'a+')
        log_file.write(datetime.now().strftime('%Y%m%d %H:%M:%S:%f')+" ")
        log_file.write("files: " + filename_power+ ";" + filename_result +"\n")
        shifted = numpy.fft.fftshift(in0)
        for i, value in enumerate(shifted):
            #log_file.write("For index: %d\n" % (i))
            file_power_exists = False
            try:
                file_power = open(filename_power, 'r')
                file_power_exists = True
            except IOError:
                log_file.write(datetime.now().strftime('%Y%m%d %H:%M:%S:%f')+" ")
                log_file.write("No database file for {file}\n".format(file=file_base_power))
                return 0
            iterator = numpy.nditer(value, flags=['f_index'])
            file_power_index = 0 #we must read this value because is the first line of the file. Not needed for processing
            if file_power_exists:
                try:
                    file_power_index = float(file_power.readline()) #read number of values per row of powers
                except Exception:
                        log_file.write("file power exception\n")
            file_result_exists = False
            try:
                file_result = open(filename_result, 'r')
                file_result_exists = True
            except IOError:
                file_result = open(filename_result, 'w+')
            file_result_index = 0
            if file_result_exists:
                try:
                    file_result_index = float(file_result.readline()) #read number of values per row of results
                except Exception:
                    file_result_index = 0        
            temp_file = open(filename_result_temp, 'w+')
            temp_file.write("%.0f\n" % (file_result_index+1))
            while not iterator.finished:
                current_freq = (iterator.index * self.freq_delta) + start_freq
                cached_power = 1000
                if file_power_exists:
                    try:
                        line = file_power.readline()
                        cached_power = float(line.split("@")[0]) #read database power
                        #log_file.write("cached_power: " + line+ "\n")
                    except Exception:
                        log_file.write(datetime.now().strftime('%Y%m%d %H:%M:%S:%f')+" ")
                        log_file.write("cached_power exception\n")
                power = iterator[0]
                #log_file.write("new power: %.2f\n" % (power))
                data = "default"
                exceeded_number = 0
                exceeded_average = 0
                exceeded_diff_min = 10000
                exceeded_diff_average = 0
                exceeded_diff_max = 0        
                if file_result_exists:
                    try:
                        line = file_result.readline()
                        data = line.split("@")[0]
                        #log_file.write(datetime.now().strftime('%Y%m%d %H:%M:%S:%f')+" ")
                        #log_file.write("cached_data: " + line+ "\n")
                        values = data.split(";")
                        exceeded_number = float(values[0])
                        exceeded_average = float(values[1])
                        exceeded_diff_min = float(values[2])
                        exceeded_diff_average = float(values[3])
                        exceeded_diff_max = float(values[4])
                    except Exception:
                        nodata = True
                exceeded_diff = 0
                if self.mode == 1: #percentage
                    threshold = cached_power*(1+self.diff_percentage/100) 
                else: #fixed db
                    threshold = cached_power+self.diff_db 
                if power > threshold:
                    exceeded_diff = power - threshold
                    exceeded_diff_min = numpy.minimum(exceeded_diff_min,exceeded_diff)
                    exceeded_diff_average = ((exceeded_diff_average * exceeded_number) + exceeded_diff) / (exceeded_number+1)
                    exceeded_number = exceeded_number+1    
                    exceeded_diff_max = numpy.maximum(exceeded_diff_max,exceeded_diff)
                exceeded_average = exceeded_number/(file_result_index+1)    
                temp_file.write("%.0f;%.2f;%.2f;%.2f;%.2f@%.6f" % (exceeded_number, exceeded_average, exceeded_diff_min,
                    exceeded_diff_average, exceeded_diff_max, current_freq/1e6))
                #log_file.write("new values: %.0f;%.2f;%.2f;%.2f;%.2f@%.6f\n" % (exceeded_number, exceeded_average, exceeded_diff_min,
                #    exceeded_diff_average, exceeded_diff_max, current_freq/1e6))
                if (iterator.index != self.vlen-1):
                    temp_file.write("\n")
                iterator.iternext()
            file_power.close()
            file_result.close()
            temp_file.close()
            os.remove(filename_result)
            os.rename(filename_result_temp, filename_result)
        log_file.close()
        return len(input_items[0])