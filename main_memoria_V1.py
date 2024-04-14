import random

tabela = []

possibilidade = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L']

primeira_escolha = random.choice(possibilidade)
segunda_escolha = random.choice(possibilidade)
terceira_escolha = random.choice(possibilidade)

if primeira_escolha == segunda_escolha:
    segunda_escolha = random.choice(possibilidade)
if primeira_escolha and segunda_escolha == terceira_escolha:
    terceira_escolha = random.choice(possibilidade)

tabela = [[segunda_escolha], [primeira_escolha], [segunda_escolha], [primeira_escolha]]
for i in tabela:
    for y in i:
        print(i, y)
