from tools.Aoto.UI import NumberBox,\
    InputBox,\
    DisclaimerBox,\
    Bright_Cyan_Text,\
    Bright_Red,\
    ResetAllColorsAndStyles

def PrintProgramArt():
    title = Bright_Red() + """
         ╔════════════════════════════════════════════╗
           ╔═╗╔═╗╔═╗╔╦╗╦╔═╗╦ ╦  ╔═╗╔═╗╔═╗╔═╗╦ ╦╔╗╔╔╦╗
           ╚═╗╠═╝║ ║ ║ ║╠╣ ╚╦╝  ╠═╣║  ║  ║ ║║ ║║║║ ║
           ╚═╝╩  ╚═╝ ╩ ╩╚   ╩   ╩ ╩╚═╝╚═╝╚═╝╚═╝╝╚╝ ╩
              ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗   ╦ ╦ ╦╔═╗╦═╗
              ║  ╠╦╝║╣ ╠═╣ ║ ║ ║╠╦╝   ║ ║ ║║╣ ║║╣
              ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝╩╚═   ╚═╩═╝╚═╝╩═╝
         ╚════════════════════════════════════════════╝
    """ + ResetAllColorsAndStyles()
    print(title)

def InputAccountAmount():
    return int(input(InputBox() + " " + Bright_Cyan_Text("Amount[0 For Unlimited]: ") + Bright_Red()))

def InputUseEmailsFromFile():
    value = int(input(InputBox() + " " + NumberBox(0) + Bright_Cyan_Text("Create random emails ") +
                     NumberBox(1) + Bright_Cyan_Text("Use emails from file: ") + Bright_Red()))
    if value == 1: return True
    else: return False

def InputForQuit_OnAllAccountsCreated():
    return input(DisclaimerBox() + Bright_Cyan_Text("Accounts Successfully Created") + ResetAllColorsAndStyles())
