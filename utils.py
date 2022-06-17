import os

def clearConsole():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def consoleTemplate(content = ''):
    print('------------ FORCA LOL ------------\n')
    print(f'{content}\n')