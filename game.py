import json


import utils

championsNames = json.load(open('champions.json'))

def start():
    print("Selecione o nome do campeão")

    inputName = ""

    filteredNames = championsNames[:5]
    utils.consoleTemplate()
    printNames(filteredNames)

    while(True):
        print()
        inputName = input("Digite o nome do campeão: ")
        utils.clearConsole()


        if inputName.isnumeric(): 
            break

        filteredNames = list(filter(lambda champName: inputName.lower() in champName.lower(), championsNames))

        utils.consoleTemplate()
        printNames(filteredNames)

    print('Campeão escolhido: ', filteredNames[int(inputName)])

def printNames(names):
    for idx, name in enumerate(names[:5]):
            print(f"{idx} - {name}")