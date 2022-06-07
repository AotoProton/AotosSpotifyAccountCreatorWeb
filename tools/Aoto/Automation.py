import os.path
from time import sleep
from random import uniform, randint
from pyclick import humanclicker, humancurve
import pyautogui
import pytweening
import keyboard
import speech_recognition as sr
from pydub import AudioSegment
import getpass

def ConvertMp3ToWav_FromDownloadsFolder_AudioNamed_audio():
    src = "C:/Users/" + getpass.getuser() + "/Downloads/audio.mp3"
    dst = "C:/Users/" + getpass.getuser() + "/Downloads/audio.wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

def WavToText_FromDownloadsFolder_AudioNamed_audio():
    while not os.path.exists("C:/Users/" + getpass.getuser() + "/Downloads/" + "audio.wav"): pass
    r = sr.Recognizer()
    audio = sr.AudioFile("C:/Users/" + getpass.getuser() + "/Downloads/" + "audio.wav")
    with audio as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text

def Wait(Min, Max): sleep(uniform(Min, Max))

def WaitWhile_ImageNotOnScreen(imageDirectory, accuracy=0.75):
    while pyautogui.locateOnScreen(imageDirectory, confidence=accuracy) is None: pass

def IsImageOnScreen(imageDirectory, accuracy=0.75):
    if pyautogui.locateOnScreen(imageDirectory, confidence=accuracy) is not None:return True

def RandomMouseEase():
    easeIndex = randint(1, 3)
    if easeIndex == 1:
        ease = pytweening.easeInQuad
        return ease
    elif easeIndex == 2:
        ease = pytweening.easeInOutQuad
        return ease
    elif easeIndex == 3:
        ease = pytweening.easeOutQuad
        return ease

def Move(image):
    try:
        fromPoint = pyautogui.position()
        toPoint = (image[0], image[1])
        options = {
            "offsetBoundaryX": randint(25 ,150),
            "offsetBoundaryY": randint(25 ,150),
            "knotsCount": randint(1 ,6),
            "distortionMean": randint(1 ,6),
            "distortionStdev": randint(1 ,6),
            "distortionFrequency": 0.5,
            "tweening": RandomMouseEase(),
            "targetPoints": randint(25 ,200),
            }
        human_curve = humancurve.HumanCurve(fromPoint=fromPoint, toPoint=toPoint, **options)
        hc = humanclicker.HumanClicker()
        hc.move(toPoint=toPoint, duration=uniform(uniform(0.01, 0.05), uniform(0.05, 1)) , humanCurve=human_curve)
    except: input("[MOUSE ERROR]")

def MoveImmediate(image):
    fromPoint = pyautogui.position()
    toPoint = (image[0], image[1])
    options = {
        "offsetBoundaryX": randint(50, 150),
        "offsetBoundaryY": randint(50, 150),
        "knotsCount": randint(1, 3),
        "distortionMean": uniform(0.5, 1.5),
        "distortionStdev": uniform(0.5, 1.5),
        "distortionFrequency": uniform(0.25, 1),
        "tweening": pytweening.easeOutQuad,
        "targetPoints": 100,
        }
    human_curve = humancurve.HumanCurve(fromPoint=fromPoint, toPoint=toPoint, **options)
    hc = humanclicker.HumanClicker()
    hc.move(toPoint=toPoint, duration=0, humanCurve=human_curve)

def Click(): humanclicker.HumanClicker().click()

def Write(text, speedMin=uniform(0.01, 0.02), speedMax=uniform(0.02, 0.3)):
    for letter in range(len(text)):
        pyautogui.write(text[letter], uniform(speedMin, speedMax))

def WriteImmediate(text): pyautogui.write(text)

def PressAndRelease(key): keyboard.press_and_release(key, 'space')

def Scroll(amount): pyautogui.scroll(amount)

def IfImageOn_MoveImmediateClick(imageDirectory, accuracy=0.75):
    if pyautogui.locateOnScreen(imageDirectory, confidence=accuracy) is not None:
        location = pyautogui.locateOnScreen(imageDirectory, confidence=accuracy)
        Wait(0.01, 0.03)
        MoveImmediate(location)
        Wait(0.01, 0.03)
        Click()
        Wait(0.01, 0.03)

def IfImageOn_MoveImmediateDoubleClickBreak(imageDirectory, accuracy=0.75):
    if pyautogui.locateOnScreen(imageDirectory, confidence=accuracy) is not None:
        location = pyautogui.locateOnScreen(imageDirectory, confidence=accuracy)
        Wait(0.01, 0.03)
        MoveImmediate(location)
        Wait(0.01, 0.03)
        Click()
        Click()
        Wait(0.01, 0.03)

def WhileImageOn_MoveClickBreak(imageDirectory, accuracy=0.75):
    while pyautogui.locateOnScreen(imageDirectory, confidence=accuracy) is not None:
        location = pyautogui.locateOnScreen(imageDirectory, confidence=accuracy)
        Wait(0.01, 0.03)
        Move(location)
        Wait(0.01, 0.03)
        Click()
        Wait(0.01, 0.03)
        break

def WhileImageOn_MoveImmediateClickBreak(imageDirectory, accuracy=0.75):
    while pyautogui.locateOnScreen(imageDirectory, confidence=accuracy) is not None:
        location = pyautogui.locateOnScreen(imageDirectory, confidence=accuracy)
        Wait(0.01, 0.03)
        MoveImmediate(location)
        Wait(0.1, 0.3)
        Click()
        Wait(0.1, 0.3)
        break

def WhileImageOn_MoveDoubleClickBreak(imageDirectory, accuracy=0.75):
    while pyautogui.locateOnScreen(imageDirectory, confidence=accuracy) is not None:
        location = pyautogui.locateOnScreen(imageDirectory, confidence=accuracy)
        Wait(0.01, 0.03)
        Move(location)
        Wait(0.01, 0.03)
        Click()
        Click()
        Wait(0.01, 0.03)
        break

def WhileImageOn_MoveImmediateDoubleClickBreak(imageDirectory, accuracy=0.75):
    while pyautogui.locateOnScreen(imageDirectory, confidence=accuracy) is not None:
        location = pyautogui.locateOnScreen(imageDirectory, confidence=accuracy)
        Wait(0.01, 0.03)
        MoveImmediate(location)
        Wait(0.01, 0.03)
        Click()
        Click()
        Wait(0.01, 0.03)
        break
