import numpy as np

A = np.array([
    [5, 2, 7],
    [12, 3, 9]
])

B = np.array([
    [10, 18],
    [16, 20],
    [21, 32]
])

resultado = A @ B

print(f"O resultado da multiplicação das matrizes é : \n{resultado}")