from tools.Aoto.Automation import Wait,\
    Write,\
    PressAndRelease,\
    Scroll,\
    IsImageOnScreen,\
    ConvertMp3ToWav_FromDownloadsFolder_AudioNamed_audio,\
    WavToText_FromDownloadsFolder_AudioNamed_audio,\
    WaitWhile_ImageNotOnScreen,\
    WhileImageOn_MoveDoubleClickBreak,\
    WhileImageOn_MoveClickBreak
from tools.Aoto.Locators import Captcha, Windows
from tools.Bots.ExceptionHandler import IsExceptionOccured

class SolveCaptcha:
    @staticmethod
    def Initialize():
        if not SolveCaptcha.FindCaptchaBox(): return False
        SolveCaptcha.ClickCaptchaBox()
        if not SolveCaptcha.FindAudioOption(): return False
        SolveCaptcha.ClickAudioOption()
        if SolveCaptcha.IsCaptchaVerified(): return True
        if not SolveCaptcha.FindDownloadAudioButton(): return False
        SolveCaptcha.ClickDownloadAudioButton()
        if not SolveCaptcha.FindAudioDownloadPage(): return False
        SolveCaptcha.DownloadAudio()
        SolveCaptcha.GoBackToCaptchaVerifyPage()
        SolveCaptcha.FindAudioTextInputField(), SolveCaptcha.ClickAudioTextInputField()
        SolveCaptcha.WriteAudioTextInputField(SolveCaptcha.ConvertMp3ToWav_ReturnAudioText())
        SolveCaptcha.EnterAudioTextInputField()
        if not SolveCaptcha.WaitCaptchaVerification(): return False
        return True

    @staticmethod
    def FindCaptchaBox(tries=3):
        while not IsImageOnScreen(Captcha.StartBox):
            for _ in range(tries):
                if IsExceptionOccured(): return False
                if IsImageOnScreen(Captcha.StartBox): return True
                Scroll(-400)
            return False
        return True
    @staticmethod
    def ClickCaptchaBox():
        WhileImageOn_MoveDoubleClickBreak(Captcha.StartBox)
        Scroll(-200)
    @staticmethod
    def FindAudioOption():
        while not IsImageOnScreen(Captcha.AudioOption) and not SolveCaptcha.IsCaptchaVerified():
            if IsExceptionOccured(): return False
        return True
    @staticmethod
    def ClickAudioOption():
        WhileImageOn_MoveDoubleClickBreak(Captcha.AudioOption)
    @staticmethod
    def FindDownloadAudioButton():
        while not IsImageOnScreen(Captcha.AudioDownload):
            if IsExceptionOccured(): return False
            if IsImageOnScreen(Captcha.AudioOption) and not SolveCaptcha.IsCaptchaVerified():
                WhileImageOn_MoveDoubleClickBreak(Captcha.AudioOption)
        return True
    @staticmethod
    def ClickDownloadAudioButton():
        WhileImageOn_MoveClickBreak(Captcha.AudioDownload)
    @staticmethod
    def FindAudioDownloadPage():
        while not IsImageOnScreen(Captcha.AudioDownloadPage):
            if IsExceptionOccured(): return False
            if IsImageOnScreen(Captcha.AudioDownload): WhileImageOn_MoveClickBreak(Captcha.AudioDownload)
        return True
    @staticmethod
    def DownloadAudio():
        while IsImageOnScreen(Captcha.AudioDownloadPage):
            PressAndRelease('ctrl+s')
            WaitWhile_ImageNotOnScreen(Windows.SaveDownloadButton)
            while IsImageOnScreen(Windows.SaveDownloadButton):PressAndRelease('enter'), Wait(0.01, 0.03)
            if not IsImageOnScreen(Windows.SaveDownloadButton):return
    @staticmethod
    def GoBackToCaptchaVerifyPage():
        Wait(0.01, 0.03)
        PressAndRelease('ctrl+w')
    @staticmethod
    def ConvertMp3ToWav_ReturnAudioText():
        ConvertMp3ToWav_FromDownloadsFolder_AudioNamed_audio()
        return WavToText_FromDownloadsFolder_AudioNamed_audio()
    @staticmethod
    def FindAudioTextInputField(): WaitWhile_ImageNotOnScreen(Captcha.AudioInputField)
    @staticmethod
    def ClickAudioTextInputField(): WhileImageOn_MoveDoubleClickBreak(Captcha.AudioInputField)
    @staticmethod
    def WriteAudioTextInputField(audioText): Write(audioText)
    @staticmethod
    def EnterAudioTextInputField(): PressAndRelease('enter')
    @staticmethod
    def WaitCaptchaVerification():
        while not IsImageOnScreen(Captcha.CaptchaVerification, 0.9):
            if IsExceptionOccured(): return False
        return True
    @staticmethod
    def IsCaptchaVerified():
        if IsImageOnScreen(Captcha.CaptchaVerification, 0.9):
            return True