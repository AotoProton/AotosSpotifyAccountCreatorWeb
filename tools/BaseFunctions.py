import os
from os import system
import keyboard
from tools.Aoto.Automation import Wait
from tools.Aoto.Text import PrintTextOverlap
from tools.Aoto.UI import Space, TextBox, Bright_Cyan_Text
import getpass

def SetTitle(title_name: str):
    system("title {0}".format(title_name))

def IfSpacePressed_PauseAccountCreation():
    if keyboard.is_pressed('space'): input(TextBox("PAUSE") + Space() +
                                           Bright_Cyan_Text("Do you want to continue?"))

def RemoveDownloadedMp3():
    if os.path.exists("C:/Users/" + getpass.getuser() + "/Downloads/audio.mp3"):
        os.remove("C:/Users/" + getpass.getuser() + "/Downloads/audio.mp3")

def RemoveConvertedWav():
    if os.path.exists("C:/Users/" + getpass.getuser() + "/Downloads/audio.wav"):
        os.remove("C:/Users/" + getpass.getuser() + "/Downloads/audio.wav")

def Remove_FirstItemOfList(lines):
    lines.__delitem__(0)
    return lines

def Readlines_FromEmailsToUseFile_ThenClose():
    emailsToUseFile = open(os.getcwd() + "/config/" + "EmailsToUse.txt", 'r')
    lines = emailsToUseFile.readlines(), emailsToUseFile.close()
    return lines

def TruncateAndWriteLines_ToEmailsToUseFile_ThenClose(lines):
    emailsToUseFile = open(os.getcwd() + "/config/" + "EmailsToUse.txt", 'r+')
    emailsToUseFile.truncate(), emailsToUseFile.writelines(lines), emailsToUseFile.close()

def GetTotalAccounts():
    return len(open("created.txt", "r").readlines())

def IsCreatedFileDoesntExist():
    if not os.path.exists(os.getcwd() + "/" + "created.txt"): return True

def CreateSaveFile():
    if IsCreatedFileDoesntExist(): open("created.txt", "a+"), Wait(3, 5)

def SaveToFile(credentials):
    CreateSaveFile()
    open("created.txt", "a+").write(credentials['email'] + ":" + credentials['password'] + "\n")

def CreatedAccountInformation(credentials, timeTaken):
    PrintTextOverlap(TextBox("CREATED") + Space() +
                     TextBox("EMAIL") + Bright_Cyan_Text(credentials['email']) + Space() +
                     TextBox("PASSWORD") + Bright_Cyan_Text(credentials['password']) + Space() +
                     TextBox("TIME") + Bright_Cyan_Text(timeTaken) + Space() +
                     TextBox("TOTAL") + Bright_Cyan_Text(str(GetTotalAccounts())))
