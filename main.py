"""
TODO

1 - Menu inicial
2 - Escolher campeão filtrando pelo input do usuário

"""
import game  
import utils

def main():
    utils.clearConsole()
    menuTemplate = "1 - Iniciar\n2 - Sair\n"

    utils.consoleTemplate(menuTemplate)

    option = int(input())
    match option:
        case 1:
            utils.clearConsole()
            return game.start()
        case 2:
            return 0
     

main()
