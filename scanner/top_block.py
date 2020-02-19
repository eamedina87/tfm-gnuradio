#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Drone Detection
# Author: Erick Medina Moreno
# Description: Pool of scripts that run different processes to detect  drones
# Generated: Wed Feb 19 16:48:32 2020
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
        self.spectrum_scan_button = spectrum_scan_button = 0
        self.jammer_button = jammer_button = 0
        self.graphic_band_choose = graphic_band_choose = 0
        self.directory_entry = directory_entry = 'home'
        self.base_scan_button = base_scan_button = 0
        self.band_scan_button = band_scan_button = 0

        ##################################################
        # Blocks
        ##################################################
        _spectrum_scan_button_push_button = Qt.QPushButton('Spectrum Scan')
        self._spectrum_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _spectrum_scan_button_push_button.pressed.connect(lambda: self.set_spectrum_scan_button(self._spectrum_scan_button_choices['Pressed']))
        _spectrum_scan_button_push_button.released.connect(lambda: self.set_spectrum_scan_button(self._spectrum_scan_button_choices['Released']))
        self.top_layout.addWidget(_spectrum_scan_button_push_button)
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
        self._directory_entry_tool_bar = Qt.QToolBar(self)
        self._directory_entry_tool_bar.addWidget(Qt.QLabel('Directory'+": "))
        self._directory_entry_line_edit = Qt.QLineEdit(str(self.directory_entry))
        self._directory_entry_tool_bar.addWidget(self._directory_entry_line_edit)
        self._directory_entry_line_edit.returnPressed.connect(
        	lambda: self.set_directory_entry(str(str(self._directory_entry_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._directory_entry_tool_bar)
        _base_scan_button_push_button = Qt.QPushButton('Base Scan')
        self._base_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _base_scan_button_push_button.pressed.connect(lambda: self.set_base_scan_button(self._base_scan_button_choices['Pressed']))
        _base_scan_button_push_button.released.connect(lambda: self.set_base_scan_button(self._base_scan_button_choices['Released']))
        self.top_layout.addWidget(_base_scan_button_push_button)
        _band_scan_button_push_button = Qt.QPushButton('Band Scan')
        self._band_scan_button_choices = {'Pressed': 1, 'Released': 0}
        _band_scan_button_push_button.pressed.connect(lambda: self.set_band_scan_button(self._band_scan_button_choices['Pressed']))
        _band_scan_button_push_button.released.connect(lambda: self.set_band_scan_button(self._band_scan_button_choices['Released']))
        self.top_layout.addWidget(_band_scan_button_push_button)

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_spectrum_scan_button(self):
        return self.spectrum_scan_button

    def set_spectrum_scan_button(self, spectrum_scan_button):
        self.spectrum_scan_button = spectrum_scan_button

    def get_jammer_button(self):
        return self.jammer_button

    def set_jammer_button(self, jammer_button):
        self.jammer_button = jammer_button

    def get_graphic_band_choose(self):
        return self.graphic_band_choose

    def set_graphic_band_choose(self, graphic_band_choose):
        self.graphic_band_choose = graphic_band_choose
        self._graphic_band_choose_callback(self.graphic_band_choose)

    def get_directory_entry(self):
        return self.directory_entry

    def set_directory_entry(self, directory_entry):
        self.directory_entry = directory_entry
        Qt.QMetaObject.invokeMethod(self._directory_entry_line_edit, "setText", Qt.Q_ARG("QString", str(self.directory_entry)))

    def get_base_scan_button(self):
        return self.base_scan_button

    def set_base_scan_button(self, base_scan_button):
        self.base_scan_button = base_scan_button

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
