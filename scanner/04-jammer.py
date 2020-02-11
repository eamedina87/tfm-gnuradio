#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Feb 10 23:18:28 2020
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sys
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
        self.gui_freq_min = gui_freq_min = 2400
        self.gui_freq_max = gui_freq_max = 2500
        self.freq_min = freq_min = gui_freq_min*1e6
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 0
        self.jammer_amp = jammer_amp = 50
        self.gui_time_switch = gui_time_switch = 50
        self.gui_rf_gain = gui_rf_gain = 14
        self.gui_jam_mode = gui_jam_mode = 1
        self.gui_if_gain = gui_if_gain = 47
        self.freq_max = freq_max = gui_freq_max*1e6
        self.center_freq = center_freq = freq_min+samp_rate/2

        ##################################################
        # Blocks
        ##################################################
        self._jammer_amp_range = Range(1, 100, 1, 50, 200)
        self._jammer_amp_win = RangeWidget(self._jammer_amp_range, self.set_jammer_amp, "jammer_amp", "counter_slider", float)
        
        self._gui_rf_gain_options = (0, 14, )
        self._gui_rf_gain_labels = ('0 db', '14 db', )
        self._gui_rf_gain_group_box = Qt.QGroupBox('RF Gain (db)')
        self._gui_rf_gain_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._gui_rf_gain_button_group = variable_chooser_button_group()
        self._gui_rf_gain_group_box.setLayout(self._gui_rf_gain_box)
        for i, label in enumerate(self._gui_rf_gain_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._gui_rf_gain_box.addWidget(radio_button)
        	self._gui_rf_gain_button_group.addButton(radio_button, i)
        self._gui_rf_gain_callback = lambda i: Qt.QMetaObject.invokeMethod(self._gui_rf_gain_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._gui_rf_gain_options.index(i)))
        self._gui_rf_gain_callback(self.gui_rf_gain)
        self._gui_rf_gain_button_group.buttonClicked[int].connect(
        	lambda i: self.set_gui_rf_gain(self._gui_rf_gain_options[i]))
        
        self._gui_if_gain_range = Range(0, 47, 1, 47, 47)
        self._gui_if_gain_win = RangeWidget(self._gui_if_gain_range, self.set_gui_if_gain, 'IF Gain (db)', "counter_slider", float)
        
        self._variable_qtgui_chooser_0_options = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, )
        self._variable_qtgui_chooser_0_labels = ('None', '433 MHz', '868 MHz', 'Wifi 2.4GHz (1)',
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
        
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(gui_rf_gain, 0)
        self.osmosdr_sink_0.set_if_gain(gui_if_gain, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(samp_rate, 0)

        self._gui_time_switch_range = Range(50, 1500, 50, 50, 200)
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
        
        self._gui_jam_mode_options = (1, 2, )
        self._gui_jam_mode_labels = ('Fixed Band (20 MHz)', 'Continuous ', )
        self._gui_jam_mode_tool_bar = Qt.QToolBar(self)
        self._gui_jam_mode_tool_bar.addWidget(Qt.QLabel('Jammer Mode'+": "))
        self._gui_jam_mode_combo_box = Qt.QComboBox()
        self._gui_jam_mode_tool_bar.addWidget(self._gui_jam_mode_combo_box)
        for label in self._gui_jam_mode_labels: self._gui_jam_mode_combo_box.addItem(label)
        self._gui_jam_mode_callback = lambda i: Qt.QMetaObject.invokeMethod(self._gui_jam_mode_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._gui_jam_mode_options.index(i)))
        self._gui_jam_mode_callback(self.gui_jam_mode)
        self._gui_jam_mode_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_gui_jam_mode(self._gui_jam_mode_options[i]))
        
        self._gui_freq_min_range = Range(0, 6000-samp_rate/1e6, samp_rate/1e6, 2400, 200)
        self._gui_freq_min_win = RangeWidget(self._gui_freq_min_range, self.set_gui_freq_min, 'Lower Frequency (MHz)', "counter_slider", float)
        
        self._gui_freq_max_range = Range(10, 6000, samp_rate/1e6, 2500, 200)
        self._gui_freq_max_win = RangeWidget(self._gui_freq_max_range, self.set_gui_freq_max, 'Higher Frequency (MHz)', "counter_slider", float)
        
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((6, ))
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_UNIFORM, jammer_amp, 0)

        self.top_layout.addWidget(self._gui_samp_rate_tool_bar)
        self.top_layout.addWidget(self._jammer_amp_win)
        self.top_layout.addWidget(self._gui_rf_gain_group_box)
        self.top_layout.addWidget(self._gui_if_gain_win)
        self.top_layout.addWidget(self._gui_jam_mode_tool_bar)
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_tool_bar)
        self.top_layout.addWidget(self._gui_freq_min_win)
        self.top_layout.addWidget(self._gui_freq_max_win)
        self.top_layout.addWidget(self._gui_time_switch_win)
                
        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.osmosdr_sink_0, 0))

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
        self.set_center_freq(self.freq_min+self.samp_rate/2)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_bandwidth(self.samp_rate, 0)
        self.set_gui_freq_max(self.gui_freq_min+self.samp_rate/1e6)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_gui_freq_min(self):
        return self.gui_freq_min

    def set_gui_freq_min(self, gui_freq_min):
        self.gui_freq_min = gui_freq_min
        self.set_freq_min(self.gui_freq_min*1e6)

    def get_gui_freq_max(self):
        return self.gui_freq_max

    def set_gui_freq_max(self, gui_freq_max):
        self.gui_freq_max = gui_freq_max
        self.set_freq_max(self.gui_freq_max*1e6)

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self.index = variable_qtgui_chooser_0
        self.rate = self.get_samp_rate()
        if (self.index == 0) :#None
            self.set_gui_freq_min(0)
            self.set_gui_freq_max(self.samp_rate/1e6)
            self.set_center_freq(10e6 if self.rate == 20e6 else 5e6)
        elif (self.index == 1): #433MHz     
            self.set_center_freq(430e6 if self.rate == 20e6 else 435e6)
        elif (self.index == 2): #868MHz
            self.set_center_freq(870e6 if self.rate == 20e6 else 865e6)
        elif (self.index == 3): #Wifi 2.4 1
            self.set_center_freq(2410e6 if self.rate == 20e6 else 2405e6)        
        elif (self.index == 4): #Wifi 2.4 2
            self.set_center_freq(2430e6 if self.rate == 20e6 else 2415e6)
        elif (self.index == 5): #Wifi 2.4 3
            self.set_center_freq(2450e6 if self.rate == 20e6 else 2425e6)
        elif (self.index == 6): #Wifi 2.4 4
            self.set_center_freq(2470e6 if self.rate == 20e6 else 2435e6)
        elif (self.index == 7): #Wifi 2.4 5
            self.set_center_freq(2490e6 if self.rate == 20e6 else 2445e6)
        elif (self.index == 8): #Wifi 2.4 6
            self.set_center_freq(2490e6 if self.rate == 20e6 else 2455e6)
        elif (self.index == 9): #Wifi 2.4 7
            self.set_center_freq(2490e6 if self.rate == 20e6 else 2465e6)
        elif (self.index == 10): #Wifi 2.4 8
            self.set_center_freq(2490e6 if self.rate == 20e6 else 2475e6)
        elif (self.index == 11): #Wifi 2.4 9
            self.set_center_freq(2490e6 if self.rate == 20e6 else 2485e6)
        elif (self.index == 12): #Wifi 2.4 10
            self.set_center_freq(2490e6 if self.rate == 20e6 else 2495e6)
        elif (self.index == 13): #GPS L1
            self.set_center_freq(1570e6 if self.rate == 20e6 else 1575e6)
        elif (self.index == 14): #GPS L2
            self.set_center_freq(1230e6 if self.rate == 20e6 else 1225e6)
        elif (self.index == 15): #GPS L5
            self.set_center_freq(1170e6 if self.rate == 20e6 else 1175e6)

    def get_jammer_amp(self):
        return self.jammer_amp

    def set_jammer_amp(self, jammer_amp):
        self.jammer_amp = jammer_amp
        self.analog_noise_source_x_0.set_amplitude(self.jammer_amp)

    def get_gui_time_switch(self):
        return self.gui_time_switch

    def set_gui_time_switch(self, gui_time_switch):
        self.gui_time_switch = gui_time_switch
        self.startTimer()

    def get_gui_rf_gain(self):
        return self.gui_rf_gain

    def set_gui_rf_gain(self, gui_rf_gain):
        self.gui_rf_gain = gui_rf_gain
        self._gui_rf_gain_callback(self.gui_rf_gain)
        self.osmosdr_sink_0.set_gain(self.gui_rf_gain, 0)

    def get_gui_jam_mode(self):
        return self.gui_jam_mode

    def set_gui_jam_mode(self, gui_jam_mode):
        self.gui_jam_mode = gui_jam_mode
        self._gui_jam_mode_callback(self.gui_jam_mode)
        if (gui_jam_mode == 2):
            self.startTimer()
        else:
            self.stopTimer()


    def get_gui_if_gain(self):
        return self.gui_if_gain

    def set_gui_if_gain(self, gui_if_gain):
        self.gui_if_gain = gui_if_gain
        self.osmosdr_sink_0.set_if_gain(self.gui_if_gain, 0)

    def get_freq_min(self):
        return self.freq_min

    def set_freq_min(self, freq_min):
        print("Freq  Min")
        print(freq_min)
        self.freq_min = freq_min
        self.set_center_freq(self.freq_min+self.samp_rate/2)

    def get_freq_max(self):
        return self.freq_max

    def set_freq_max(self, freq_max):
        print("Freq Max")
        print(freq_max)
        self.freq_max = freq_max

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        print("Center Freq")
        print(center_freq)
        self.center_freq = center_freq
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)

    def startTimer(self):
        self.stopTimer()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.gui_time_switch)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def stopTimer(self):
        try:
            self.timer.stop()
        except Exception as e:
            print("Timer not initialized")

    def recurring_timer(self):
        if (self.get_center_freq()+self.samp_rate >= self.get_freq_max()):
            self.set_center_freq(self.get_freq_min()+self.samp_rate/2)
        else:
            self.set_center_freq(self.get_center_freq()+self.samp_rate)

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
