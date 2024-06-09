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

    """### Essa estrutura sera responsável em apresentar ao usuário o mode de inicio"""
    lista_cobertura_ = [['              ', ' A', '   B', '   C', '   D', '   E'],
                        ['            1', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            2', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            3', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            4', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            5', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['            6', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ']]

    """### Possui os icones do jogo. Possui 30 itens ao todo"""
    lista_emoj_signos = numpy.array(['🐶', '🪁', '😈', '🧠', '💩',
                                     '🤚', '👗', '🐬', '🐊', '🦉',
                                     '🐧', '🌲', '🍕', '🍩', '🏠',
                                     '🪐', '🌠', '🏐', '🎵', '🎼',
                                     '💣', '🩸', '🧿', '☎', '🎤'])
    """### Embaralha todos os icones para que sejam sorteados para o jogo"""
    random.shuffle(lista_emoj_signos)

    """### Escolhe 15 icones iniciais da lista de emojis"""
    for i in range(0, 15):
        sorteio_emoj.append(lista_emoj_signos[i])

    """### Pega os icones escolhidos e faz uma copia"""
    del dados_jogo[:]
    for selecao_emoj in sorteio_emoj:
        dados_jogo.append(selecao_emoj)
        dados_jogo.append(selecao_emoj)

    """### Com os icones em pares, é realizado mais um embaralhamento, para que os icones fiquem dispersos."""
    random.shuffle(dados_jogo)

    """### Como esta em uma única lista, é preciso transformar uma matrix, com 6 linhas e 5 colunas"""
    estrutura_final_jogo = numpy.array(dados_jogo)
    estrutura_final_jogo = estrutura_final_jogo.reshape(6, 5)

    """### Retorna a matriz para o inicio do jogo"""
    return lista_cobertura_, estrutura_final_jogo


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
    matriz_jogo = int
    posicao_escolha = 1
    estrutura, dados_sorteio = construcao_do_jogo()

    while True:
        print(linha_aparencia)
        for linha in estrutura:
            print()
            for coluna in linha:
                print(coluna, end=' ')

        if posicao_escolha == 1:
            print()
            print(linha_aparencia)
            opc_posicao_1 = input(f"Escolha a {posicao_escolha}º posição(voltar=999): ").upper()
            posicao_escolha += 1
        else:
            print()
            print(linha_aparencia)
            opc_posicao_2 = input(f"Escolha a {posicao_escolha}º posição(voltar=999): ")
            posicao_escolha -= 1

        if opc_posicao_1[0] == "A":
            opc_posicao_1 = int(1)
            estrutura = int (opc_posicao_1 + opc_posicao_1[1])
        elif opc_posicao_1[0] == "B":
            pass
        elif opc_posicao_1[0] == "C":
            pass
        elif opc_posicao_1[0] == "D":
            pass
        elif opc_posicao_1[0] == "E":
            pass
        elif opc_posicao_1 == '999':
            resp = input("Tem certeza que desaja sair? Vai perder todo o progresso (S/N): ").upper()
            if resp[0] == 'S':
                del valor_inicio[:]
                del sorteio_emoj[:]
                print('Saindo do jogo!')
                break
            else:
                print('Voltando ao jogo!')
        else:
            print('Essa opção não existe')



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
