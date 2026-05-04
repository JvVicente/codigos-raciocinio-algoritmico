import numpy as np

matriz = np.array([
    [10, 5, 3, 23],  
    [9, 6, 7, 97],
    [15, 8, 22, 82]
])

contPares = 0
for linhas in matriz:
    for num in linhas:
        if num % 2 == 0:
            contPares += 1

print(matriz)
print(f"Existem {contPares} números pares na matriz")