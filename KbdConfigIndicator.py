#!/usr/bin/env python
# coding: utf-8

import os
import signal
import json
import subprocess
import tkMessageBox
import sys
import AuthWindow
import ConfigParser
from KbdMain import KbdMain
from Tkinter import *

from urllib2 import Request, urlopen, URLError

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


APPINDICATOR_ID = 'KbdConfig'

def main():
	notify.init(APPINDICATOR_ID)

	resultado = None
	while resultado == None or resultado == 1:
		root=Tk()
		m=AuthWindow.popupWindow(root)
		root.mainloop()
		if m.senha != None:
			resultado=subprocess.call("echo " + m.senha + " | sudo -S -v", shell=True)
			if resultado != 1:
				notify.Notification.new("Keyboard", "Permission granted", None).show()

	indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('Img/keyboard_icon.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu(m.senha))
	notify.init(APPINDICATOR_ID)
	gtk.main()
	start_kbd_colors()

def start_kbd_colors():
	status = read_config("general", "status")
	if status == "on":
		left=read_config("colors", "left")
		middle=read_config("colors", "middle")
		right=read_config("colors", "right")
		subprocess.call("sudo su -c 'echo " + left + " > /sys/devices/platform/clevo_wmi/kbled/left'", shell=True)
		subprocess.call("sudo su -c 'echo " + middle + " > /sys/devices/platform/clevo_wmi/kbled/middle'", shell=True)
		subprocess.call("sudo su -c 'echo " + right + " > /sys/devices/platform/clevo_wmi/kbled/right'", shell=True)
	else:
		subprocess.call("sudo su -c 'echo 000 > /sys/devices/platform/clevo_wmi/kbled/left'", shell=True)
		subprocess.call("sudo su -c 'echo 000 > /sys/devices/platform/clevo_wmi/kbled/middle'", shell=True)
		subprocess.call("sudo su -c 'echo 000 > /sys/devices/platform/clevo_wmi/kbled/right'", shell=True)

def build_menu(senha):
	menu = gtk.Menu()
	item_toggle = gtk.MenuItem('Toggle On/Off')
	item_toggle.connect('activate', toggle_lights)
	menu.append(item_toggle)

	item_configure = gtk.MenuItem('Configure')
	item_configure.connect('activate', open_configuration, senha)
	menu.append(item_configure)

	item_quit = gtk.MenuItem('Exit')
	item_quit.connect('activate', quit)
	menu.append(item_quit)
	menu.show_all()
	return menu

def toggle_lights(_):
	status = read_config("general", "status")
	if status == "on":
		subprocess.call("sudo su -c 'echo 000 > /sys/devices/platform/clevo_wmi/kbled/left'", shell=True)
		subprocess.call("sudo su -c 'echo 000 > /sys/devices/platform/clevo_wmi/kbled/middle'", shell=True)
		subprocess.call("sudo su -c 'echo 000 > /sys/devices/platform/clevo_wmi/kbled/right'", shell=True)
		set_config("general", "status", "off")
	else:
		left=read_config("colors", "left")
		middle=read_config("colors", "middle")
		right=read_config("colors", "right")
		subprocess.call("sudo su -c 'echo " + left + " > /sys/devices/platform/clevo_wmi/kbled/left'", shell=True)
		subprocess.call("sudo su -c 'echo " + middle + " > /sys/devices/platform/clevo_wmi/kbled/middle'", shell=True)
		subprocess.call("sudo su -c 'echo " + right + " > /sys/devices/platform/clevo_wmi/kbled/right'", shell=True)
		set_config("general", "status", "on")

def read_config(section, name):
	config = ConfigParser.ConfigParser()
	config.readfp(open('kbd.cfg'))
	return config.get(section, name)

def set_config(section, name, value):
	config = ConfigParser.ConfigParser()
	config.readfp(open('kbd.cfg'))
	config.set(section, name, value)
	with open("kbd.cfg", "w") as configfile:
		config.write(configfile)

def open_configuration(_, senha):
	KbdMain(senha)

if __name__ == '__main__':
    main()