import numpy as np

numeros = np.array([
    [10, 5, 3, 12, 67],    
    [9, 6, 7, 17, 77],
    [15, 8, 22, 30, 89],
    [32, 10, 34, 50, 19],
    [100, 128, 46, 71, 93]
])

numerosModificados = np.copy(numeros)

numerosModificados[0][1] = 23
numerosModificados[2][4] = 200

print(f"A matriz original é: \n{numeros}")
print(f"A matriz modificada é: \n{numerosModificados}")