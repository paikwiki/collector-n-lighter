class Config:
    # will store logs(one file per a day)
    DIR_LOGS = "/home/pi/codes/collector-n-lighter/logs"
    # will be updated when signal comes in
    FILE_TO_READ = "/home/pi/codes/collector-n-lighter/collector/InputSignal.txt"
    # unit: second
    DELAY_SIGNAL_IN = 5
    # unit: second
    DELAY_DEFAULT = 0.5
    ENDTIME_OF_DAY = "22:00:00"
