import random
import numpy
from os import mkdir
from time import sleep
from pathlib import Path



"""#### Declaração de variáveis"""
sorteio_emoj, dados_jogo, inicio_jogo = list(), list(), list()

pasta_home = Path.home()
local_arq_pontuacao = (pasta_home, 'AppData', 'LocalLow')
arq_pontuacao = 'Pontuação Geral.txt'
arq_save_pontos = f'{local_arq_pontuacao}\\{arq_pontuacao}'

linha_aparencia = '--==--' * 15

def construcao_do_jogo():
    """
    Função responsável em construir toda a estrutura do jogo.
    :return:
    """

    """### Essa estrutura sera responsável em apresentar ao usuário o mode de inicio"""
    lista_cobertura_ = [['                   ', ' A', '   B', '   C', '   D', '   E'],
                        ['                 1', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['                 2', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['                 3', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['                 4', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['                 5', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 '],
                        ['                 6', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ', ' 😄 ']]

    """### Possui os icones do jogo. Possui 30 itens ao todo"""
    lista_emoj_signos = numpy.array([' 🐶 ', ' 🪁 ', ' 😈 ', ' 🧠 ', ' 💩 ',
                                     ' 🤚 ', ' 👗 ', ' 🐬 ', ' 🐊 ', ' 🦉 ',
                                     ' 🐧 ', ' 🌲 ', ' 🍕 ', ' 🍩 ', ' 🏠 ',
                                     ' 🪐 ', ' 🌠 ', ' 🏐 ', ' 🎵 ', ' 🎼 ',
                                     ' 💣 ', ' 🩸 ', ' 🧿 ', ' ☎ ', ' 🎤 '])

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
    linha_a, coluna_a, linha_b, coluna_b = 0, 0, 0, 0
    ponto_partida, ponto_final = 0, 0

    jogada = 1
    resposta_1, resposta_2 = '', ''
    estrutura, dados_sorteio = construcao_do_jogo()

    """### Estrutura inicial"""
    print(linha_aparencia)
    for linha in estrutura:
        print()
        for coluna in linha:
            print(coluna, end=' ')

    while True:

        #  Escolhendo a primeiro opção
        if jogada == 1:
            while True:
                print()
                print(linha_aparencia)
                opc_posicao_1 = input(f"Escolha a {jogada}º posição(voltar=999): ").upper()

                if len(opc_posicao_1) == 0:
                    print('Escolha uma coluna (Letras) e uma linha (Números)')
                elif len(opc_posicao_1[0]) < 1 and int(opc_posicao_1[1]) > 6:
                    print('Opção inccorreta')
                else:
                    break
        #  A segunda opção vai ser escolhida
        elif jogada == 2:
            while True:
                print()
                print(linha_aparencia)
                opc_posicao_2 = input(f"Escolha a {jogada}º posição(voltar=999): ").upper()

                if len(opc_posicao_1) == 0:
                    print('Escolha uma coluna (Letras) e uma linha (Números)')
                elif len(opc_posicao_2[0]) < 1 and int(opc_posicao_2[1]) > 6:
                    print('Opção inccorreta1')
                else:
                    break

        if jogada == 1:
            if opc_posicao_1[0] == "A":  # Letras são considerados COLUNAS
                linha_a = int(opc_posicao_1[1])  # Número chega como string sendo convertidas para inteiro
                coluna_a = 1  # As letras são modificados por números reais
                resposta_1 = dados_sorteio[linha_a - 1][coluna_a - 1]

            elif opc_posicao_1[0] == "B":  # Letras são considerados COLUNAS
                linha_a = int(opc_posicao_1[1])  # Número chega como string sendo convertidas para inteiro
                coluna_a = 2  # As letras são modificados por números reais
                resposta_1 = dados_sorteio[linha_a - 1][coluna_a - 1]

            elif opc_posicao_1[0] == "C":  # Letras são considerados COLUNAS
                linha_a = int(opc_posicao_1[1])  # Número chega como string sendo convertidas para inteiro
                coluna_a = 3  # As letras são modificados por números reais
                resposta_1 = dados_sorteio[linha_a - 1][coluna_a - 1]

            elif opc_posicao_1[0] == "D":  # Letras são considerados COLUNAS
                linha_a = int(opc_posicao_1[1])  # Número chega como string sendo convertidas para inteiro
                coluna_a = 4  # As letras são modificados por números reais
                resposta_1 = dados_sorteio[linha_a - 1][coluna_a - 1]

            elif opc_posicao_1[0] == "E":  # Letras são considerados COLUNAS
                linha_a = int(opc_posicao_1[1])  # Número chega como string sendo convertidas para inteiro
                coluna_a = 5  # As letras são modificados por números reais
                resposta_1 = dados_sorteio[linha_a - 1][coluna_a - 1]

            elif opc_posicao_1 == '999':
                resp = input("Tem certeza que desaja sair? Vai perder todo o progresso (S/N): ").upper()
                if resp[0] == 'S':
                    del estrutura[:]  # As listas são limpas quando sair do jogo
                    del sorteio_emoj[:]  # As listas são limpas quando sair do jogo
                    print('Saindo do jogo!')
                    break  # Quebra o loop
                else:
                    print('Voltando ao jogo!')
            else:
                print('Opção não existe!')

        elif jogada == 2:

            if opc_posicao_2[0] == "A":  # Letras são considerados COLUNAS
                linha_b = int(opc_posicao_2[1])
                coluna_b = 1  # As letras são modificados por números reais
                resposta_2 = dados_sorteio[linha_b - 1][coluna_b - 1]

            elif opc_posicao_2[0] == "B":  # Letras são considerados COLUNAS
                linha_b = int(opc_posicao_2[1])  # Número chega como string sendo convertidas para inteiro
                coluna_b = 2  # As letras são modificados por números reais
                resposta_2 = dados_sorteio[linha_b - 1][coluna_b - 1]

            elif opc_posicao_2[0] == "C":  # Letras são considerados COLUNAS
                linha_b = int(opc_posicao_2[1])  # Número chega como string sendo convertidas para inteiro
                coluna_b = 3  # As letras são modificados por números reais
                resposta_2 = dados_sorteio[linha_b - 1][coluna_b - 1]

            elif opc_posicao_2[0] == "D":  # Letras são considerados COLUNAS
                linha_b = int(opc_posicao_2[1])  # Número chega como string sendo convertidas para inteiro
                coluna_b = 4  # As letras são modificados por números reais
                resposta_2 = dados_sorteio[linha_b - 1][coluna_b - 1]

            elif opc_posicao_2[0] == "E":  # Letras são considerados COLUNAS
                linha_b = int(opc_posicao_2[1])  # Número chega como string sendo convertidas para inteiro
                coluna_b = 5  # As letras são modificados por números reais
                resposta_2 = dados_sorteio[linha_b - 1][coluna_b - 1]

            elif opc_posicao_1 == '999':
                resp = input("Tem certeza que desaja sair? Vai perder todo o progresso (S/N): ").upper()
                if resp[0] == 'S':
                    del estrutura[:]
                    del sorteio_emoj[:]
                    print('Saindo do jogo!')
                    break
                else:
                    print('Voltando ao jogo!')
            else:
                print('Essa opção não existe')

        if jogada == 1:
            estrutura[linha_a][coluna_a] = resposta_1

            print(f'\n{linha_aparencia}')
            print(f'Sua pontuação: {ponto_partida}')

            """### A primeira posição foi entrada, então continuar a visualização para o jogador"""
            for linha in estrutura:
                print()
                for coluna in linha:
                    print(coluna, end=' ')

        elif jogada == 2:
            estrutura[linha_b][coluna_b] = resposta_2

            print(f'\n{linha_aparencia}')
            print(f'Sua pontuação: {ponto_partida}')

            """### Quando as pares são iguais, a estrutura vai se manter com a posição encontrada"""
            for linha in estrutura:
                print()
                for coluna in linha:
                    print(coluna, end=' ')

        elif jogada == 3:  # Jogada 3 é para saber se a 1º e 2º opção esta corretas

            if resposta_1 == resposta_2:
                ponto_partida += 1

                print(f'\n{linha_aparencia}')
                print(f'Parabéns! Você acertou! \n', f'Você esta com {ponto_partida} ponto')

                """### Caso acerte, a estrutura vai continuar o mesmo"""
                for linha in estrutura:
                    print()
                    for coluna in linha:
                        print(coluna, end=' ')

            else:
                print(f'\n{linha_aparencia}')
                print(f'Você errou')
                sair_do_jogo = input('Aperte "enter" para continuar (Sair=999)')

                if sair_do_jogo == '999':
                    print('Você esta saindo do jogo')
                    break
                """### Caso erre, a posição vai voltar com o icone padrão"""
                estrutura[linha_a][coluna_a] = ' 😄 '
                estrutura[linha_b][coluna_b] = ' 😄 '

                for linha in estrutura:
                    print()
                    for coluna in linha:
                        print(coluna, end=' ')

        if jogada == 3:
            jogada = 1
        else:
            jogada += 1


def _gravando_ponto(valor_entrada):
    print('Fim do jogo.')
    print(f'Sua pontuaçao foi: {valor_entrada}')
    print(linha_aparencia)
    nome_jogador = input('Digite seu nome: ').title()

    gravando_pontuacao = open(arq_save_pontos, 'w')
    gravando_pontuacao.write(f'')

"""### Menu principal"""
while True:

    print(f'\n{linha_aparencia}')
    print('''
                            [1] Iniciar jogo
                            [2] Ver pontuação
                            [0] Sair
          ''')
    resp_opcao_menu = leia_int('                            Escolha uma OPÇÂO: ')

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
