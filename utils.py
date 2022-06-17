import os

def clearConsole():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def consoleTemplate():
    print('             FORCA LOL')
    print('')