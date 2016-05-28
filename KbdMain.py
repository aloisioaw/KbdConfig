#!/usr/bin/env python

import sys
import pygtk
import subprocess
import ConfigParser

from gi.repository import Gtk
from KbdConstants import KbdConstants

class KbdMain:

	def __init__(self, senha):
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
		self.attachClickColorChange(builder, "Left")
		self.attachClickColorChange(builder, "Middle")
		self.attachClickColorChange(builder, "Right")

	def attachClickColorChange(self, builder, position):
		for color in KbdConstants.COLORS:
			builder.get_object("rdbtn" + position + color).connect("clicked", self.colorClick, color, position.lower())

	def colorClick(self, widget, value, position):
		if widget.get_active():
			code = self.convertColorNameToCode(value)
			self.changeKeyboardColor(code, position)

	def changeKeyboardColor(self, code, position):
		subprocess.call("sudo su -c 'echo " + code + " > /sys/devices/platform/clevo_wmi/kbled/" + position + "'", shell=True)
		self.set_config("colors", position, code)


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

	def set_config(self, section, name, value):
		config = ConfigParser.ConfigParser()
		config.readfp(open("kbd.cfg"))
		config.set(section, name, value)
		with open("kbd.cfg", "w") as configfile:
			config.write(configfile)
