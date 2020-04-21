#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Feb  3 15:39:07 2020
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
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import tfm
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################

        arguments = sys.argv[1:]
        hasArguments = len(arguments) == 3 

        self.gui_samp_rate = gui_samp_rate = 20 if not hasArguments else int(sys.argv[2])
        self.samp_rate = samp_rate = gui_samp_rate*1e6
        self.gui_fft_size = gui_fft_size = 1024 if not hasArguments else int(sys.argv[3])
        self.gui_directory = gui_directory = "/home/eamedina/Documentos/freq_docs/fft" if not hasArguments else sys.argv[1]
        self.freq_min = freq_min = 420e6
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 0
        self.gui_mode_value = gui_mode_value = 1
        self.gui_mode = gui_mode = 2
        self.freq_max = freq_max = 440e6
        self.freq = freq = freq_min+(samp_rate/2)
        self.fft_size = fft_size = gui_fft_size
        self.directory = directory = gui_directory

        ##################################################
        # Blocks
        ##################################################
        self._gui_mode_value_range = Range(1, 100, 1, 10, 100)
        self._gui_mode_value_win = RangeWidget(self._gui_mode_value_range, self.set_gui_mode_value, 'Mode Value (% or db)', "counter_slider", float)

        self._gui_frequency_range = Range(samp_rate/2e6, 6e6 - samp_rate/2e6, samp_rate/1e6, freq/1e6, 6e6/samp_rate)
        self._gui_frequency_win = RangeWidget(self._gui_frequency_range, self.set_gui_freq, 'Center Frequency', "counter_slider", float)
        
        self._variable_qtgui_chooser_0_options = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, )
        self._variable_qtgui_chooser_0_labels = ('433 MHz', '868 MHz', 'Wifi 2.4GHz (1)',
            'Wifi 2.4GHz (2)', 'Wifi 2.4GHz (3)', 'Wifi 2.4GHz (4)', 'Wifi 2.4GHz (5)',  'Wifi 2.4GHz (6)',
            'Wifi 2.4GHz (7)*', 'Wifi 2.4GHz (8)*', 'Wifi 2.4GHz (9)*', 'Wifi 2.4GHz (10)*', 
            'GPS L1', 'GPS L2', 'GPS L5', )
        self._variable_qtgui_chooser_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_0_tool_bar.addWidget(Qt.QLabel('Preset Bands'+": "))
        self._variable_qtgui_chooser_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_0_tool_bar.addWidget(self._variable_qtgui_chooser_0_combo_box)
        for label in self._variable_qtgui_chooser_0_labels: self._variable_qtgui_chooser_0_combo_box.addItem(label)
        self._variable_qtgui_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_options.index(i)))
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self._variable_qtgui_chooser_0_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_variable_qtgui_chooser_0(self._variable_qtgui_chooser_0_options[i]))
        
        self.tfm_power_comparator_ff_0 = tfm.power_comparator_ff(self.samp_rate, self.freq, self.fft_size, self.directory, 1, gui_mode_value, gui_mode_value)
        self.tfm_logpowerfft_win_0 = tfm.logpowerfft_win(self.samp_rate, self.fft_size, 2, 30)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	fft_size, #fftsize
        	firdes.WIN_HAMMING, #wintype
        	freq, #fc
        	samp_rate, #bw
        	'Band Analysis', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	False, #plottime
        	False, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        
        self.qtgui_sink_x_0.enable_rf_freq(True)

        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(0, 0)
        self.osmosdr_source_0.set_bb_gain(0, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self._gui_samp_rate_options = (10, 20, )
        self._gui_samp_rate_labels = ('10 Msps', '20 Msps', )
        self._gui_samp_rate_tool_bar = Qt.QToolBar(self)
        self._gui_samp_rate_tool_bar.addWidget(Qt.QLabel('Sample Rate'+": "))
        self._gui_samp_rate_combo_box = Qt.QComboBox()
        self._gui_samp_rate_combo_box.setEnabled(False)
        self._gui_samp_rate_tool_bar.addWidget(self._gui_samp_rate_combo_box)
        for label in self._gui_samp_rate_labels: self._gui_samp_rate_combo_box.addItem(label)
        self._gui_samp_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._gui_samp_rate_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._gui_samp_rate_options.index(i)))
        self._gui_samp_rate_callback(self.gui_samp_rate)
        self._gui_samp_rate_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_gui_samp_rate(self._gui_samp_rate_options[i]))
        
        self._gui_mode_options = (1, 2, )
        self._gui_mode_labels = ('Percentage (%)', 'Value (db)', )
        self._gui_mode_tool_bar = Qt.QToolBar(self)
        self._gui_mode_tool_bar.addWidget(Qt.QLabel('Mode'+": "))
        self._gui_mode_combo_box = Qt.QComboBox()
        self._gui_mode_tool_bar.addWidget(self._gui_mode_combo_box)
        for label in self._gui_mode_labels: self._gui_mode_combo_box.addItem(label)
        self._gui_mode_callback = lambda i: Qt.QMetaObject.invokeMethod(self._gui_mode_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._gui_mode_options.index(i)))
        self._gui_mode_callback(self.gui_mode)
        self._gui_mode_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_gui_mode(self._gui_mode_options[i]))
        
        self._gui_fft_size_options = (1024, 2048, )
        self._gui_fft_size_labels = (str(self._gui_fft_size_options[0]), str(self._gui_fft_size_options[1]), )
        self._gui_fft_size_tool_bar = Qt.QToolBar(self)
        self._gui_fft_size_tool_bar.addWidget(Qt.QLabel('FFT size'+": "))
        self._gui_fft_size_combo_box = Qt.QComboBox()
        self._gui_fft_size_combo_box.setEnabled(False)
        self._gui_fft_size_tool_bar.addWidget(self._gui_fft_size_combo_box)
        for label in self._gui_fft_size_labels: self._gui_fft_size_combo_box.addItem(label)
        self._gui_fft_size_callback = lambda i: Qt.QMetaObject.invokeMethod(self._gui_fft_size_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._gui_fft_size_options.index(i)))
        self._gui_fft_size_callback(self.gui_fft_size)
        self._gui_fft_size_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_gui_fft_size(self._gui_fft_size_options[i]))
        
        self._gui_directory_tool_bar = Qt.QToolBar(self)
        self._gui_directory_tool_bar.addWidget(Qt.QLabel('Directory'+": "))
        self._gui_directory_line_edit = Qt.QLineEdit(str(self.gui_directory))
        self._gui_directory_line_edit.setReadOnly(True)
        self._gui_directory_tool_bar.addWidget(self._gui_directory_line_edit)
        self._gui_directory_line_edit.returnPressed.connect(
        	lambda: self.set_gui_directory(str(str(self._gui_directory_line_edit.text().toAscii()))))
        
        self.top_layout.addWidget(self._gui_directory_tool_bar)
        self.top_layout.addWidget(self._gui_samp_rate_tool_bar)
        self.top_layout.addWidget(self._gui_fft_size_tool_bar)
        self.top_layout.addWidget(self._gui_frequency_win)
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_tool_bar)
        self.top_layout.addWidget(self._gui_mode_tool_bar)
        self.top_layout.addWidget(self._gui_mode_value_win)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.tfm_logpowerfft_win_0, 0))
        self.connect((self.tfm_logpowerfft_win_0, 0), (self.tfm_power_comparator_ff_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_gui_samp_rate(self):
        return self.gui_samp_rate

    def set_gui_samp_rate(self, gui_samp_rate):
        self.gui_samp_rate = gui_samp_rate
        self.set_samp_rate(self.gui_samp_rate*1e6)
        self._gui_samp_rate_callback(self.gui_samp_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_freq(self.freq_min+(self.samp_rate/2))
        self.qtgui_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_gui_fft_size(self):
        return self.gui_fft_size

    def set_gui_fft_size(self, gui_fft_size):
        self.gui_fft_size = gui_fft_size
        self.set_fft_size(self.gui_fft_size)
        self._gui_fft_size_callback(self.gui_fft_size)

    def get_gui_directory(self):
        return self.gui_directory

    def set_gui_directory(self, gui_directory):
        self.gui_directory = gui_directory
        self.set_directory(self.gui_directory)
        Qt.QMetaObject.invokeMethod(self._gui_directory_line_edit, "setText", Qt.Q_ARG("QString", str(self.gui_directory)))

    def get_freq_min(self):
        return self.freq_min

    def set_freq_min(self, freq_min):
        self.freq_min = freq_min
        self.set_freq(self.freq_min+(self.samp_rate/2))

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self.index = variable_qtgui_chooser_0
        self.rate = self.get_samp_rate()
        if (self.index == 0) :#433MHz
            self.set_freq(430e6 if self.rate == 20e6 else 435e6)
        elif (self.index == 1): #868MHz
            self.set_freq(870e6 if self.rate == 20e6 else 865e6)
        elif (self.index == 2): #Wifi 2.4 1
            self.set_freq(2410e6 if self.rate == 20e6 else 2405e6)        
        elif (self.index == 3): #Wifi 2.4 2
            self.set_freq(2430e6 if self.rate == 20e6 else 2415e6)
        elif (self.index == 4): #Wifi 2.4 3
            self.set_freq(2450e6 if self.rate == 20e6 else 2425e6)
        elif (self.index == 5): #Wifi 2.4 4
            self.set_freq(2470e6 if self.rate == 20e6 else 2435e6)
        elif (self.index == 6): #Wifi 2.4 5
            self.set_freq(2490e6 if self.rate == 20e6 else 2445e6)
        elif (self.index == 7): #Wifi 2.4 6
            self.set_freq(2490e6 if self.rate == 20e6 else 2455e6)
        elif (self.index == 8): #Wifi 2.4 7
            self.set_freq(2490e6 if self.rate == 20e6 else 2465e6)
        elif (self.index == 9): #Wifi 2.4 8
            self.set_freq(2490e6 if self.rate == 20e6 else 2475e6)
        elif (self.index == 10): #Wifi 2.4 9
            self.set_freq(2490e6 if self.rate == 20e6 else 2485e6)
        elif (self.index == 11): #Wifi 2.4 10
            self.set_freq(2490e6 if self.rate == 20e6 else 2495e6)
        elif (self.index == 12): #GPS L1
            self.set_freq(1570e6 if self.rate == 20e6 else 1575e6)
        elif (self.index == 13): #GPS L2
            self.set_freq(1230e6 if self.rate == 20e6 else 1225e6)
        elif (self.index == 14): #GPS L5
            self.set_freq(1170e6 if self.rate == 20e6 else 1175e6)

    def get_gui_mode_value(self):
        return self.gui_mode_value

    def set_gui_mode_value(self, gui_mode_value):
        self.gui_mode_value = gui_mode_value
        if (self.gui_mode == 1):
            self.tfm_power_comparator_ff_0.set_diff_percentage(gui_mode_value)
        else:
            self.tfm_power_comparator_ff_0.set_diff_db(gui_mode_value)

    def get_gui_mode(self):
        return self.gui_mode

    def set_gui_mode(self, gui_mode):
        self.gui_mode = gui_mode
        self._gui_mode_callback(self.gui_mode)
        self.tfm_power_comparator_ff_0.set_mode(gui_mode)
        self.set_gui_mode_value(self.get_gui_mode_value())

    def get_freq_max(self):
        return self.freq_max

    def set_freq_max(self, freq_max):
        self.freq_max = freq_max

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)
        self.tfm_power_comparator_ff_0.set_center_freq(self.freq)

    def set_gui_freq(self, freq):
        self.set_freq(freq*1e6)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_directory(self):
        return self.directory

    def set_directory(self, directory):
        self.directory = directory


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
