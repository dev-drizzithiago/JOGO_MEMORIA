import random

tabela = [[]]

possibilidade = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'L']

primeira_escolha = random.choice(possibilidade)
sengunda_escolha = random.choice(possibilidade)
if primeira_escolha == sengunda_escolha:
    sengunda_escolha = random.choice(possibilidade)

print(primeira_escolha)
print(sengunda_escolha)

