import os
from typing import Any
from time import sleep
from Collector import Collector
from conf.Config import Config

collector : Any = Collector()
readFile : str = Config.FILE_TO_READ
lastmod : int = int(os.path.getmtime(readFile))

while True:
    if lastmod != int(os.path.getmtime(readFile)):
        collector.collect()
        sleep(Config.DELAY_SIGNAL_IN)
        lastmod = int(os.path.getmtime(readFile))
    else:
        sleep(Config.DELAY_DEFAULT)
