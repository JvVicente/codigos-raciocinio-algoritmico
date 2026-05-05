import numpy as np

matriz = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])

diagonal = matriz.diagonal()

print(f"Os elementos da diagonal princípal da matriz é: {diagonal}")