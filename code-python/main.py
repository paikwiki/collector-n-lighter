import os

from time import localtime, strftime
from conf.Config import Config

config = Config()

t = localtime()

currentDate = strftime("%Y-%m-%d", t)
currentTime = strftime("%H:%M:%S", t)

fileDir = config.DIR_TO_SAVE
fileName = "log_" +  currentDate + ".log"
filePath = "/".join([fileDir, fileName])

os.makedirs(fileDir, exist_ok=True)

f = open(filePath, 'a')
f.write(currentDate + " " + currentTime + " hey\n")
f.close()
