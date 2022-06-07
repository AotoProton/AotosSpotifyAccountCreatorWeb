from tools.Aoto.Automation import Wait
from tools.Aoto.UI import TextBox, Space, Bright_Red_Text
from tools.BaseFunctions import SetTitle,\
    Readlines_FromEmailsToUseFile_ThenClose,\
    Remove_FirstItemOfList,\
    TruncateAndWriteLines_ToEmailsToUseFile_ThenClose,\
    IfSpacePressed_PauseAccountCreation, \
    CreateSaveFile, SaveToFile,\
    CreatedAccountInformation,\
    RemoveDownloadedMp3,\
    RemoveConvertedWav
from tools.Input import PrintProgramArt,\
    InputAccountAmount,\
    InputUseEmailsFromFile,\
    InputForQuit_OnAllAccountsCreated
from tools.Bots.SpotifyBot import TryToFindSpotifySignupPage,\
    FindMonthsDropdown, ClickMonthsDropdown,\
    DisableEmailNotifications,\
    FindSignupButton, ClickSignupButton,\
    WaitUntilSignedUp, \
    IsMonthSelected,\
    FindJanuary, \
    ClickJanuary, \
    FindFebruary, \
    ClickFebruary, \
    FindMarch, \
    ClickMarch, \
    FindApril, \
    ClickApril, \
    FindMay, \
    ClickMay, \
    FindJune, \
    ClickJune, \
    FindJuly, \
    ClickJuly, \
    FindAugust, \
    ClickAugust, \
    FindSeptember, \
    ClickSeptember, \
    FindOctober, \
    ClickOctober, \
    FindNovember, \
    ClickNovember, \
    FindDecember, \
    ClickDecember, \
    FindMaleButton, \
    ClickMaleButton, \
    FindFemaleButton, \
    ClickFemaleButton, \
    TryToFindAcceptCookies, ClickAcceptCookies,\
    FindEmailInputField, ClickEmailInputField, WriteEmailInputField,\
    FindEmailConfirmationInputField, ClickEmailConfirmationInputField, WriteEmailConfirmationInputField,\
    FindPasswordInputField, ClickPasswordInputField, WritePasswordInputField,\
    FindDisplaynameInputField, ClickDisplaynameInputField, WriteDisplaynameInputField,\
    FindDayInputField, ClickDayInputField, WriteDayInputField,\
    FindYearInputField, ClickYearInputField, WriteYearInputField
from tools.Bots.CaptchaBot import SolveCaptcha
from tools.Aoto.Credentials import GetAuthenticCredentials
from tools.Aoto.Text import Newline
from tools.Aoto.Timer import StartTimer, EndTimer, TimeTaken
from tools.Bots.FirefoxBot import OpenFirefox, FindFirefoxSearch, ClickFirefoxSearch, FirefoxSearch,\
    TerminateFirefox, ClearFirefoxCache
from tools.Bots.ProtonVpnBot import OpenProtonVpn,\
    FindProtonVpnQuickConnect, ClickProtonVpnQuickConnect,\
    FindProtonVpnQuickDisconnect, ClickProtonVpnQuickDisconnect,\
    FindProtonVpnStatusConnected,\
    FindProtonVpnIcon, ClickProtonVpnIcon,\
    TerminateProtonVpn,\
    IsProtonVpnUpgradeMessagePopped,\
    IsProtonVpnConnected, IsProtonVpnDisconnected

