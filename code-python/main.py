from time import sleep
from Collector import Collector

collector = Collector()
while True:
	collector.collect()
	sleep(1)
