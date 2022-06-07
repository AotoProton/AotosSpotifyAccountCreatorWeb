import names
from random_username import generate
from string import ascii_letters, digits
from random import randint, choice

def FindFirstUpperCaseIndex(text):
    for letter in text:
        if str.isupper(letter):
            return text.index(letter)

def RemoveRandomlyGeneratedLastNumberFromUserName(text): return text[0: len(text) - 1]

def GetRandomDisplayname(gender):
    displayname = ""
    useRealnames = choice([True, False])
    if useRealnames:
        idAddingType = choice(["None", "Start", "Middle", "End",
                               "StartAndMiddle", "MiddleAndEnd", "EndAndStart",
                               "StartAndMiddleAndEnd"])
        if idAddingType == "None": displayname += names.get_first_name(gender=gender) + names.get_last_name()
        if idAddingType == "Start":
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += names.get_first_name(gender=gender) + names.get_last_name()
        if idAddingType == "Middle":
            idAmount = randint(1, 4)
            displayname += names.get_first_name(gender=gender)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += names.get_last_name()
        if idAddingType == "End":
            idAmount = randint(1, 4)
            displayname += names.get_first_name(gender=gender) + names.get_last_name()
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
        if idAddingType == "StartAndMiddle":
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += names.get_first_name(gender=gender)
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += names.get_last_name()
        if idAddingType == "MiddleAndEnd":
            displayname += names.get_first_name(gender=gender)
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += names.get_last_name()
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
        if idAddingType == "EndAndStart":
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += names.get_first_name(gender=gender)
            displayname += names.get_last_name()
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
        if idAddingType == "StartAndMiddleAndEnd":
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += names.get_first_name(gender=gender)
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += names.get_last_name()
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
    if not useRealnames:
        displayname = generate.generate_username(1)[0]
        displayname = RemoveRandomlyGeneratedLastNumberFromUserName(displayname)
        firstUpperCase = FindFirstUpperCaseIndex(displayname)
        firstPart = displayname[0: firstUpperCase]
        secondPart = displayname[firstUpperCase: len(displayname)]
        displayname = ""
        idAddingType = choice(["None", "Start", "Middle", "End",
                               "StartAndMiddle", "MiddleAndEnd", "EndAndStart",
                               "StartAndMiddleAndEnd"])
        if idAddingType == "None": displayname += firstPart + secondPart
        if idAddingType == "Start":
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += firstPart + secondPart
        if idAddingType == "Middle":
            idAmount = randint(1, 4)
            displayname += firstPart
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += secondPart
        if idAddingType == "End":
            idAmount = randint(1, 4)
            displayname += firstPart + secondPart
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
        if idAddingType == "StartAndMiddle":
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += firstPart
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += secondPart
        if idAddingType == "MiddleAndEnd":
            displayname += firstPart
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += secondPart
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
        if idAddingType == "EndAndStart":
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += firstPart
            displayname += secondPart
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
        if idAddingType == "StartAndMiddleAndEnd":
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += firstPart
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
            displayname += secondPart
            idAmount = randint(1, 4)
            for _ in range(idAmount):
                displayname += str(randint(0, 9))
    return displayname

def GetRandomGender():
    gender = choice(['male', 'female']),
    gender = str(gender)
    gender = gender[2:len(gender)]
    gender = gender[0: len(gender) - 3]
    return gender

def GetRandomDomain():
    return choice(["@gmail.com", "@gmail.com", "@gmail.com", "@yahoo.com", "@hotmail.com", "@gmail.com",])

def GetRandomEmail(displayname):
    email = displayname + GetRandomDomain()
    return email

def GetLowerCasedRandomPassword():
    password_characters = ascii_letters + digits
    password_characters = ''.join(choice(password_characters) for _ in range(randint(10, 15)))
    password = password_characters.lower()
    return password

def GetRandomBirthDay():
    return str(randint(1, 28))

def GetRandomBirthMonth():
    return str(randint(1, 12))

def GetRandomBirthYear():
    return str(randint(1970, 2005))

def GetAuthenticCredentials():
    gender = GetRandomGender()
    displayname = GetRandomDisplayname(gender)
    email = GetRandomEmail(displayname)
    credentials = {
        'displayname': displayname,
        'email': email,
        'password': GetLowerCasedRandomPassword(),
        'gender': gender,
        'birth_day': GetRandomBirthDay(),
        'birth_month': GetRandomBirthMonth(),
        'birth_year': GetRandomBirthYear(),
        }
    return credentials