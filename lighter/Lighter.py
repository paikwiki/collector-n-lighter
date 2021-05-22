from time import localtime, strftime, struct_time
from conf.Config import Config

class Lighter:
    __filePath: str = ""
    __timestamp: str = ""

    def __init__(self):

        self.__setFilePath()

    def light(self):
        self.__setFilePath()
        self.__setTimestamp()
        print("Lighter will read from", self.__filePath, ".")
        print("Light is turned on if there is a", self.__timestamp, "log.")

    # __setTimestamp()
    # - example: 2021-05-20 22:51:05
    # TODO: filePath의 날짜와 현재시간을 조합하여 시간을 반환하도록 변경
    def __setTimestamp(self):
        t: struct_time = localtime()
        _cDate: str = strftime("%Y-%m-%d", t)
        _cTime: str = strftime("%H:%M:%S", t)
        self.__timestamp = " ".join([_cDate, _cTime])

    # __setFilePath()
    # - example: ./logs/log_2021-05-20.log
    # TODO: 가장 최신의 파일을 가져오도록 변경
    def __setFilePath(self):
        currentDate = strftime("%Y-%m-%d", localtime())
        _fileDir: str = Config.DIR_LOGS
        _fileName: str = "log_" + currentDate + ".log"
        self.__filePath = "/".join([_fileDir, _fileName])
