import random

tabela = [[0, 2], [3, 4], [5, 6], [7, 8]]
cobertura = [['0', '0'], ['0', '0'], ['0', '0'], ['0', '0']]

possibilidade = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L']

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

print(primeira_escolha)
print(segunda_escolha)
print(terceira_escolha)
print(quarta_escolha)

tabela[0][0] = primeira_escolha
tabela[0][1] = primeira_escolha
tabela[1][0] = segunda_escolha
tabela[1][1] = segunda_escolha
tabela[2][0] = terceira_escolha
tabela[2][1] = terceira_escolha
tabela[3][0] = quarta_escolha
tabela[3][1] = quarta_escolha

for i in tabela:
    print()
    for y in i:
        print(f'[ {y} ]', end=' ')

print()
for i in cobertura:
    print()
    for y in i:
        print(f'[ {y} ]', end=' ')
