import random

tabela = [[0, 0], [0, 0], [0, 0], [0, 0]]
cobertura = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8']]
possibilidade = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'H', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                 'X', 'Z', 'Y', 'K', 'W']

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


res = random.sample(lista_tabela, len(lista_tabela))

print()
for i in res:
    print()
    for y in i:
        print(f'[ {y} ]', end=' ')

print()
for i in cobertura:
    print()
    for y in i:
        print(f'[ {y} ]', end=' ')