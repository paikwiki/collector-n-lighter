import os
from typing import Any
from time import sleep
from Lighter import Lighter
from conf.Config import Config

lighter: Any = Lighter()

while lighter.isEnd == False:
    lighter.light()
    sleep(Config.DELAY_DEFAULT)

print("Lighter end")
