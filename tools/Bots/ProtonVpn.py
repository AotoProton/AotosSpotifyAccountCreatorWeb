import subprocess
import psutil
from tools.Aoto.Automation import IsImageOnScreen,\
    WaitWhile_ImageNotOnScreen,\
    WhileImageOn_MoveImmediateClickBreak,\
    IfImageOn_MoveImmediateClick, Wait
from tools.Aoto.Locators import VPN

def IsProtonVpnRunning():
    for process in psutil.process_iter():
        try:
            if "ProtonVPN".lower() in process.name().lower(): return True
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): pass

def TerminateProtonVpn():
    if IsProtonVpnRunning(): subprocess.Popen("TASKKILL /F /IM ProtonVPN.exe",
                                            stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)

def OpenProtonVpn(): subprocess.Popen(["C:/Program Files (x86)/Proton Technologies/ProtonVPN/ProtonVPN.exe"])

def IsProtonVpnUpgradeMessagePopped():
    if IsImageOnScreen(VPN.ProtonVPN.App.UpgradeButton, 0.9): return True

def FindProtonVpnIcon(): WaitWhile_ImageNotOnScreen(VPN.ProtonVPN.App.TaskbarIcon)

def ClickProtonVpnIcon(): WhileImageOn_MoveImmediateClickBreak(VPN.ProtonVPN.App.TaskbarIcon)

def IsProtonVpnConnected(): return IsImageOnScreen(VPN.ProtonVPN.App.StatusConnected)

def IsProtonVpnDisconnected(): return IsImageOnScreen(VPN.ProtonVPN.App.StatusDisconnected)

def FindProtonVpnStatusConnected():
    while not IsImageOnScreen(VPN.ProtonVPN.App.StatusConnected):
        IfImageOn_MoveImmediateClick(VPN.ProtonVPN.App.QuickConnect), Wait(0.5, 1)

def FindProtonVpnQuickConnect(): WaitWhile_ImageNotOnScreen(VPN.ProtonVPN.App.QuickConnect)

def ClickProtonVpnQuickConnect(): WhileImageOn_MoveImmediateClickBreak(VPN.ProtonVPN.App.QuickConnect)

def FindProtonVpnQuickDisconnect(): WaitWhile_ImageNotOnScreen(VPN.ProtonVPN.App.QuickDisconnect)

def ClickProtonVpnQuickDisconnect(): WhileImageOn_MoveImmediateClickBreak(VPN.ProtonVPN.App.QuickDisconnect)