import numpy as np

matriz = np.array([
    [10, 5, 3],  
    [9, 5, 7],
    [15, 8, 22]
])

listaSomas = [0, 0, 0]

for j in range(3):
    for i in range(3):
        listaSomas[j] += int(matriz[i][j])

print(f"A soma de cada coluna da matriz é: {listaSomas}")

