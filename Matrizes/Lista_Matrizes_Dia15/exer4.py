import numpy as np

matriz = np.array([
    [10, 5],
    [9, 6]
])

matriz[0], matriz[1] = matriz[1].copy(), matriz[0].copy()

print(matriz)