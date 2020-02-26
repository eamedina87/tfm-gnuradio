#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Drone Detection
# Author: Erick Medina Moreno
# Description: Pool of scripts that run different processes to detect  drones
# Generated: Wed Feb 12 12:57:33 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from PyQt5.QtCore import pyqtSlot
import sys
from gnuradio import qtgui
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import sys
import time
import functools
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QFileDialog
from gnuradio.qtgui import Range, RangeWidget
import subprocess

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Drone Detection")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Drone Detection")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QHBoxLayout(self.top_widget)

        self.data_params_layout = Qt.QHBoxLayout()
        self.directory_params_layout = Qt.QHBoxLayout()
        
        self.top_left_layout = Qt.QVBoxLayout()
        self.top_right_layout = Qt.QVBoxLayout()

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.directory = directory = "/home/eamedina/Documentos/freq_docs/new"
        self.spectrum_scan_button = spectrum_scan_button = 0
        self.jammer_button = jammer_button = 0
        self.base_scan_button = base_scan_button = 0
        self.band_scan_button = band_scan_button = 0
        self.graphic_band_choose = graphic_band_choose = 0
        self.samp_rate = 20e6
        self.fft_size = 1024
        self.freq_max = 6000e6
        self.center_freq = self.samp_rate/2
        self.table_sort_index = 1
        self.table_sort_reverse = True
        self.bandwidth_range = bandwidth_range = 20
        self.samp_rate_chooser = samp_rate_chooser = 20
        self.center_freq_range = center_freq_range = 3000
        self.fft_size_chooser = fft_size_chooser = 1024
        self.update_graph_button = update_graph_button = 0
        self.update_params_button = update_params_button = 0
        self.update_diretory_button = update_directory_button = 0
        self.loop_min_freq = self.samp_rate/2
        self.loop_max_freq = self.freq_max

        ##################################################
        # Blocks
        ##################################################

        #SCRIPT BUTTONS
        _spectrum_scan_button_push_button = Qt.QPushButton('Spectrum Scan')
        self._spectrum_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _spectrum_scan_button_push_button.pressed.connect(lambda: self.set_spectrum_scan_button(self._spectrum_scan_button_choices['Pressed']))
        _spectrum_scan_button_push_button.released.connect(lambda: self.set_spectrum_scan_button(self._spectrum_scan_button_choices['Released']))
        
        _jammer_button_push_button = Qt.QPushButton('Jammer')
        self._jammer_button_choices = {'Pressed': 1, 'Released': 0}
        _jammer_button_push_button.pressed.connect(lambda: self.set_jammer_button(self._jammer_button_choices['Pressed']))
        _jammer_button_push_button.released.connect(lambda: self.set_jammer_button(self._jammer_button_choices['Released']))
        
        _base_scan_button_push_button = Qt.QPushButton('Base Scan')
        self._base_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _base_scan_button_push_button.pressed.connect(lambda: self.set_base_scan_button(self._base_scan_button_choices['Pressed']))
        _base_scan_button_push_button.released.connect(lambda: self.set_base_scan_button(self._base_scan_button_choices['Released']))
        
        _band_scan_button_push_button = Qt.QPushButton('Band Scan')
        self._band_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _band_scan_button_push_button.pressed.connect(lambda: self.set_band_scan_button(self._band_scan_button_choices['Pressed']))
        _band_scan_button_push_button.released.connect(lambda: self.set_band_scan_button(self._band_scan_button_choices['Released']))

        #GRAPH PARAMS
        self._directory_entry_tool_bar = Qt.QToolBar(self)
        self._directory_entry_tool_bar.addWidget(Qt.QLabel('Directory'+": "))
        self._directory_entry_line_edit = Qt.QLineEdit(str(self.directory))
        self._directory_entry_line_edit.setReadOnly(True)
        self._directory_entry_tool_bar.addWidget(self._directory_entry_line_edit)
        self._directory_entry_line_edit.returnPressed.connect(
        	lambda: self.set_directory_entry(str(str(self._directory_entry_line_edit.text().toAscii()))))
        
        _update_directory_button_push_button = Qt.QPushButton('Select Directory')
        self._update_directory_button_choices = {'Pressed': 1, 'Released': 0}
        _update_directory_button_push_button.pressed.connect(lambda: self.set_update_directory_button(self._update_directory_button_choices['Pressed']))
        _update_directory_button_push_button.released.connect(lambda: self.set_update_directory_button(self._update_directory_button_choices['Released']))

        self._graphic_band_choose_options = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, )
        self._graphic_band_choose_labels = ('CONTINUOUS', 'ALL', '433 MHz', '868 MHz', 'Wifi 2.4GHz (1)',
            'Wifi 2.4GHz (2)', 'Wifi 2.4GHz (3)', 'Wifi 2.4GHz (4)', 'Wifi 2.4GHz (5)',  'Wifi 2.4GHz (6)*',
            'Wifi 2.4GHz (7)*', 'Wifi 2.4GHz (8)*', 'Wifi 2.4GHz (9)*', 'Wifi 2.4GHz (10)*')
        self._graphic_band_choose_tool_bar = Qt.QToolBar(self)
        self._graphic_band_choose_tool_bar.addWidget(Qt.QLabel("Choose band"+": "))
        self._graphic_band_choose_combo_box = Qt.QComboBox()
        self._graphic_band_choose_tool_bar.addWidget(self._graphic_band_choose_combo_box)
        for label in self._graphic_band_choose_labels: self._graphic_band_choose_combo_box.addItem(label)
        self._graphic_band_choose_callback = lambda i: Qt.QMetaObject.invokeMethod(self._graphic_band_choose_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._graphic_band_choose_options.index(i)))
        self._graphic_band_choose_callback(self.graphic_band_choose)
        self._graphic_band_choose_combo_box.currentIndexChanged.connect(
            lambda i: self.set_graphic_band_choose(self._graphic_band_choose_options[i]))

        self._samp_rate_chooser_options = (10, 20, )
        self._samp_rate_chooser_labels = ('10 Msps', '20 Msps', )
        self._samp_rate_chooser_tool_bar = Qt.QToolBar(self)
        self._samp_rate_chooser_tool_bar.addWidget(Qt.QLabel('Sample Rate'+": "))
        self._samp_rate_chooser_combo_box = Qt.QComboBox()
        self._samp_rate_chooser_tool_bar.addWidget(self._samp_rate_chooser_combo_box)
        for label in self._samp_rate_chooser_labels: self._samp_rate_chooser_combo_box.addItem(label)
        self._samp_rate_chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._samp_rate_chooser_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._samp_rate_chooser_options.index(i)))
        self._samp_rate_chooser_callback(self.samp_rate_chooser)
        self._samp_rate_chooser_combo_box.currentIndexChanged.connect(
            lambda i: self.set_samp_rate_chooser(self._samp_rate_chooser_options[i]))
        
        self._fft_size_chooser_options = (1024, 2048, )
        self._fft_size_chooser_labels = (str(self._fft_size_chooser_options[0]), str(self._fft_size_chooser_options[1]), )
        self._fft_size_chooser_tool_bar = Qt.QToolBar(self)
        self._fft_size_chooser_tool_bar.addWidget(Qt.QLabel('FFT Size'+": "))
        self._fft_size_chooser_combo_box = Qt.QComboBox()
        self._fft_size_chooser_tool_bar.addWidget(self._fft_size_chooser_combo_box)
        for label in self._fft_size_chooser_labels: self._fft_size_chooser_combo_box.addItem(label)
        self._fft_size_chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._fft_size_chooser_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._fft_size_chooser_options.index(i)))
        self._fft_size_chooser_callback(self.fft_size_chooser)
        self._fft_size_chooser_combo_box.currentIndexChanged.connect(
            lambda i: self.set_fft_size_chooser(self._fft_size_chooser_options[i]))
        
        _update_params_button_push_button = Qt.QPushButton('Update Params.')
        self._update_params_button_choices = {'Pressed': 1, 'Released': 0}
        _update_params_button_push_button.pressed.connect(lambda: self.set_update_params_button(self._update_params_button_choices['Pressed']))
        _update_params_button_push_button.released.connect(lambda: self.set_update_params_button(self._update_params_button_choices['Released']))

        #FREQUENCY/RANGE CONTROLS
        self._center_freq_range_range = Range(5, 6000, 5, 3000, 200)
        self._center_freq_range_win = RangeWidget(self._center_freq_range_range, self.set_center_freq_range, 'Freq. (MHz)', "counter_slider", float)
        
        self._bandwidth_range_range = Range(10, 6000, 10, 20, 200)
        self._bandwidth_range_win = RangeWidget(self._bandwidth_range_range, self.set_bandwidth_range, 'Bandwidth (MHz)', "counter_slider", float)

        _update_graph_button_push_button = Qt.QPushButton('Update Graph')
        self._update_graph_button_choices = {'Pressed': 1, 'Released': 0}
        _update_graph_button_push_button.pressed.connect(lambda: self.set_update_graph_button(self._update_graph_button_choices['Pressed']))
        _update_graph_button_push_button.released.connect(lambda: self.set_update_graph_button(self._update_graph_button_choices['Released']))

        #GRAPHIC/PLOT
        self.dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self._dynamic_ax = self.dynamic_canvas.figure.subplots()

        #TABLE
        self.tableWidget = QTableWidget()
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.tableClicked)

        #LEFT LAYOUT
        self.top_left_layout.addWidget(_base_scan_button_push_button)
        self.top_left_layout.addWidget(_spectrum_scan_button_push_button)
        self.top_left_layout.addWidget(_band_scan_button_push_button)
        self.top_left_layout.addWidget(_jammer_button_push_button)

        #DIRECTORY LAYOUT
        self.directory_params_layout.addWidget(self._directory_entry_tool_bar)
        self.directory_params_layout.addWidget(_update_directory_button_push_button)

        #DATA PARAMS LAYOUT
        self.data_params_layout.addWidget(self._samp_rate_chooser_tool_bar)
        self.data_params_layout.addWidget(self._fft_size_chooser_tool_bar)
        self.data_params_layout.addWidget(_update_params_button_push_button)

        #FREQUENCY PARAMS LAYOUT
        self.freq_container = Qt.QWidget()
        self.freq_params_v_layout = Qt.QVBoxLayout(self.freq_container)
        self.freq_params_h_layout = Qt.QHBoxLayout()
        self.freq_params_h_layout.addWidget(self._bandwidth_range_win)
        self.freq_params_h_layout.addWidget(_update_graph_button_push_button)
        self.freq_params_v_layout.addWidget(self._center_freq_range_win)
        self.freq_params_v_layout.addLayout(self.freq_params_h_layout)
        self.freq_container.setVisible(False)

        #RIGHT LAYOUT
        self.top_right_layout.addLayout(self.directory_params_layout)
        self.top_right_layout.addLayout(self.data_params_layout)
        self.top_right_layout.addWidget(self._graphic_band_choose_tool_bar)
        self.top_right_layout.addWidget(self.freq_container)
        self.top_right_layout.addWidget(self.dynamic_canvas)
        self.top_right_layout.addWidget(self.tableWidget)

        self.top_layout.addLayout(self.top_left_layout)
        self.top_layout.addLayout(self.top_right_layout)

        self.updateScanDataForFreq()
        self.startContinuosBandTimer()
        self.updateTableData()

    def chooseDirectory(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory", self.directory))
        if len(file) > 0:
            self.clearGraph()
            self.clearTable()
            self.set_directory_entry(file)
            
    def startUpdateAllTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(5000)
        timerCallback = functools.partial(self.updateScanData)
        self.timer.timeout.connect(timerCallback)
        self.timer.start()

    def cancelUpdateAllTimer(self):
        try:
            self.timer.stop()
        except:
            print("All timer not initialized yet")

    def startContinuosBandTimer(self):
        self.band_timer = QtCore.QTimer()
        self.band_timer.setInterval(2000)
        timerCallback = functools.partial(self.updateFreqAndScanData)
        self.band_timer.timeout.connect(timerCallback)
        self.band_timer.start()

    def cancelContinuousBandTimer(self):
        try:
            self.band_timer.stop()        
        except:
            print("Continuous timer not initialized yet")

    def startUpdateBandTimer(self):
        self.band_timer = QtCore.QTimer()
        self.band_timer.setInterval(5000)
        timerCallback = functools.partial(self.updateScanDataForFreq)
        self.band_timer.timeout.connect(timerCallback)
        self.band_timer.start()

    def cancelUpdateBandTimer(self):
        try:
            self.band_timer.stop()        
        except:
            print("Band timer not initialized yet")

    def updateFreqAndScanData(self):
        if (self.center_freq+self.samp_rate >= self.freq_max):
            self.center_freq = self.samp_rate/2
        else:
            self.center_freq += self.samp_rate
        self.updateScanDataForFreq()

    def updateTableData(self):
        powers = []
        freqs = []
        compare_powers = []
        compare_freqs = []
        value_list = []
        for center_freq in range(int(self.samp_rate/2),int(self.freq_max),int(self.samp_rate)):
            self.readFilesForFreq(center_freq, self.samp_rate, self.fft_size, powers, freqs, compare_powers, compare_freqs, value_list)
        self.addValuesToTable(value_list)

    def updateScanData(self):
        powers = []
        freqs = []
        compare_powers = []
        compare_freqs = []
        value_list = []
        for center_freq in range(int(self.loop_min_freq),int(self.loop_max_freq),int(self.samp_rate)):
            self.readFilesForFreq(center_freq, self.samp_rate, self.fft_size, powers, freqs, compare_powers, compare_freqs, value_list)
        self.plotNewValues(freqs, powers, compare_freqs, compare_powers)
    
    def updateScanDataForFreq(self):
        powers = []
        freqs = []
        compare_powers = []
        compare_freqs = []
        value_list = []
        self.readFilesForFreq(self.center_freq, self.samp_rate, self.fft_size, powers, freqs, compare_powers, compare_freqs, value_list)
        self.plotNewValues(freqs, powers, compare_freqs, compare_powers)    

    def addValuesToTable(self, value_list):
        _list = sorted(value_list, key=self.getKey, reverse=self.table_sort_reverse)
        self.tableWidget.setRowCount(len(value_list))
        self.tableWidget.setColumnCount(len(value_list[0]))
        self.tableWidget.setHorizontalHeaderLabels(['Freq. (MHz)', 'Max. Diff.(db)', 'Min Diff.(db)', 'Avg. Diff.(db)', '% > Thr.'])
        for index in range(0, len(value_list), 1):
            current_value = _list[index]
            self.tableWidget.setItem(index,0, QTableWidgetItem(str(current_value[0])))
            self.tableWidget.setItem(index,1, QTableWidgetItem(str(current_value[1])))
            self.tableWidget.setItem(index,2, QTableWidgetItem(str(current_value[2])))
            self.tableWidget.setItem(index,3, QTableWidgetItem(str(current_value[3])))
            self.tableWidget.setItem(index,4, QTableWidgetItem(str(current_value[4]*100)))

    def clearTable(self):
        self.tableWidget.clear()

    def clearGraph(self):
        self._dynamic_ax.clear()
        self._dynamic_ax.figure.canvas.draw()        

    def check_graph_params(self):
        self.loop_min_freq = (self.center_freq_range - self.bandwidth_range/2) * 1e6
        self.loop_max_freq = (self.center_freq_range + self.bandwidth_range/2) * 1e6
        self.updateScanData()

    def getKey(self, item):
        return item[self.table_sort_index]

    def tableClicked(self, item):
        if item != self.table_sort_index:
            self.table_sort_index = item
        else:
            self.table_sort_reverse = not self.table_sort_reverse
        self.updateTableData()

    def plotNewValues(self, freqs, powers, compare_freqs, compare_powers):
        if (len(powers) > 0):
            self.clearGraph()
            self._dynamic_ax.plot(compare_freqs, compare_powers, color='red')
            self._dynamic_ax.plot(freqs, powers)
            self._dynamic_ax.figure.canvas.draw()        

    def readFilesForFreq(self, center_freq, samp_rate, fft_size, powers, freqs, compare_powers, compare_freqs, _list):
        file_base_power = "power_%.0fMHz_%.0fMsps_%dFFT" % (center_freq // 1e6, samp_rate // 1e6, fft_size)
        filename_power = "{dir}/{file}.txt".format(dir=self.directory, file=file_base_power)
        file_base_compare = "compare_%.0fMHz_%.0fMsps_%dFFT_1m_1pc_1db" % (center_freq // 1e6, samp_rate // 1e6, fft_size)
        filename_compare = "{dir}/{file}.txt".format(dir=self.directory, file=file_base_compare)
        compare_exists = False
        try:
            file_power = open(filename_power, 'r')
            file_power_index = float(file_power.readline()) #read number of values per row of powers
            try:
                file_compare = open(filename_compare, 'r')
                file_compare_index = float(file_compare.readline())
                compare_exists = True
            except Exception:
                print("No compare file found {file}".format(file=file_base_compare))    
            for power_line in file_power.readlines():
                power = float(power_line.split("@")[0])
                powers.append(power)
                freqs.append(float(power_line.split("@")[1]))
                if compare_exists:
                    line = file_compare.readline()
                    values = line.split("@")[0]
                    freq = float(line.split("@")[1])    
                    values_array = values.split(";")
                    exceeded_number = float(values_array[0])
                    exceeded_average = float(values_array[1])
                    diff_min = float(values_array[2])
                    diff_average = float(values_array[3])
                    diff_max = float(values_array[4])
                    if freq > 1: #HackRF One supports values from 1MHz to 6GHz
                        _list.append((freq, diff_max, diff_min, diff_average, exceeded_average))
                    compare_powers.append(power + diff_max)
                    compare_freqs.append(freq)
        except Exception:
            print("Exception reading file {file} or {file2}\n".format(file=file_base_power, file2=file_base_compare))
            return 0
        file_power.close()  
        if compare_exists:
            file_compare.close()

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_directory_entry(self):
        return self.directory

    def set_directory_entry(self, directory_entry):
        self.directory = directory_entry
        Qt.QMetaObject.invokeMethod(self._directory_entry_line_edit, "setText", Qt.Q_ARG("QString", str(self.directory)))

    def get_base_scan_button(self):
        return self.base_scan_button

    def set_base_scan_button(self, base_scan_button):
        self.base_scan_button = base_scan_button
        if (base_scan_button == 1):
            subprocess.call("./01-scan_base.py",shell=True)

    def get_spectrum_scan_button(self):
        return self.spectrum_scan_button

    def set_spectrum_scan_button(self, spectrum_scan_button):
        self.spectrum_scan_button = spectrum_scan_button
        if (spectrum_scan_button == 1):
            subprocess.call("./02-scan_spectrum.py")

    def get_band_scan_button(self):
        return self.band_scan_button

    def set_band_scan_button(self, band_scan_button):
        self.band_scan_button = band_scan_button
        if (band_scan_button == 1):
            subprocess.call("./03-scan_band.py")

    def get_jammer_button(self):
        return self.jammer_button

    def set_jammer_button(self, jammer_button):
        self.jammer_button = jammer_button
        if (jammer_button == 1):
            subprocess.call("./04-jammer.py")

    def get_graphic_band_choose(self):
        return self.graphic_band_choose

    def set_graphic_band_choose(self, graphic_band_choose):
        self.graphic_band_choose = graphic_band_choose
        self._graphic_band_choose_callback(self.graphic_band_choose)

    def get_update_directory_button(self):
        return self.update_directory_button

    def set_update_directory_button(self, update_directory_button):
        self.update_directory_button = update_directory_button
        if update_directory_button == 1:
            self.chooseDirectory()

    def get_update_graph_button(self):
        return self.update_graph_button

    def set_update_graph_button(self, update_graph_button):
        self.update_graph_button = update_graph_button

    def get_samp_rate_chooser(self):
        return self.samp_rate_chooser

    def set_samp_rate_chooser(self, samp_rate_chooser):
        self.samp_rate_chooser = samp_rate_chooser
        self._samp_rate_chooser_callback(self.samp_rate_chooser)
        self.samp_rate = samp_rate_chooser

    def get_fft_size_chooser(self):
        return self.fft_size_chooser

    def set_fft_size_chooser(self, fft_size_chooser):
        self.fft_size_chooser = fft_size_chooser
        self._fft_size_chooser_callback(self.fft_size_chooser)
        self.fft_size = fft_size_chooser
        print(fft_size_chooser)

    def get_center_freq_range(self):
        return self.center_freq_range

    def set_center_freq_range(self, center_freq_range):
        self.center_freq_range = center_freq_range

    def get_bandwidth_range(self):
        return self.bandwidth_range

    def set_bandwidth_range(self, bandwidth_range):
        self.bandwidth_range = bandwidth_range

    def get_update_graph_button(self):
        return self.update_graph_button

    def set_update_graph_button(self, update_graph_button):
        self.update_graph_button = update_graph_button
        if update_graph_button == 1:
            self.check_graph_params()

    def get_update_params_button(self):
        return self.update_params_button

    def set_update_params_button(self, update_params_button):
        self.update_params_button = update_params_button

    def get_graphic_band_choose(self):
        return self.graphic_band_choose

    def set_graphic_band_choose(self, graphic_band_choose):
        self.cancelUpdateAllTimer()
        self.cancelUpdateBandTimer()
        self.cancelContinuousBandTimer()
        self.graphic_band_choose = graphic_band_choose
        self._graphic_band_choose_callback(self.graphic_band_choose)
        self.index = graphic_band_choose
        self.freq_container.setVisible(False)
        if (self.index == 0) :#CONTINUOUS
            self.center_freq = self.samp_rate / 2
            self.updateScanDataForFreq()
            self.startContinuosBandTimer()
            return
        elif (self.index == 1) :#ALL
            self.updateScanData()
            self.startUpdateAllTimer()
            self.freq_container.setVisible(True)
            return
        elif (self.index == 2) :#433MHz
            self.center_freq = 430e6 if self.samp_rate == 20e6 else 435e6
        elif (self.index == 3): #868MHz
            self.center_freq = 870e6 if self.samp_rate == 20e6 else 865e6
        elif (self.index == 4): #Wifi 2.4 1
            self.center_freq = 2410e6 if self.samp_rate == 20e6 else 2405e6
        elif (self.index == 5): #Wifi 2.4 2
            self.center_freq = 2430e6 if self.samp_rate == 20e6 else 2415e6
        elif (self.index == 6): #Wifi 2.4 3
            self.center_freq = 2450e6 if self.samp_rate == 20e6 else 2425e6
        elif (self.index == 7): #Wifi 2.4 4
            self.center_freq = 2470e6 if self.samp_rate == 20e6 else 2435e6
        elif (self.index == 8): #Wifi 2.4 5
            self.center_freq = 2490e6 if self.samp_rate == 20e6 else 2445e6
        elif (self.index == 9): #Wifi 2.4 6
            self.center_freq = 2490e6 if self.samp_rate == 20e6 else 2455e6
        elif (self.index == 10): #Wifi 2.4 7
            self.center_freq = 2490e6 if self.samp_rate == 20e6 else 2465e6
        elif (self.index == 11): #Wifi 2.4 8
            self.center_freq = 2490e6 if self.samp_rate == 20e6 else 2475e6
        elif (self.index == 12): #Wifi 2.4 9
            self.center_freq = 2490e6 if self.samp_rate == 20e6 else 2485e6
        elif (self.index == 13): #Wifi 2.4 10
            self.center_freq = 2490e6 if self.samp_rate == 20e6 else 2495e6
        self.updateScanDataForFreq()
        self.startUpdateBandTimer()

def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
