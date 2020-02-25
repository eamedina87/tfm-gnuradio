#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Drone Detection
# Author: Erick Medina Moreno
# Description: Pool of scripts that run different processes to detect  drones
# Generated: Tue Feb 25 13:04:36 2020
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
import sys
from gnuradio import qtgui


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
        self.update_graph_button = update_graph_button = 0
        self.spectrum_scan_button = spectrum_scan_button = 0
        self.samp_rate_chooser = samp_rate_chooser = 20
        self.jammer_button = jammer_button = 0
        self.graphic_band_choose = graphic_band_choose = 0
        self.fft_size_chooser = fft_size_chooser = 1024
        self.directory_entry = directory_entry = 'home'
        self.center_freq_range = center_freq_range = 3000
        self.base_scan_button = base_scan_button = 0
        self.bandwidth_range = bandwidth_range = 20
        self.band_scan_button = band_scan_button = 0

        ##################################################
        # Blocks
        ##################################################
        _update_graph_button_push_button = Qt.QPushButton('Update Graph')
        self._update_graph_button_choices = {'Pressed': 1, 'Released': 0}
        _update_graph_button_push_button.pressed.connect(lambda: self.set_update_graph_button(self._update_graph_button_choices['Pressed']))
        _update_graph_button_push_button.released.connect(lambda: self.set_update_graph_button(self._update_graph_button_choices['Released']))
        self.top_layout.addWidget(_update_graph_button_push_button)

        _spectrum_scan_button_push_button = Qt.QPushButton('Spectrum Scan')
        self._spectrum_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _spectrum_scan_button_push_button.pressed.connect(lambda: self.set_spectrum_scan_button(self._spectrum_scan_button_choices['Pressed']))
        _spectrum_scan_button_push_button.released.connect(lambda: self.set_spectrum_scan_button(self._spectrum_scan_button_choices['Released']))
        self.top_layout.addWidget(_spectrum_scan_button_push_button)
        
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
        self.top_layout.addWidget(self._samp_rate_chooser_tool_bar)
        
        _jammer_button_push_button = Qt.QPushButton('Jammer')
        self._jammer_button_choices = {'Pressed': 1, 'Released': 0}
        _jammer_button_push_button.pressed.connect(lambda: self.set_jammer_button(self._jammer_button_choices['Pressed']))
        _jammer_button_push_button.released.connect(lambda: self.set_jammer_button(self._jammer_button_choices['Released']))
        self.top_layout.addWidget(_jammer_button_push_button)
        
        self._graphic_band_choose_options = (0, 1, 2, )
        self._graphic_band_choose_labels = (str(self._graphic_band_choose_options[0]), str(self._graphic_band_choose_options[1]), str(self._graphic_band_choose_options[2]), )
        self._graphic_band_choose_tool_bar = Qt.QToolBar(self)
        self._graphic_band_choose_tool_bar.addWidget(Qt.QLabel("graphic_band_choose"+": "))
        self._graphic_band_choose_combo_box = Qt.QComboBox()
        self._graphic_band_choose_tool_bar.addWidget(self._graphic_band_choose_combo_box)
        for label in self._graphic_band_choose_labels: self._graphic_band_choose_combo_box.addItem(label)
        self._graphic_band_choose_callback = lambda i: Qt.QMetaObject.invokeMethod(self._graphic_band_choose_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._graphic_band_choose_options.index(i)))
        self._graphic_band_choose_callback(self.graphic_band_choose)
        self._graphic_band_choose_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_graphic_band_choose(self._graphic_band_choose_options[i]))
        self.top_layout.addWidget(self._graphic_band_choose_tool_bar)
        
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
        self.top_layout.addWidget(self._fft_size_chooser_tool_bar)
        
        self._directory_entry_tool_bar = Qt.QToolBar(self)
        self._directory_entry_tool_bar.addWidget(Qt.QLabel('Directory'+": "))
        self._directory_entry_line_edit = Qt.QLineEdit(str(self.directory_entry))
        self._directory_entry_tool_bar.addWidget(self._directory_entry_line_edit)
        self._directory_entry_line_edit.returnPressed.connect(
        	lambda: self.set_directory_entry(str(str(self._directory_entry_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._directory_entry_tool_bar)
        
        self._center_freq_range_range = Range(10, 6000, 10, 3000, 200)
        self._center_freq_range_win = RangeWidget(self._center_freq_range_range, self.set_center_freq_range, 'Center Frequency', "counter_slider", float)
        self.top_layout.addWidget(self._center_freq_range_win)
        
        _base_scan_button_push_button = Qt.QPushButton('Base Scan')
        self._base_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _base_scan_button_push_button.pressed.connect(lambda: self.set_base_scan_button(self._base_scan_button_choices['Pressed']))
        _base_scan_button_push_button.released.connect(lambda: self.set_base_scan_button(self._base_scan_button_choices['Released']))
        self.top_layout.addWidget(_base_scan_button_push_button)
        
        self._bandwidth_range_range = Range(10, 6000, 10, 20, 200)
        self._bandwidth_range_win = RangeWidget(self._bandwidth_range_range, self.set_bandwidth_range, 'Bandwidth', "counter_slider", float)
        self.top_layout.addWidget(self._bandwidth_range_win)
        
        _band_scan_button_push_button = Qt.QPushButton('Band Scan')
        self._band_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _band_scan_button_push_button.pressed.connect(lambda: self.set_band_scan_button(self._band_scan_button_choices['Pressed']))
        _band_scan_button_push_button.released.connect(lambda: self.set_band_scan_button(self._band_scan_button_choices['Released']))
        self.top_layout.addWidget(_band_scan_button_push_button)

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_update_graph_button(self):
        return self.update_graph_button

    def set_update_graph_button(self, update_graph_button):
        self.update_graph_button = update_graph_button

    def get_spectrum_scan_button(self):
        return self.spectrum_scan_button

    def set_spectrum_scan_button(self, spectrum_scan_button):
        self.spectrum_scan_button = spectrum_scan_button

    def get_samp_rate_chooser(self):
        return self.samp_rate_chooser

    def set_samp_rate_chooser(self, samp_rate_chooser):
        self.samp_rate_chooser = samp_rate_chooser
        self._samp_rate_chooser_callback(self.samp_rate_chooser)

    def get_jammer_button(self):
        return self.jammer_button

    def set_jammer_button(self, jammer_button):
        self.jammer_button = jammer_button

    def get_graphic_band_choose(self):
        return self.graphic_band_choose

    def set_graphic_band_choose(self, graphic_band_choose):
        self.graphic_band_choose = graphic_band_choose
        self._graphic_band_choose_callback(self.graphic_band_choose)

    def get_fft_size_chooser(self):
        return self.fft_size_chooser

    def set_fft_size_chooser(self, fft_size_chooser):
        self.fft_size_chooser = fft_size_chooser
        self._fft_size_chooser_callback(self.fft_size_chooser)

    def get_directory_entry(self):
        return self.directory_entry

    def set_directory_entry(self, directory_entry):
        self.directory_entry = directory_entry
        Qt.QMetaObject.invokeMethod(self._directory_entry_line_edit, "setText", Qt.Q_ARG("QString", str(self.directory_entry)))

    def get_center_freq_range(self):
        return self.center_freq_range

    def set_center_freq_range(self, center_freq_range):
        self.center_freq_range = center_freq_range

    def get_base_scan_button(self):
        return self.base_scan_button

    def set_base_scan_button(self, base_scan_button):
        self.base_scan_button = base_scan_button

    def get_bandwidth_range(self):
        return self.bandwidth_range

    def set_bandwidth_range(self, bandwidth_range):
        self.bandwidth_range = bandwidth_range

    def get_band_scan_button(self):
        return self.band_scan_button

    def set_band_scan_button(self, band_scan_button):
        self.band_scan_button = band_scan_button


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
