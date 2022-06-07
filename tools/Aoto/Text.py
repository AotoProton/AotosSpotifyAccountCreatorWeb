def ClearLine():
    i = 0
    for i in range(256):
        print(end='\b', flush=True)
        print(end=' ', flush=True)
        print(end='\b', flush=True)

def Newline():
    print(' ')
    print(end='')
    print(end='', flush=True)

def PrintTextOverlap(text):
    ClearLine()
    print(end=text)
    print(end='', flush=True)