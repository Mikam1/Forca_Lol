"""
TODO

1 - Menu inicial
2 - Escolher campeão filtrando pelo input do usuário

"""
import game  
import utils

def main():
    print('')
    print('         FORCA LOL')
    print('')
    print('     1 - Iniciar') # FUNÇÃO INCIAR JOGO
    print('     2 - Sair')    # SAIR DO PROGRAMA
    print('')

    option = int(input())
    match option:
        case 1:
            utils.clearConsole()
            return game.start()
        case 2:
            return 0
     

main()
