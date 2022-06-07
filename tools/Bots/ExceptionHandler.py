from tools.Aoto.Locators import Spotify, VPN, Browsers, Captcha
from tools.Aoto.Automation import IsImageOnScreen

class Exceptions:
    @staticmethod
    def IsProtonVpnUpgradeMessagePopped():
        if IsImageOnScreen(VPN.ProtonVPN.App.UpgradeButton, 0.9): return True

    @staticmethod
    def IsEmailAlreadyConnected():
        if IsImageOnScreen(Spotify.Signup.EmailAlreadyConnectedError): return True
    @staticmethod
    def IsEmailInvalid():
        if IsImageOnScreen(Spotify.Signup.InvalidEmailError): return True
    @staticmethod
    def IsSpotifySignupVpnErrorOccured():
        if IsImageOnScreen(Spotify.Signup.ConnectedToVPNError): return True

    @staticmethod
    def IsFirefoxPageStopped():
        if IsImageOnScreen(Browsers.Firefox.PageStopped): return True
    @staticmethod
    def IsFirefoxForbiddenErrorOccured():
        if IsImageOnScreen(Browsers.Firefox.ForbiddenError): return True
    @staticmethod
    def IsFirefoxFindingSiteErrorOccured():
        if IsImageOnScreen(Browsers.Firefox.FindingSiteError): return True
    @staticmethod
    def IsFirefoxConnectionTimeoutErrorOccured():
        if IsImageOnScreen(Browsers.Firefox.ConnectionTimeoutError): return True
    @staticmethod
    def IsFirefoxConnectionProtocolErrorOccured():
        if IsImageOnScreen(Browsers.Firefox.ConnectionProtocolError): return True
    @staticmethod
    def IsFirefoxConnectionFailedErrorOccured():
        if IsImageOnScreen(Browsers.Firefox.ConnectionFailedError): return True
    @staticmethod
    def IsFirefoxUpstreamConnectionErrorOccured():
        if IsImageOnScreen(Browsers.Firefox.UpstreamConnectionError): return True

    @staticmethod
    def IsCaptchaConnectErrorOccured_FirstVersion():
        if IsImageOnScreen(Captcha.ConnectionErrorV1): return True
    @staticmethod
    def IsCaptchaConnectErrorOccured_SecondVersion():
        if IsImageOnScreen(Captcha.ConnectionErrorV2): return True
    @staticmethod
    def IsCaptchaServerConnectionErrorOccured():
        if IsImageOnScreen(Captcha.ServerConnectionError): return True
    @staticmethod
    def IsCaptchaContactErrorOccured():
        if IsImageOnScreen(Captcha.CannotContactToCaptchaError): return True
    @staticmethod
    def IsCaptchaConfirmErrorOccured():
        if IsImageOnScreen(Captcha.ConfirmError): return True
    @staticmethod
    def IsCaptchaSolveMoreErrorOccured():
        if IsImageOnScreen(Captcha.SolveMoreError): return True
    @staticmethod
    def IsCaptchaExpired():
        if IsImageOnScreen(Captcha.Expired): return True
    @staticmethod
    def OnAutomatedQueriesErrorOccured():
        if IsImageOnScreen(Captcha.AutomatedQueriesError):
            input("Automated Queries!")
def IsExceptionOccured():
    if Exceptions.IsProtonVpnUpgradeMessagePopped(): return True
    if Exceptions.IsEmailAlreadyConnected(): return True
    if Exceptions.IsEmailInvalid(): return True
    if Exceptions.IsSpotifySignupVpnErrorOccured(): return True
    if Exceptions.IsFirefoxPageStopped(): return True
    if Exceptions.IsFirefoxForbiddenErrorOccured(): return True
    if Exceptions.IsFirefoxFindingSiteErrorOccured(): return True
    if Exceptions.IsFirefoxConnectionTimeoutErrorOccured(): return True
    if Exceptions.IsFirefoxConnectionProtocolErrorOccured(): return True
    if Exceptions.IsFirefoxConnectionFailedErrorOccured(): return True
    if Exceptions.IsFirefoxUpstreamConnectionErrorOccured(): return True
    if Exceptions.IsCaptchaConnectErrorOccured_FirstVersion(): return True
    if Exceptions.IsCaptchaConnectErrorOccured_SecondVersion(): return True
    if Exceptions.IsCaptchaServerConnectionErrorOccured(): return True
    if Exceptions.IsCaptchaContactErrorOccured(): return True
    if Exceptions.IsCaptchaConfirmErrorOccured(): return True
    if Exceptions.IsCaptchaSolveMoreErrorOccured(): return True
    if Exceptions.IsCaptchaExpired(): return True
    Exceptions.OnAutomatedQueriesErrorOccured()