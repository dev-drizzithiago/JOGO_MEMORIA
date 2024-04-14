import random

tabela = [[0, 0], [0, 0], [0, 0], [0, 0]]
cobertura = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8']]
possibilidade = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'H', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'X', 'Z', 'Y', 'K', 'W']

linha, coluna = 0, 0

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

print(lista_tabela[0][0])
print(lista_tabela[0][1])
print(lista_tabela[1][0])
print(lista_tabela[1][1])
print(lista_tabela[2][0])
print(lista_tabela[2][1])
print(lista_tabela[3][0])
print(lista_tabela[3][1])

for i in lista_tabela:
    print()
    for y in i:
        print(f'[ {y} ]', end=' ')

while True:
    print(cobertura)
    for i in cobertura:
        print()
        for y in i:
            print(f'[ {y} ]', end=' ')

    opcao = input('\nDigita um número: ')
    print(lista_tabela[0][0])

    if opcao == cobertura[0][0]:
        cobertura[0][0] = str(lista_tabela[0][0])

    elif opcao == cobertura[0][1]:
        cobertura[0][1] = str(lista_tabela[0][1])

    elif opcao == cobertura[1][0]:
        cobertura[1][0] = str(lista_tabela[1][0])

    elif opcao == cobertura[1][1]:
        cobertura[1][1] = str(lista_tabela[1][1])

    elif opcao == cobertura[2][0]:
        cobertura[2][0] = str(lista_tabela[2][0])

    elif opcao == cobertura[2][1]:
        cobertura[2][1] = str(lista_tabela[2][1])

    elif opcao == cobertura[3][0]:
        cobertura[3][0] = str(lista_tabela[3][0])

    elif opcao == cobertura[3][1]:
        cobertura[3][1] = str(lista_tabela[3][1])




