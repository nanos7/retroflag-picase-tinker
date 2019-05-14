#!/usr/bin/env python

import ASUS.GPIO as GPIO
import time
import os
import subprocess

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.ASUS)

# Pin en ASUS BOARD
# pin 3
powerPin = 253
# pin 2
resetPin = 252
# pin 8
ledPin = 161
# pin 7
powerenPin = 17

hold = 1

GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(powerenPin,GPIO.OUT)
GPIO.setup(powerPin,GPIO.IN)
GPIO.setup(resetPin,GPIO.IN)
GPIO.output(ledPin,GPIO.HIGH)
GPIO.output(powerenPin,GPIO.HIGH)

# Funciones
def ledon():
	# Encender led
	GPIO.output(ledPin,GPIO.HIGH)

def ledoff():
	# Apagar led
	GPIO.output(ledPin,GPIO.LOW)
	
def led_blink():
	#Encender
	ledon()
	time.sleep(0.5)
	#Apagar
	ledoff()
	time.sleep(0.5)

# Pressed
def	poweroff():
	led_blink()
	output = int(subprocess.check_output(['/opt/RetroFlag/multi_switch.sh', '--es-pid']))
	if output:
		os.system("/opt/RetroFlag/multi_switch.sh --es-poweroff")
	else:
		os.system("sudo shutdown -h now")

# Released
def poweron():
	ledon()

def reboot():
	output = int(subprocess.check_output(['/opt/RetroFlag/multi_switch.sh', '--es-pid']))
	output_rc = int(subprocess.check_output(['/opt/RetroFlag/multi_switch.sh', '--rc-pid']))
	if output_rc:
		os.system("/opt/RetroFlag/multi_switch.sh --closeemu")
	elif output:
		os.system("/opt/RetroFlag/multi_switch.sh --es-restart")
	else:
		os.system("sudo reboot")
	
try:
	while True:
		if GPIO.input(resetPin) == GPIO.LOW:
			reboot()
		elif GPIO.input(powerPin):
			poweron()
		else:
			poweroff()
except KeyboardInterrupt:
	GPIO.cleanup()

