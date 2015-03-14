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
		window.show_all()

		self.prepareButtons(builder)

		window.connect("delete-event", Gtk.main_quit)
		Gtk.main()

	def prepareButtons(self, builder):
		builder.get_object("rdbtnLeftOff").connect("clicked", self.leftColorClick, "Off")
		builder.get_object("rdbtnLeftWhite").connect("clicked", self.leftColorClick, "White")
		builder.get_object("rdbtnLeftGreen").connect("clicked", self.leftColorClick, "Green")
		builder.get_object("rdbtnLeftRed").connect("clicked", self.leftColorClick, "Red")
		builder.get_object("rdbtnLeftBlue").connect("clicked", self.leftColorClick, "Blue")
		builder.get_object("rdbtnLeftYellow").connect("clicked", self.leftColorClick, "Yellow")
		builder.get_object("rdbtnLeftPurple").connect("clicked", self.leftColorClick, "Purple")
		builder.get_object("rdbtnLeftAqua").connect("clicked", self.leftColorClick, "Aqua")

		builder.get_object("rdbtnMiddleOff").connect("clicked", self.middleColorClick, "Off")
		builder.get_object("rdbtnMiddleWhite").connect("clicked", self.middleColorClick, "White")
		builder.get_object("rdbtnMiddleGreen").connect("clicked", self.middleColorClick, "Green")
		builder.get_object("rdbtnMiddleRed").connect("clicked", self.middleColorClick, "Red")
		builder.get_object("rdbtnMiddleBlue").connect("clicked", self.middleColorClick, "Blue")
		builder.get_object("rdbtnMiddleYellow").connect("clicked", self.middleColorClick, "Yellow")
		builder.get_object("rdbtnMiddlePurple").connect("clicked", self.middleColorClick, "Purple")
		builder.get_object("rdbtnMiddleAqua").connect("clicked", self.middleColorClick, "Aqua")

		builder.get_object("rdbtnRightOff").connect("clicked", self.rightColorClick, "Off")
		builder.get_object("rdbtnRightWhite").connect("clicked", self.rightColorClick, "White")
		builder.get_object("rdbtnRightGreen").connect("clicked", self.rightColorClick, "Green")
		builder.get_object("rdbtnRightRed").connect("clicked", self.rightColorClick, "Red")
		builder.get_object("rdbtnRightBlue").connect("clicked", self.rightColorClick, "Blue")
		builder.get_object("rdbtnRightYellow").connect("clicked", self.rightColorClick, "Yellow")
		builder.get_object("rdbtnRightPurple").connect("clicked", self.rightColorClick, "Purple")
		builder.get_object("rdbtnRightAqua").connect("clicked", self.rightColorClick, "Aqua")


	def leftColorClick(self, widget, value):
		if widget.get_active():
			code = self.convertColorNameToCode(value)
			self.changeKeyboardColor(code, "left")

	def middleColorClick(self, widget, value):
		if widget.get_active():
			code = self.convertColorNameToCode(value)
			self.changeKeyboardColor(code, "middle")

	def rightColorClick(self, widget, value):
		if widget.get_active():
			code = self.convertColorNameToCode(value)
			self.changeKeyboardColor(code, "right")

	def changeKeyboardColor(self, code, position):
		print "echo " + code + " > /sys/devices/platform/clevo_wmi/kbled/" + position
		print ""
		print ""
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