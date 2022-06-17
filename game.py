import json


import utils

championsNames = json.load(open('champions.json'))

def start():
    print("Selecione o nome do campeão")
    print(championsNames[:5])

    inputName = ""

    filteredNames = []

    while(True):
        print()
        inputName = input("Digite o nome do campeão: ")
        utils.clearConsole()


        if inputName.isnumeric(): 
            break

        filteredNames = list(filter(lambda champName: inputName.lower() in champName.lower(), championsNames))

        utils.consoleTemplate()
        print(filteredNames[:5])

    print('Campeão escolhido: ', filteredNames[int(inputName)])
