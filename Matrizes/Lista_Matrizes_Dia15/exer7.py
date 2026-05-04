import numpy as np

matriz = np.array([
    [10, 5, 3],  
    [9, 6, 7],
    [15, 8, 22]
])

maiorElemento = np.max(matriz)

print(matriz)
print(f"O número {maiorElemento} é o maior elemento da matriz")