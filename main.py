"""
TODO

1 - Menu inicial
2 - Escolher campeão filtrando pelo input do usuário

"""

import json
  
championsNames = json.load(open('champions.json'))

def main():
    print('')
    print('     FORCA LOL')
    print('     1 - Iniciar') # FUNÇÃO INCIAR JOGO
    print('     2 - Sair')    # SAIR DO PROGRAMA
    print('')

main()