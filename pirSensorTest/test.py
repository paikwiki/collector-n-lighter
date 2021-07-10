import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pirPin = 7
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)

temp = 0 
while True:
    if GPIO.input(pirPin):
        print("Motion", temp)
        temp = temp + 1
    else:
        print("...")
    time.sleep(0.5)