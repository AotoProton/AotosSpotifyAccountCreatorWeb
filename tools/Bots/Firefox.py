import subprocess
import psutil
from tools.Aoto.Automation import Write, PressAndRelease,\
    WaitWhile_ImageNotOnScreen,\
    WhileImageOn_MoveImmediateClickBreak,\
    IsImageOnScreen, Wait
from tools.Aoto.Locators import Browsers

def IsFirefoxRunning():
    for process in psutil.process_iter():
        try:
            if "firefox".lower() in process.name().lower(): return True
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): pass
def OpenFirefox():
    subprocess.Popen(["C:/Program Files/Mozilla Firefox/firefox.exe"])
def TerminateFirefox():
    while IsFirefoxRunning(): subprocess.Popen("TASKKILL /F /IM firefox.exe",
                                               stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)
    Wait(0.5, 1)

def FindFirefoxSearch():
    WaitWhile_ImageNotOnScreen(Browsers.Firefox.SearchBar, 0.9)
def ClickFirefoxSearch():
    WhileImageOn_MoveImmediateClickBreak(Browsers.Firefox.SearchBar, 0.9), Wait(0.1, 0.3)
def FirefoxSearch(search):
    Write(search, 0.01, 0.03), Wait(0.01, 0.03), PressAndRelease('enter')
def FindFirefoxCloseButton():
    while not IsImageOnScreen(Browsers.Firefox.Close, 0.9)\
            and not IsImageOnScreen(Browsers.Firefox.CloseHighlighted, 0.9): pass
def ClickFirefoxCloseButton():
    if IsImageOnScreen(Browsers.Firefox.Close, 0.9):
        WhileImageOn_MoveImmediateClickBreak(Browsers.Firefox.Close, 0.9)
    if IsImageOnScreen(Browsers.Firefox.CloseHighlighted, 0.9):
        WhileImageOn_MoveImmediateClickBreak(Browsers.Firefox.CloseHighlighted, 0.9)

class FirefoxCacheRemover:
    @staticmethod
    def RemoveFirefoxCache():
        TerminateFirefox()
        OpenFirefox()
        FindFirefoxCloseButton()
        ClickFirefoxCloseButton()
def ClearFirefoxCache():
    FirefoxCacheRemover.RemoveFirefoxCache()

