

def cria_matriz(m, n, valor):
    matriz = []
    linha = [valor]*n
    for i in range(m):
        matriz.append(linha[:])
    print(matriz)


linha = 5
coluna = 5
valor = 11

cria_matriz(linha, coluna, valor)
