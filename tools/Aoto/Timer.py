import time

global startTime
global endTime

def StartTimer():
    global startTime
    startTime = time.time()

def EndTimer():
    global endTime
    endTime = time.time()

def TimeTaken():
    global startTime
    global endTime
    timeLapsedInSeconds = endTime - startTime
    mins = timeLapsedInSeconds // 60
    sec = timeLapsedInSeconds % 60
    sec = str(sec)
    sec = sec[0:sec.index('.')]
    sec = int(sec)
    hours = mins // 60
    mins = mins % 60
    return "HR:{0} MIN:{1} SEC:{2}".format(int(hours), int(mins), sec)