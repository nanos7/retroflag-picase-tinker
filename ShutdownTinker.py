#!/usr/bin/env python

import ASUS.GPIO as GPIO
import time
import os

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

def poweroff():
	led_blink()
	os.system("sudo killall emulationstation && sleep 5s && sudo shutdown -h now")
	
def poweron():
	ledon()

try:
	while True:
		if GPIO.input(powerPin):
			poweron()
		else:
			poweroff()
except KeyboardInterrupt:
	GPIO.cleanup()


#power = LED(powerenPin)
#power.on()



#functions that handle button events
def when_pressed():
  led.blink(.2,.2)
  os.system("sudo killall emulationstation && sleep 5s && sudo shutdown -h now")
def when_released():
  led.on()
def reboot(): 
  os.system("sudo killall emulationstation && sleep 5s && sudo reboot")
  
#btn = Button(powerPin, hold_time=hold)
#rebootBtn = Button(resetPin)
#rebootBtn.when_pressed = reboot 
#btn.when_pressed = when_pressed
#btn.when_released = when_released
#pause()
