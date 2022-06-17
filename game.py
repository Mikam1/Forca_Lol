import json
import utils

championsNames = json.load(open('champions.json'))

def start():
    inputName = ""

    filteredNames = championsNames[:5]

    utils.consoleTemplate(getNamesTemplate(filteredNames))

    while(True):
        inputName = input("Digite o nome do campeão: ")
        utils.clearConsole()

        if inputName.isnumeric() and int(inputName) > -1 and int(inputName) < 6: 
            break

        filteredNames = list(filter(lambda champName: inputName.lower() in champName.lower(), championsNames))

        utils.consoleTemplate(getNamesTemplate(filteredNames))
        print(f"Nome pesquisado: {inputName}")
        

    print('Campeão escolhido: ', filteredNames[int(inputName)])

def getNamesTemplate(names):
    message = ''

    if len(names) == 0:
        return 'Nenhum campeão encontrado'

    for idx, name in enumerate(names[:5]):
            message += f"{idx} - {name}\n"

    return message