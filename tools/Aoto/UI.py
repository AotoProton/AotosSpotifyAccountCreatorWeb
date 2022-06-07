from colorama import Fore, Style

def InputBox():
    return Style.BRIGHT + Fore.CYAN + "[" + Fore.RED + ">" + Fore.CYAN + "]" + Style.RESET_ALL + Fore.RESET

def DisclaimerBox():
    return Style.BRIGHT + Fore.CYAN + "[" + Fore.RED + "!" + Fore.CYAN + "]" + Style.RESET_ALL + Fore.RESET

def NumberBox(number):
    return Style.BRIGHT + Fore.CYAN + "[" + Fore.RED + str(number) + Fore.CYAN + "]" + Style.RESET_ALL + Fore.RESET

def TextBox(text):
    return Style.BRIGHT + Fore.CYAN + "[" + Fore.RED + str(text) + Fore.CYAN + "]" + Style.RESET_ALL + Fore.RESET

def Space():
    return " "

def ResetAllColorsAndStyles():
    return Style.RESET_ALL + Fore.RESET

def Bright_Cyan():
    return Style.BRIGHT + Fore.CYAN

def Bright_Red():
    return Style.BRIGHT + Fore.RED

def Bright_Cyan_Text(text):
    return Style.BRIGHT + Fore.CYAN + text + Style.RESET_ALL + Fore.RESET

def Bright_Red_Text(text):
    return Style.BRIGHT + Fore.RED + text + Style.RESET_ALL + Fore.RESET
