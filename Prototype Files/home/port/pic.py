from picamera import PiCamera
from time import sleep
from escpos.printer import Serial
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(36,GPIO.IN,pull_up_down=GPIO.PUD_UP)

camera = PiCamera()
camera.start_preview()
sleep(2)

while True:
	if GPIO.input(37) == 0:
		print('Shutter Button Pushed')
		camera.capture('/home/port/image.jpg')
		print('Image Taken')
		sleep(1)
		printer = Serial(devfile='/dev/rfcomm0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1.00, dsrdtr=True)
		printer.text('\n')
		printer.image('image.jpg')
		printer.text('\n\n\n\n\n\n')

	if GPIO.input(36) == 0:
		GPIO.cleanup()
		os.system('sudo shutdown -h now')
