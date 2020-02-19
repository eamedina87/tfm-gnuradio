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
        self.center_freq = 10e6
        self.samp_rate = 20e6
        self.fft_size = 1024
        self.freq_max = 6000e6

        ##################################################
        # Blocks
        ##################################################

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
        
        self.top_left_layout.addWidget(_base_scan_button_push_button)
        self.top_left_layout.addWidget(_spectrum_scan_button_push_button)
        self.top_left_layout.addWidget(_band_scan_button_push_button)
        self.top_left_layout.addWidget(_jammer_button_push_button)

        self._directory_entry_tool_bar = Qt.QToolBar(self)
        self._directory_entry_tool_bar.addWidget(Qt.QLabel('Directory'+": "))
        self._directory_entry_line_edit = Qt.QLineEdit(str(self.directory))
        self._directory_entry_tool_bar.addWidget(self._directory_entry_line_edit)
        self._directory_entry_line_edit.returnPressed.connect(
        	lambda: self.set_directory_entry(str(str(self._directory_entry_line_edit.text().toAscii()))))
        self.top_right_layout.addWidget(self._directory_entry_tool_bar)

        self._graphic_band_choose_options = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, )
        self._graphic_band_choose_labels = ('ALL', 'CONTINUOUS', '433 MHz', '868 MHz', 'Wifi 2.4GHz (1)',
            'Wifi 2.4GHz (2)', 'Wifi 2.4GHz (3)', 'Wifi 2.4GHz (4)', 'Wifi 2.4GHz (5)',  'Wifi 2.4GHz (6)*',
            'Wifi 2.4GHz (7)*', 'Wifi 2.4GHz (8)*', 'Wifi 2.4GHz (9)*', 'Wifi 2.4GHz (10)*', 
            'GPS L1', 'GPS L2', 'GPS L5')
        self._graphic_band_choose_tool_bar = Qt.QToolBar(self)
        self._graphic_band_choose_tool_bar.addWidget(Qt.QLabel("Choose band"+": "))
        self._graphic_band_choose_combo_box = Qt.QComboBox()
        self._graphic_band_choose_tool_bar.addWidget(self._graphic_band_choose_combo_box)
        for label in self._graphic_band_choose_labels: self._graphic_band_choose_combo_box.addItem(label)
        self._graphic_band_choose_callback = lambda i: Qt.QMetaObject.invokeMethod(self._graphic_band_choose_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._graphic_band_choose_options.index(i)))
        self._graphic_band_choose_callback(self.graphic_band_choose)
        self._graphic_band_choose_combo_box.currentIndexChanged.connect(
            lambda i: self.set_graphic_band_choose(self._graphic_band_choose_options[i]))

        self.top_right_layout.addWidget(self._graphic_band_choose_tool_bar)

        self.dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.top_right_layout.addWidget(self.dynamic_canvas)

        self._dynamic_ax = self.dynamic_canvas.figure.subplots()
        
        self.top_layout.addLayout(self.top_left_layout)
        self.top_layout.addLayout(self.top_right_layout)

        self.updateScanData()    
        self.startUpdateAllTimer()

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
        self.band_timer.setInterval(5000)
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

    def updateScanData(self):
        print("updateScanData")
        powers = []
        freqs = []
        compare_powers = []
        compare_freqs = []
        for center_freq in range(int(self.samp_rate/2),int(6000e6),int(self.samp_rate)):
            self.readFilesForFreq(center_freq, self.samp_rate, self.fft_size, powers, freqs, compare_powers, compare_freqs)
        self.plotNewValues(freqs, powers, compare_freqs, compare_powers)
    
    def updateScanDataForFreq(self):
        print("updateScanDataForFreq {freq}".format(freq=self.center_freq))
        powers = []
        freqs = []
        compare_powers = []
        compare_freqs = []
        self.readFilesForFreq(self.center_freq, self.samp_rate, self.fft_size, powers, freqs, compare_powers, compare_freqs)
        self.plotNewValues(freqs, powers, compare_freqs, compare_powers)    

    def plotNewValues(self, freqs, powers, compare_freqs, compare_powers):
        self._dynamic_ax.clear()
        self._dynamic_ax.plot(compare_freqs, compare_powers, color='red')
        self._dynamic_ax.plot(freqs, powers)
        self._dynamic_ax.figure.canvas.draw()        

    def readFilesForFreq(self, center_freq, samp_rate, fft_size, powers, freqs, compare_powers, compare_freqs):
        file_base_power = "power_%.0fMHz_%.0fMsps_%dFFT" % (center_freq // 1e6, samp_rate // 1e6, fft_size)
        filename_power = "{dir}/{file}.txt".format(dir=self.directory, file=file_base_power)
        file_base_compare = "compare_%.0fMHz_%.0fMsps_%dFFT_1m_1pc_1db" % (center_freq // 1e6, samp_rate // 1e6, fft_size)
        filename_compare = "{dir}/{file}.txt".format(dir=self.directory, file=file_base_compare)
        try:
            file_power = open(filename_power, 'r')
            file_power_index = float(file_power.readline()) #read number of values per row of powers
            compare_exists = False
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
                    max_diff = float(values.split(";")[4])
                    compare_powers.append(power + max_diff)
                    compare_freqs.append(float(line.split("@")[1]))
        except Exception:
            print("Exception reading file {file} or {file2}\n".format(file=file_base_power, file2=file_base_compare))
            return 0
        file_power.close()  
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

    def get_spectrum_scan_button(self):
        return self.spectrum_scan_button

    def set_spectrum_scan_button(self, spectrum_scan_button):
        self.spectrum_scan_button = spectrum_scan_button

    def get_jammer_button(self):
        return self.jammer_button

    def set_jammer_button(self, jammer_button):
        self.jammer_button = jammer_button

    def get_base_scan_button(self):
        return self.base_scan_button

    def set_base_scan_button(self, base_scan_button):
        self.base_scan_button = base_scan_button

    def get_band_scan_button(self):
        return self.band_scan_button

    def set_band_scan_button(self, band_scan_button):
        self.band_scan_button = band_scan_button

    def get_graphic_band_choose(self):
        return self.graphic_band_choose

    def set_graphic_band_choose(self, graphic_band_choose):
        self.cancelUpdateAllTimer()
        self.cancelUpdateBandTimer()
        self.cancelContinuousBandTimer()
        self.graphic_band_choose = graphic_band_choose
        self._graphic_band_choose_callback(self.graphic_band_choose)
        self.index = graphic_band_choose
        if (self.index == 0) :#ALL
            self.updateScanData()
            self.startUpdateAllTimer()
            return
        elif (self.index == 1) :#CONTINUOUS
            self.center_freq = self.samp_rate / 2
            self.updateScanDataForFreq()
            self.startContinuosBandTimer()
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
        elif (self.index == 14): #GPS L1
            self.center_freq = 1570e6 if self.samp_rate == 20e6 else 1575e6
        elif (self.index == 15): #GPS L2
            self.center_freq = 1230e6 if self.samp_rate == 20e6 else 1225e6
        elif (self.index == 16): #GPS L5
            self.center_freq = 1170e6 if self.samp_rate == 20e6 else 1175e6
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
