import os

from time import localtime, strftime
from conf.Config import Config

class Collector:
	currentDate = strftime("%Y-%m-%d", localtime())
	fileDir = Config().DIR_TO_SAVE
	fileName = "log_" +  currentDate + ".log"
	filePath = "/".join([fileDir, fileName])

	def __init__(self):
		os.makedirs(self.fileDir, exist_ok=True)
	def getTimestamp(self):
		t = localtime()
		cDate = strftime("%Y-%m-%d", t)
		cTime = strftime("%H:%M:%S", t)
		return (" ".join([cDate, cTime]))
	def collect(self):
		f = open(self.filePath, 'a')
		f.write(self.getTimestamp() + "\n")
		f.close()
