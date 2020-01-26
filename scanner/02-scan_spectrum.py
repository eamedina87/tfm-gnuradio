#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Jan 22 23:38:50 2020
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
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
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
        self.gui_samp_rate = gui_samp_rate = 20
        self.samp_rate = samp_rate = gui_samp_rate*1e6
        self.gui_fft_size = gui_fft_size = 1024
        self.fft_size = fft_size = gui_fft_size
        self.gui_time_switch = gui_time_switch = 250
        self.time_switch = time_switch = gui_time_switch
        self.gui_freq_min = gui_freq_min = 0
        self.freq_min = freq_min = gui_freq_min
        self.gui_freq_max = gui_freq_max = gui_freq_min+samp_rate/1e6
        self.freq_max = freq_max = gui_freq_max
        self.gui_directory = gui_directory = "/home/eamedina/Documentos/freq_docs/ui"
        self.gui_update_btn = gui_update_btn = 0
        self.gui_mode_value = gui_mode_value = 1
        self.gui_mode = gui_mode = 1
        self.freq = freq = freq_min+(samp_rate/2)
        self.directory = directory = gui_directory

        ##################################################
        # Blocks
        ##################################################
        self._gui_mode_value_range = Range(1, 100, 1, 1, 100)
        self._gui_mode_value_win = RangeWidget(self._gui_mode_value_range, self.set_gui_mode_value, 'Mode Value (% or db)', "counter_slider", float)
        
        self._gui_freq_min_range = Range(0, 6000-samp_rate/1e6, samp_rate/1e6, 0, 200)
        self._gui_freq_min_win = RangeWidget(self._gui_freq_min_range, self.set_gui_freq_min, 'Lower Frequency (MHz)', "counter_slider", float)
        
        self.tfm_power_comparator_ff_0 = tfm.power_comparator_ff(self.samp_rate, self.freq, self.fft_size, self.directory, gui_mode, gui_mode_value, gui_mode_value)
        self.tfm_logpowerfft_win_0 = tfm.logpowerfft_win(self.samp_rate, self.fft_size, 2, 30)
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

        _gui_update_btn_push_button = Qt.QPushButton('Update Params')
        self._gui_update_btn_choices = {'Pressed': 1, 'Released': 0}
        _gui_update_btn_push_button.pressed.connect(lambda: self.set_gui_update_btn(self._gui_update_btn_choices['Pressed']))
        _gui_update_btn_push_button.released.connect(lambda: self.set_gui_update_btn(self._gui_update_btn_choices['Released']))
        
        self._gui_time_switch_range = Range(50, 1500, 50, 250, 200)
        self._gui_time_switch_win = RangeWidget(self._gui_time_switch_range, self.set_gui_time_switch, 'Frequency Switch Time (ms)', "counter_slider", float)
        
        self._gui_samp_rate_options = (10, 20, )
        self._gui_samp_rate_labels = ('10 Msps', '20 Msps', )
        self._gui_samp_rate_tool_bar = Qt.QToolBar(self)
        self._gui_samp_rate_tool_bar.addWidget(Qt.QLabel('Sample Rate'+": "))
        self._gui_samp_rate_combo_box = Qt.QComboBox()
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
        
        self._gui_freq_max_range = Range(gui_freq_min+samp_rate/1e6, 6000, samp_rate/1e6, gui_freq_min+samp_rate/1e6, 200)
        self._gui_freq_max_win = RangeWidget(self._gui_freq_max_range, self.set_gui_freq_max, 'Higher Frequency (MHz)', "counter_slider", float)
        
        self._gui_fft_size_options = (1024, 2048, )
        self._gui_fft_size_labels = (str(self._gui_fft_size_options[0]), str(self._gui_fft_size_options[1]), )
        self._gui_fft_size_tool_bar = Qt.QToolBar(self)
        self._gui_fft_size_tool_bar.addWidget(Qt.QLabel('FFT size'+": "))
        self._gui_fft_size_combo_box = Qt.QComboBox()
        self._gui_fft_size_tool_bar.addWidget(self._gui_fft_size_combo_box)
        for label in self._gui_fft_size_labels: self._gui_fft_size_combo_box.addItem(label)
        self._gui_fft_size_callback = lambda i: Qt.QMetaObject.invokeMethod(self._gui_fft_size_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._gui_fft_size_options.index(i)))
        self._gui_fft_size_callback(self.gui_fft_size)
        self._gui_fft_size_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_gui_fft_size(self._gui_fft_size_options[i]))
        
        self._gui_directory_tool_bar = Qt.QToolBar(self)
        self._gui_directory_tool_bar.addWidget(Qt.QLabel('Directory'+": "))
        self._gui_directory_line_edit = Qt.QLineEdit(str(self.gui_directory))
        self._gui_directory_tool_bar.addWidget(self._gui_directory_line_edit)
        self._gui_directory_line_edit.returnPressed.connect(
        	lambda: self.set_gui_directory(str(str(self._gui_directory_line_edit.text().toAscii()))))

        self.top_layout.addWidget(self._gui_samp_rate_tool_bar)
        self.top_layout.addWidget(self._gui_fft_size_tool_bar)
        self.top_layout.addWidget(self._gui_freq_min_win)
        self.top_layout.addWidget(self._gui_freq_max_win)
        self.top_layout.addWidget(self._gui_mode_tool_bar)
        self.top_layout.addWidget(self._gui_mode_value_win)
        self.top_layout.addWidget(self._gui_directory_tool_bar)
        self.top_layout.addWidget(self._gui_time_switch_win)
        self.top_layout.addWidget(_gui_update_btn_push_button)
        

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.tfm_logpowerfft_win_0, 0))
        self.connect((self.tfm_logpowerfft_win_0, 0), (self.tfm_power_comparator_ff_0, 0))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(time_switch)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def recurring_timer(self):
        print("Timer executed")
        if (self.get_freq()+self.samp_rate >= self.get_freq_max()):
            self.set_freq(self.get_freq_min()+self.samp_rate/2)
        else:
            self.set_freq(self.get_freq()+self.samp_rate)

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
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.set_gui_freq_max(self.gui_freq_min+self.samp_rate/1e6)
        self.logpwrfft_x_0.set_sample_rate(self.samp_rate)

    def get_gui_time_switch(self):
        return self.gui_time_switch

    def set_gui_time_switch(self, gui_time_switch):
        self.gui_time_switch = gui_time_switch
        self.set_time_switch(self.gui_time_switch)

    def get_gui_freq_min(self):
        return self.gui_freq_min

    def set_gui_freq_min(self, gui_freq_min):
        self.gui_freq_min = gui_freq_min
        self.set_gui_freq_max(self.gui_freq_min+self.samp_rate/1e6)

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

    def get_time_switch(self):
        return self.time_switch

    def set_time_switch(self, time_switch):
        self.time_switch = time_switch

    def get_gui_update_btn(self):
        return self.gui_update_btn

    def set_gui_update_btn(self, gui_update_btn):
        self.gui_update_btn = gui_update_btn
        #todo update eveything

    def get_gui_mode_value(self):
        return self.gui_mode_value

    def set_gui_mode_value(self, gui_mode_value):
        self.gui_mode_value = gui_mode_value

    def get_gui_mode(self):
        return self.gui_mode

    def set_gui_mode(self, gui_mode):
        self.gui_mode = gui_mode
        self._gui_mode_callback(self.gui_mode)

    def get_gui_freq_max(self):
        return self.gui_freq_max

    def set_gui_freq_max(self, gui_freq_max):
        self.gui_freq_max = gui_freq_max

    def get_freq_max(self):
        return self.freq_max

    def set_freq_max(self, freq_max):
        self.freq_max = freq_max

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        print("Set Freq executed")
        self.freq = freq
        self.osmosdr_source_0.set_center_freq(self.freq, 0)
        self.tfm_power_comparator_ff_0.set_center_freq(self.freq)

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
