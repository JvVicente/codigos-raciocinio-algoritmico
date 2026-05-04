import numpy as np

numeros = np.array([
    [10, 5, 3, 12],    
    [9, 6, 7, 17],
    [15, 8, 22, 30],
    [32, 10, 34, 50]
])

uns = np.ones(numeros.shape)

print(f"Matriz original: \n{numeros}")
print(f"Matriz uns: \n{uns}")