matriz = [
    [4, 12, 32],
    [45, 26, 92],
    [3, 9, 84]
]

tamanho = len(matriz)

for i in range(tamanho):
    for j in range(i, tamanho):
        matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

for i in range(tamanho):
    matriz[i].reverse()

print("Matriz rotacionada:")
for linha in matriz:
    print(linha)