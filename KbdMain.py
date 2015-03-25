#!/usr/bin/env python

import sys
import pygtk
import subprocess

from gi.repository import Gtk

class KbdMain:

	def __init__(self):
		filename = "KbdConfig.glade"
		builder = Gtk.Builder()
		builder.add_from_file(filename)
		builder.connect_signals(self)
		window = builder.get_object("wdwMain")
		window.set_title("KbdConfig")
		window.show_all()

		self.prepareButtons(builder)

		window.connect("delete-event", Gtk.main_quit)
		Gtk.main()

	def prepareButtons(self, builder):
		builder.get_object("rdbtnLeftOff").connect("clicked", self.colorClick, "Off", "left")
		builder.get_object("rdbtnLeftWhite").connect("clicked", self.colorClick, "White", "left")
		builder.get_object("rdbtnLeftGreen").connect("clicked", self.colorClick, "Green", "left")
		builder.get_object("rdbtnLeftRed").connect("clicked", self.colorClick, "Red", "left")
		builder.get_object("rdbtnLeftBlue").connect("clicked", self.colorClick, "Blue", "left")
		builder.get_object("rdbtnLeftYellow").connect("clicked", self.colorClick, "Yellow", "left")
		builder.get_object("rdbtnLeftPurple").connect("clicked", self.colorClick, "Purple", "left")
		builder.get_object("rdbtnLeftAqua").connect("clicked", self.colorClick, "Aqua", "left")

		builder.get_object("rdbtnMiddleOff").connect("clicked", self.colorClick, "Off", "middle")
		builder.get_object("rdbtnMiddleWhite").connect("clicked", self.colorClick, "White", "middle")
		builder.get_object("rdbtnMiddleGreen").connect("clicked", self.colorClick, "Green", "middle")
		builder.get_object("rdbtnMiddleRed").connect("clicked", self.colorClick, "Red", "middle")
		builder.get_object("rdbtnMiddleBlue").connect("clicked", self.colorClick, "Blue", "middle")
		builder.get_object("rdbtnMiddleYellow").connect("clicked", self.colorClick, "Yellow", "middle")
		builder.get_object("rdbtnMiddlePurple").connect("clicked", self.colorClick, "Purple", "middle")
		builder.get_object("rdbtnMiddleAqua").connect("clicked", self.colorClick, "Aqua", "middle")

		builder.get_object("rdbtnRightOff").connect("clicked", self.colorClick, "Off", "right")
		builder.get_object("rdbtnRightWhite").connect("clicked", self.colorClick, "White", "right")
		builder.get_object("rdbtnRightGreen").connect("clicked", self.colorClick, "Green", "right")
		builder.get_object("rdbtnRightRed").connect("clicked", self.colorClick, "Red", "right")
		builder.get_object("rdbtnRightBlue").connect("clicked", self.colorClick, "Blue", "right")
		builder.get_object("rdbtnRightYellow").connect("clicked", self.colorClick, "Yellow", "right")
		builder.get_object("rdbtnRightPurple").connect("clicked", self.colorClick, "Purple", "right")
		builder.get_object("rdbtnRightAqua").connect("clicked", self.colorClick, "Aqua", "right")


	def colorClick(self, widget, value, position):
		if widget.get_active():
			code = self.convertColorNameToCode(value)
			self.changeKeyboardColor(code, position)

	def changeKeyboardColor(self, code, position):
		subprocess.call("echo " + code + " > /sys/devices/platform/clevo_wmi/kbled/" + position, shell=True)

	def convertColorNameToCode(self, colorName):
		if colorName == "Off":
			return "000"

		if colorName == "White":
			return "111"

		if colorName == "Green":
			return "100"

		if colorName == "Red":
			return "010"

		if colorName == "Blue":
			return "001"

		if colorName == "Yellow":
			return "110"

		if colorName == "Purple":
			return "011"

		if colorName == "Aqua":
			return "101"