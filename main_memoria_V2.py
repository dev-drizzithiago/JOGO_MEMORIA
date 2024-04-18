import random
from time import sleep

lista_de_emojes = []


def leia_int(valor):
    while True:
        try:
            valor_int = int(input(valor))
            return valor_int
        except:
            print(f'Opção INVALIDA!, Digite novamente')


while True:
    print('''
            [1] Iniciar jogo
            [2] Ver pontuação
            [0] Sair
    ''')
    resp_opcao_menu = leia_int('Escolha uma OPÇÂO: ')
    if resp_opcao_menu == 1:
        pass
    elif resp_opcao_menu == 2:
        pass
    elif resp_opcao_menu == 0:
        print('Fechando o Programa')
        sleep(1)
        break
    else:
        print('Essa opção não faz parte do menu!')
