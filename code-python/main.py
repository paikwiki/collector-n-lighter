import os
from time import sleep
from Collector import Collector
from conf.Config import Config

collector = Collector()
config = Config()

readFile = config.FILE_TO_READ
lastmod = int(os.path.getmtime(readFile))
while True:
	if lastmod != int(os.path.getmtime(readFile)):
		lastmod = int(os.path.getmtime(readFile))
		collector.collect()
	sleep(1)
