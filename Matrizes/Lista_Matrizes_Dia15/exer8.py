import numpy as np

matriz = np.array([
    [10, 5, 3],  
    [9, 5, 7],
    [15, 8, 22]
])

for i, linha in enumerate(matriz):
    media = np.mean(linha)
    print(f"A média da linha {i + 1} é: {media}")
