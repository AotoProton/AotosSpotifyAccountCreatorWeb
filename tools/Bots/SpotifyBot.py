from tools.Aoto.Automation import Wait,\
    Write,\
    Scroll,\
    IsImageOnScreen,\
    WaitWhile_ImageNotOnScreen,\
    IfImageOn_MoveImmediateDoubleClickBreak,\
    WhileImageOn_MoveImmediateClickBreak
from tools.Aoto.Locators import Spotify
from tools.Bots.ExceptionHandler import IsExceptionOccured

def TryToFindSpotifySignupPage(tries=25):
    for _ in range(tries):
        if IsImageOnScreen(Spotify.Signup.Icon): return True
        if IsExceptionOccured(): return False
        Wait(0.5,1)
def TryToFindAcceptCookies(tries=20):
    for _ in range(tries):
        if IsImageOnScreen(Spotify.Signup.AcceptCookiesV1): return True
        if IsImageOnScreen(Spotify.Signup.AcceptCookiesV2): return True
        Wait(0.5,1)
def ClickAcceptCookies():
    IfImageOn_MoveImmediateDoubleClickBreak(Spotify.Signup.AcceptCookiesV1)
    IfImageOn_MoveImmediateDoubleClickBreak(Spotify.Signup.AcceptCookiesV2)

def FindEmailInputField():
    while not IsImageOnScreen(Spotify.Signup.EmailInputField):
        if IsExceptionOccured(): return False
    return True
def ClickEmailInputField(): WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.EmailInputField), Wait(0.01, 0.03)
def WriteEmailInputField(email): Write(email, 0.01, 0.03), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)

def FindEmailConfirmationInputField():
    while not IsImageOnScreen(Spotify.Signup.EmailConfirmationInputField):
        if IsExceptionOccured(): return False
    return True
def ClickEmailConfirmationInputField():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.EmailConfirmationInputField), Wait(0.01, 0.03)
def WriteEmailConfirmationInputField(email): Write(email, 0.01, 0.03), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)

def FindPasswordInputField():
    while not IsImageOnScreen(Spotify.Signup.PasswordInputField):
        if IsExceptionOccured(): return False
    return True
def ClickPasswordInputField():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.PasswordInputField), Wait(0.01, 0.03)
def WritePasswordInputField(password): Write(password, 0.01, 0.03), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)

def FindDisplaynameInputField():
    while not IsImageOnScreen(Spotify.Signup.DisplayInputField):
        if IsExceptionOccured(): return False
    return True
def ClickDisplaynameInputField():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.DisplayInputField), Wait(0.01, 0.03)
def WriteDisplaynameInputField(displayname): Write(displayname, 0.01, 0.03),\
                                             Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)

def FindDayInputField():
    while not IsImageOnScreen(Spotify.Signup.DayInputField):
        if IsExceptionOccured(): return False
    return True
def ClickDayInputField(): WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.DayInputField), Wait(0.01, 0.03)
def WriteDayInputField(day): Write(day, 0.01, 0.03)

def IsMonthSelected():
    if not IsImageOnScreen(Spotify.Signup.MonthsDropdown, 0.9): return True
def FindMonthsDropdown(): WaitWhile_ImageNotOnScreen(Spotify.Signup.MonthsDropdown, 0.9)
def ClickMonthsDropdown():
    if not IsImageOnScreen(Spotify.Signup.January):
        WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.MonthsDropdown, 0.9)
        Wait(0.5, 1)
def FindJanuary(): WaitWhile_ImageNotOnScreen(Spotify.Signup.January)
def ClickJanuary():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.January), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindFebruary(): WaitWhile_ImageNotOnScreen(Spotify.Signup.February)
def ClickFebruary():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.February), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindMarch(): WaitWhile_ImageNotOnScreen(Spotify.Signup.March, 0.9)
def ClickMarch():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.March, 0.9), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindApril(): WaitWhile_ImageNotOnScreen(Spotify.Signup.April)
def ClickApril():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.April), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindMay(): WaitWhile_ImageNotOnScreen(Spotify.Signup.May)
def ClickMay():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.May), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindJune(): WaitWhile_ImageNotOnScreen(Spotify.Signup.June)
def ClickJune():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.June), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindJuly(): WaitWhile_ImageNotOnScreen(Spotify.Signup.July)
def ClickJuly():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.July), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindAugust(): WaitWhile_ImageNotOnScreen(Spotify.Signup.August)
def ClickAugust():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.August), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindSeptember(): WaitWhile_ImageNotOnScreen(Spotify.Signup.September)
def ClickSeptember():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.September), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindOctober(): WaitWhile_ImageNotOnScreen(Spotify.Signup.October)
def ClickOctober():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.October), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindNovember(): WaitWhile_ImageNotOnScreen(Spotify.Signup.November)
def ClickNovember():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.November), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)
def FindDecember(): WaitWhile_ImageNotOnScreen(Spotify.Signup.December, 0.9)
def ClickDecember():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.December, 0.9), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)

def FindYearInputField():
    while not IsImageOnScreen(Spotify.Signup.YearInputField):
        if IsExceptionOccured(): return False
    return True
def ClickYearInputField():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.YearInputField), Wait(0.01, 0.03)
def WriteYearInputField(year): Write(year, 0.01, 0.03), Wait(0.1, 0.3), Scroll(-200), Wait(0.01, 0.03)

def FindMaleButton(): WaitWhile_ImageNotOnScreen(Spotify.Signup.MaleButton)
def ClickMaleButton():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.MaleButton), Wait(0.01, 0.03), Scroll(-200)
def FindFemaleButton(): WaitWhile_ImageNotOnScreen(Spotify.Signup.FemaleButton)
def ClickFemaleButton():
    WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.FemaleButton), Wait(0.01, 0.03), Scroll(-200)

def DisableEmailNotifications():
    if IsImageOnScreen(Spotify.Signup.DisableEmailNotificationSelect):
        IfImageOn_MoveImmediateDoubleClickBreak(Spotify.Signup.DisableEmailNotificationSelect)

def FindSignupButton():
    while not IsImageOnScreen(Spotify.Signup.SignUpBtn):
        Scroll(-400)
def ClickSignupButton(): WhileImageOn_MoveImmediateClickBreak(Spotify.Signup.SignUpBtn)

def WaitUntilSignedUp():
    while not IsImageOnScreen(Spotify.Signup.SignedUpCheck) and not IsImageOnScreen(Spotify.Signup.SignedUpCheck2):
        Wait(2, 4)
        if IsExceptionOccured(): return False
        if not IsImageOnScreen(Spotify.Signup.SignUpBtn): Scroll(-200)
        ClickSignupButton()
        Wait(2, 4)
    return True
