def cria_matriz(m, n, valor):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(valor)
        matriz.append(linha)
    print(matriz)


linha = 5
coluna = 5
valor = 0

cria_matriz(linha, coluna, valor)