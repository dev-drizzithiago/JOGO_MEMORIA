import random

tabela = [[0, 0], [0, 0], [0, 0], [0, 0]]
cobertura = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8']]
possibilidade = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L']

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

lista_tabela = [primeira_escolha, primeira_escolha, segunda_escolha, segunda_escolha,
                terceira_escolha, terceira_escolha, quarta_escolha, quarta_escolha]
print(lista_tabela)

for i in range(0, 1):
    tabela[0][i] = primeira_escolha
    tabela[0][i] = primeira_escolha
    tabela[1][i] = segunda_escolha
    tabela[1][i] = segunda_escolha
    tabela[2][i] = terceira_escolha
    tabela[2][i] = terceira_escolha
    tabela[3][i] = quarta_escolha
    tabela[3][i] = quarta_escolha

random.shuffle(lista_tabela)

print(tabela)

for i in lista_tabela:
    print()
    for y in i:
        print(f'[ {y} ]', end=' ')

print()
for i in cobertura:
    print()
    for y in i:
        print(f'[ {y} ]', end=' ')
