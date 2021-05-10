from time import localtime, strftime

t = localtime()

currentDate = strftime("%Y-%m-%d", t)
currentTime = strftime("%H:%M:%S", t)

fileName = "log_" +  currentDate + ".log"

f = open(fileName, 'a')
f.write(currentDate + " " + currentTime + " hey\n")
f.close()