class Main:
    def OnAccountCreated(self, credentials):
        TerminateFirefox()
        self.createdAccounts += 1
        if self.useEmailsFromFile:
            Remove_FirstItemOfList(self.emailsToUse)
            TruncateAndWriteLines_ToEmailsToUseFile_ThenClose(self.emailsToUse)
        SetTitle("Aoto's Spotify Account Bot Web - Created: " +
            str(self.createdAccounts) + "/" + str(self.totalAccountAmountToCreate) +
            " Errors:" + str(self.errorCount))
        CreateSaveFile(), SaveToFile(credentials=credentials)
        EndTimer()
        CreatedAccountInformation(credentials=credentials, timeTaken=TimeTaken())
        Newline()

    def OnExceptionOccured(self):
        self.errorCount += 1
        SetTitle("Aoto's Spotify Account Bot Web - Created: " +
            str(self.createdAccounts) + "/" + str(self.totalAccountAmountToCreate) +
            " Errors:" + str(self.errorCount))
        self.AccountCreator()

    def __init__(self):
        SetTitle("Aoto's Spotify Account Creator Web")
        self.spotifySignUpPageUrl = "https://www.spotify.com/us/signup"
        self.createdAccounts = 0
        self.errorCount = 0
        self.emailsToUse = Readlines_FromEmailsToUseFile_ThenClose()
        PrintProgramArt()
        self.totalAccountAmountToCreate = InputAccountAmount()
        self.useEmailsFromFile = InputUseEmailsFromFile()
        if self.useEmailsFromFile and self.totalAccountAmountToCreate > len(self.emailsToUse):
            self.totalAccountAmountToCreate = len(self.emailsToUse)
        Newline()
        self.AccountCreator()
        Newline()
        InputForQuit_OnAllAccountsCreated()

    def AccountCreator(self):
        while self.createdAccounts < self.totalAccountAmountToCreate or self.totalAccountAmountToCreate == 0:
            try:
                IfSpacePressed_PauseAccountCreation()
                credentials = GetAuthenticCredentials()
                StartTimer()
                ClearFirefoxCache(), RemoveDownloadedMp3(), RemoveConvertedWav()
                OpenProtonVpn(), FindProtonVpnIcon(), ClickProtonVpnIcon()
                while not IsProtonVpnUpgradeMessagePopped():
                    if IsProtonVpnConnected():
                        FindProtonVpnQuickDisconnect(), ClickProtonVpnQuickDisconnect()
                        FindProtonVpnQuickConnect(), ClickProtonVpnQuickConnect()
                        Wait(2, 3)
                        FindProtonVpnStatusConnected()
                        break
                    if IsProtonVpnDisconnected():
                        FindProtonVpnQuickConnect(), ClickProtonVpnQuickConnect()
                        Wait(2, 3)
                        FindProtonVpnStatusConnected()
                        break
                if IsProtonVpnUpgradeMessagePopped():
                    TerminateProtonVpn()
                    self.errorCount += 1
                    SetTitle("Aoto's Spotify Account Bot Web - Created: " +
                        str(self.createdAccounts) + "/" + str(self.totalAccountAmountToCreate) +
                        " Errors:" + str(self.errorCount))
                    self.AccountCreator()
                OpenFirefox(), FindFirefoxSearch(), ClickFirefoxSearch(), FirefoxSearch(self.spotifySignUpPageUrl)
                if not TryToFindSpotifySignupPage(): self.OnExceptionOccured()
                if not TryToFindAcceptCookies(): self.OnExceptionOccured()
                ClickAcceptCookies()
                if not self.useEmailsFromFile:
                    if not FindEmailInputField(): self.OnExceptionOccured()
                    ClickEmailInputField()
                    WriteEmailInputField(credentials['email'])
                    if not FindEmailConfirmationInputField(): self.OnExceptionOccured()
                    ClickEmailConfirmationInputField()
                    WriteEmailConfirmationInputField(credentials['email'])
                if self.useEmailsFromFile:
                    if not FindEmailInputField(): self.OnExceptionOccured()
                    ClickEmailInputField()
                    WriteEmailInputField(self.emailsToUse[0])
                    if not FindEmailConfirmationInputField():
                        self.errorCount += 1
                        SetTitle("Aoto's Spotify Account Bot Web - Created: " +
                                 str(self.createdAccounts) + "/" + str(self.totalAccountAmountToCreate) +
                                 " Errors:" + str(self.errorCount))
                        self.AccountCreator()
                    ClickEmailConfirmationInputField()
                    WriteEmailConfirmationInputField(credentials['email'])
                if not FindPasswordInputField(): self.OnExceptionOccured()
                ClickPasswordInputField()
                WritePasswordInputField(credentials['password'])
                if not FindDisplaynameInputField(): self.OnExceptionOccured()
                ClickDisplaynameInputField()
                WriteDisplaynameInputField(credentials['displayname'])
                if not FindDayInputField(): self.OnExceptionOccured()
                ClickDayInputField()
                WriteDayInputField(credentials['birth_day'])
                while not IsMonthSelected():
                    FindMonthsDropdown(), ClickMonthsDropdown()
                    if credentials['birth_month'] == "1": FindJanuary(), ClickJanuary()
                    if credentials['birth_month'] == "2": FindFebruary(), ClickFebruary()
                    if credentials['birth_month'] == "3": FindMarch(), ClickMarch()
                    if credentials['birth_month'] == "4": FindApril(), ClickApril()
                    if credentials['birth_month'] == "5": FindMay(), ClickMay()
                    if credentials['birth_month'] == "6": FindJune(), ClickJune()
                    if credentials['birth_month'] == "7": FindJuly(), ClickJuly()
                    if credentials['birth_month'] == "8": FindAugust(), ClickAugust()
                    if credentials['birth_month'] == "9": FindSeptember(), ClickSeptember()
                    if credentials['birth_month'] == "10": FindOctober(), ClickOctober()
                    if credentials['birth_month'] == "11": FindNovember(), ClickNovember()
                    if credentials['birth_month'] == "12": FindDecember(), ClickDecember()
                if not FindYearInputField(): self.OnExceptionOccured()
                ClickYearInputField()
                WriteYearInputField(credentials['birth_year'])
                if credentials['gender'] == 'male': FindMaleButton(), ClickMaleButton()
                if credentials['gender'] == 'female': FindFemaleButton(), ClickFemaleButton()
                DisableEmailNotifications()
                try:
                    if not SolveCaptcha.Initialize(): self.OnExceptionOccured()
                except: self.OnExceptionOccured()
                FindSignupButton(), ClickSignupButton()
                if not WaitUntilSignedUp(): self.OnExceptionOccured()
                self.OnAccountCreated(credentials=credentials)
            except:
                print(TextBox("ERROR") + Space() + Bright_Red_Text("Retrying!"))
                self.errorCount += 1
                SetTitle("Aoto's Spotify Account Bot Web - Created: " +
                    str(self.createdAccounts) + "/" + str(self.totalAccountAmountToCreate) +
                    " Errors:" + str(self.errorCount))
                self.AccountCreator()

if __name__ == '__main__': main = Main()