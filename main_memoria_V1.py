import random

tabela = []

possibilidade = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L']

primeira_escolha = random.choice(possibilidade)
segunda_escolha = random.choice(possibilidade)
if primeira_escolha == segunda_escolha:
    segunda_escolha = random.choice(possibilidade)

tabela = [primeira_escolha, segunda_escolha]
print(tabela)
