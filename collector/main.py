import os
from typing import Any
from time import sleep, localtime, strftime, strptime
# from datetime import datetime
from Collector import Collector
from conf.Config import Config
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(Config.PIR_PIN, GPIO.IN, GPIO.PUD_UP)

collector = Collector()


def isEnd():
    currentTime = localtime()
    currentDate = strftime("%Y-%m-%d", currentTime)
    string = " ".join([currentDate, Config.ENDTIME_OF_DAY])
    tm = strptime(string, '%Y-%m-%d %H:%M:%S')
    if tm < currentTime:
        return True
    return False
while (not isEnd()):
    if GPIO.input(Config.PIR_PIN):
        collector.collect()
        sleep(Config.DELAY_SIGNAL_IN)
    else:
        sleep(Config.DELAY_DEFAULT)
