import random
from time import sleep
import numpy

"""#### """
sorteio_emoj = list()
dados_jogo = list()
inicio_jogo = list()
# estrutura_final_jogo = list()

linha_aparencia = '--==--' * 15


def construcao_do_jogo():
    """
    Função responsável em construir toda a estrutura do jogo.

    :return:
    """

    lista_cobertura_ = (['              ', ' A', '   B', '   C', '   D', '   E'],
                        ['            1', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            2', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            3', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            4', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            5', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            6', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '])

    lista_emoj_signos = ['🐶', '🪁', '😈', '🧠', '💩',
                         '🤚', '👗', '🐬', '🐊', '🦉',
                         '🐧', '🌲', '🍕', '🍩', '🏠',
                         '🪐', '🌠', '🏐', '🎵', '🎼',
                         '💣', '🩸', '🧿', '☎', '🎤']

    random.shuffle(lista_emoj_signos)
    for i in range(0, 15):
        sorteio_emoj.append(lista_emoj_signos[i])

    for selecao_emoj in sorteio_emoj:
        dados_jogo.append(selecao_emoj)
        dados_jogo.append(selecao_emoj)
    random.shuffle(dados_jogo)
    print(dados_jogo)

    estrutura_final_jogo = numpy.array(dados_jogo)
    print(estrutura_final_jogo)

    return lista_cobertura_, dados_jogo
def leia_int(valor_entrada):
    """
    :param valor_entrada: Entra do valor da opção em menus
    :return: Se o valor for número inteiro, retorna para a opção escolhida
    """
    while True:
        try:
            valor_int = int(input(valor_entrada))
            return valor_int
        except:
            print(f'Opção INVALIDA!, Digite novamente')


def iniciando_jogo():
    posicao_escolha = 1
    valor_inicio, dados_sorteio = construcao_do_jogo()
    while True:
        # print(dados_sorteio)
        print(linha_aparencia)
        for linha in valor_inicio:
            print()
            for coluna in linha:
                print(coluna, end=' ')

        print()
        print(linha_aparencia)
        opc_posicao = input(f"Escolha a {posicao_escolha}º posição: ")


while True:

    print(f'\n{linha_aparencia}')
    print('''
            [1] Iniciar jogo
            [2] Ver pontuação
            [0] Sair
    ''')
    resp_opcao_menu = leia_int('Escolha uma OPÇÂO: ')

    if resp_opcao_menu == 1:
        iniciando_jogo()

    elif resp_opcao_menu == 2:
        pass

    elif resp_opcao_menu == 0:
        print('Fechando o Programa')
        sleep(1)
        break

    else:
        print('Essa opção não faz parte do menu!')
