import os
from typing import Any
from time import sleep, localtime, strftime, strptime
# from datetime import datetime
from Collector import Collector
from conf.Config import Config

collector = Collector()
readFile = Config.FILE_TO_READ
lastmod = int(os.path.getmtime(readFile))

def isEnd():
    currentTime = localtime()
    currentDate = strftime("%Y-%m-%d", currentTime)
    string = " ".join([currentDate, Config.ENDTIME_OF_DAY])
    tm = strptime(string, '%Y-%m-%d %H:%M:%S')
    if tm < currentTime:
        return True
    return False
while (not isEnd()):
    if lastmod != int(os.path.getmtime(readFile)):
        collector.collect()
        sleep(Config.DELAY_SIGNAL_IN)
        lastmod = int(os.path.getmtime(readFile))
    else:
        sleep(Config.DELAY_DEFAULT)
