import random


"""#### Estrutura do programa"""
tabela = [[0, 0], [0, 0], [0, 0], [0, 0]]
cobertura = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8']]
possibilidade = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'H', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'X', 'Z', 'Y', 'K', 'W']

"""#### Declaração de Variaveis"""
linha, coluna = 0, 0
contador = 1
resposta_1 = ''
resposta_2 = ''
acerto = False
opcao_1 = False


primeira_escolha = random.choice(possibilidade)
segunda_escolha = random.choice(possibilidade)
terceira_escolha = random.choice(possibilidade)
quarta_escolha = random.choice(possibilidade)

if primeira_escolha == segunda_escolha:
    segunda_escolha = random.choice(possibilidade)
if primeira_escolha and segunda_escolha == terceira_escolha:
    terceira_escolha = random.choice(possibilidade)
if primeira_escolha and segunda_escolha and terceira_escolha == quarta_escolha:
    quarta_escolha = random.choice(possibilidade)

lista_tabela = [[terceira_escolha, quarta_escolha], [primeira_escolha, segunda_escolha],
                [terceira_escolha, quarta_escolha], [primeira_escolha, segunda_escolha]]

random.shuffle(lista_tabela)


while True:
    for i in cobertura:
        print()
        for y in i:
            print(f'[ {y} ]', end=' ')
    if contador == 1:
        opcao = input(f'\nDigita a {contador}° POSIÇÂO: ')
    else:
        opcao = input(f'\nDigita a {contador}º POSIÇÃO: ')

    if opcao_1:

    if opcao == cobertura[0][0]:
        cobertura[0][0] = str(lista_tabela[0][0])
        opcao_1 = True
        resposta_1 = str(lista_tabela[0][0])
        resposta_2 = str(lista_tabela[0][0])

    elif opcao == cobertura[0][1]:
        cobertura[0][1] = str(lista_tabela[0][1])
        resposta_1 = str(lista_tabela[0][1])
        resposta_2 = str(lista_tabela[0][1])

    elif opcao == cobertura[1][0]:
        cobertura[1][0] = str(lista_tabela[1][0])
        resposta_1 = str(lista_tabela[1][0])
        resposta_2 = str(lista_tabela[1][0])

    elif opcao == cobertura[1][1]:
        cobertura[1][1] = str(lista_tabela[1][1])
        resposta_1 = str(lista_tabela[1][1])
        resposta_2 = str(lista_tabela[1][1])

    elif opcao == cobertura[2][0]:
        cobertura[2][0] = str(lista_tabela[2][0])
        resposta_1 = str(lista_tabela[2][0])
        resposta_2 = str(lista_tabela[2][0])

    elif opcao == cobertura[2][1]:
        cobertura[2][1] = str(lista_tabela[2][1])
        resposta_1 = str(lista_tabela[2][1])
        resposta_2 = str(lista_tabela[2][1])

    elif opcao == cobertura[3][0]:
        cobertura[3][0] = str(lista_tabela[3][0])
        resposta_1 = str(lista_tabela[3][0])
        resposta_2 = str(lista_tabela[3][0])

    elif opcao == cobertura[3][1]:
        cobertura[3][1] = str(lista_tabela[3][1])
        resposta_1 = str(lista_tabela[3][1])
        resposta_2 = str(lista_tabela[3][1])
    else:
        print('Você escolheu uma opção errada. Digite de novo!')

    """#### Soma mais 1 no contador"""
    if contador == 2:
        contador = 1
        if resposta_1 == resposta_2:
            print('Parabens, você acertou!')
        else:
            print('Você errou, tente de novo!')
    else:
        contador += 1




