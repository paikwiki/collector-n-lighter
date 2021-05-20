import os

from time import localtime, strftime
from conf.Config import Config


class Collector:
    filePath = ""
    timestamp = ""

    # __init__()
    # - set file path
    # - make dir for logs if it's not existed
    def __init__(self):
        self.__setFilePath()
        # exist_ok: not throw
        os.makedirs(Config().DIR_TO_SAVE, exist_ok=True)

    # collect()
    # - update self.timestamp
    # - open and close log file
    # - write a log in a file
    def collect(self):
        # update file path every collect()
        # just in case collector runs over one day
        self.__setFilePath()
        self.__setTimestamp()
        f = open(self.filePath, 'a')  # a: APPEND
        f.write(self.timestamp + "\n")
        f.close()

    # __setTimestamp()
    # - example: 2021-05-20 22:51:05
    def __setTimestamp(self):
        t = localtime()
        cDate = strftime("%Y-%m-%d", t)
        cTime = strftime("%H:%M:%S", t)
        return (" ".join([cDate, cTime]))

    # __setFilePath()
    # - example: ./logs/log_2021-05-20.log
    def __setFilePath(self):
        currentDate = strftime("%Y-%m-%d", localtime())
        fileDir = Config().DIR_TO_SAVE
        fileName = "log_" + currentDate + ".log"
        self.filePath = "/".join([fileDir, fileName])
