import numpy as np

matriz = np.array([
    [10, 5, 3, 42],  
    [9, 6, 7, 19],
    [15, 8, 22, 75],
    [90, 21, 53, 89]
])

soma = 0

for i in range(len(matriz)):
    soma += matriz[i][i]

print(matriz)
print(f"A soma da diagonal principal da matriz é: {soma}")