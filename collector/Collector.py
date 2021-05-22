import os
from typing import Any
from time import localtime, strftime, struct_time
from conf.Config import Config

class Collector:
    __filePath: str = ""
    __timestamp: str = ""

    # __init__()
    # - set file path
    # - make dir for logs if it's not existed
    def __init__(self):
        self.__setFilePath()
        # exist_ok: not throw
        os.makedirs(Config.DIR_LOGS, exist_ok=True)

    # collect()
    # - update self.__timestamp
    # - open and close log file
    # - write a log in a file
    def collect(self):
        # update file path every collect()
        # just in case collector runs over one day
        self.__setFilePath()
        self.__setTimestamp()
        _f : Any = open(self.__filePath, 'a')  # a: APPEND
        _f.write(self.__timestamp + "\n")
        _f.close()

    # __setTimestamp()
    # - example: 2021-05-20 22:51:05
    def __setTimestamp(self):
        t: struct_time = localtime()
        _cDate: str = strftime("%Y-%m-%d", t)
        _cTime: str = strftime("%H:%M:%S", t)
        self.__timestamp = " ".join([_cDate, _cTime])

    # __setFilePath()
    # - example: ./logs/log_2021-05-20.log
    def __setFilePath(self):
        currentDate = strftime("%Y-%m-%d", localtime())
        _fileDir: str = Config.DIR_LOGS
        _fileName: str = "log_" + currentDate + ".log"
        self.__filePath = "/".join([_fileDir, _fileName])
