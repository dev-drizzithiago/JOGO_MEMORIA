import random
from time import sleep

lista_cobertura_ = ['😄']
lista_emoj_signos = ['🕉️', '✡️', '☸️', '☯️', '✝️',
                     '☦️', '☪️', '☮️', '🕎', '🔯',
                     '🪯', '♈', '♉', '♊', '♋',
                     '♌', '♍', '♎', '♏', '♐',
                     '♑', '♒', '♓', '⛎', '🛐']


sorteio_emoj = random.choice(lista_emoj_signos)

for valor in sorteio_emoj:
    print(valor, end=' ')


def leia_int(valor_entrada):
    while True:
        try:
            valor_int = int(input(valor_entrada))
            return valor_int
        except:
            print(f'Opção INVALIDA!, Digite novamente')

def inicio_jogo():
    pass


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
