import numpy as np 

matriz = np.array([
    [10, 5, 3],  
    [9, 5, 7],
    [15, 8, 22]
])

simetrica = np.array_equal(matriz, matriz.T)

print(f"A matriz é simétrica? {simetrica}")