import os
from time import localtime, strftime, struct_time, mktime, time
from conf.Config import Config
from time import sleep
import datetime

class Lighter:
    targetFile = NotImplemented

    __filePath: str = ""
    __days_ago: int = 0

    def __init__(self):
        self.__setFilePath()

    def light(self):

        # 파일 열기
        if (self.__filePath != ""):
            self.targetFile = open(self.__filePath)
        if not self.targetFile: return

        line = self.targetFile.readline().rstrip()

        # 빈 파일일 경우 끝내기
        if not line:
            self.targetFile.close()
            return
        curr = datetime.datetime.now() - datetime.timedelta(days=self.__days_ago)
        seconds = mktime(datetime.datetime.strptime(line, "%Y-%m-%d %H:%M:%S").timetuple())
        parsedLine = datetime.datetime.fromtimestamp(seconds)

        # 지나간 로그를 스킵하고 타겟이 되는 로그를 가져옴
        # 타겟이 되는 로그의 조건: parsedLine이 curr보다 크거나 같은 경우
        while (parsedLine < curr):
            line = self.targetFile.readline().rstrip()
            if not line: break # 더이상 읽어올 게 없거나 빈 줄을 만나면 while 종료

            seconds = mktime(datetime.datetime.strptime(line, "%Y-%m-%d %H:%M:%S").timetuple())
            parsedLine = datetime.datetime.fromtimestamp(seconds)
        print(parsedLine, " - ", curr, " = ", parsedLine - curr)

        # 타겟이 되는 로그가 불을 켜야하는 상태인지 체크
        if (parsedLine >= curr and parsedLine <= curr + datetime.timedelta(seconds=Config.DELAY_DEFAULT + 0.1)): # TODO: 혹시 몰라서 패딩값 적용
            print(">> Light ON")
            sleep(Config.DELAY_LIGHT_ON)
            print("<< Light OFF")

        # 파일 닫기
        self.targetFile.close()

    # __setFilePath()
    # - example: ./logs/log_2021-05-20.log
    # 가장 최신의 파일을 가져오도록 변경. Config.RANGE_TO_FIND의 날짜만큼 탐색
    def __setFilePath(self):
        currentDate = datetime.datetime.now()
        fileDir: str = Config.DIR_LOGS
        for days_ago in range(1, Config.RANGE_TO_FIND):
            fileDate = currentDate - datetime.timedelta(days=days_ago)
            fileName: str = "log_" + fileDate.strftime("%Y-%m-%d") + ".log"
            filePath: str = "/".join([fileDir, fileName])
            if os.path.isfile(filePath):
                self.__filePath = filePath
                self.__days_ago = days_ago
                break
        if (self.__filePath == ""):
            print("Error: Log file does not exist.")
        else:
            print(self.__filePath)
