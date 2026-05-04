import numpy as np

matriz = np.array([
    [10, 5, 3],  
    [9, 6, 7],
    [15, 8, 22]
])

print(matriz)
num = int(input("Digite um número para multiplicar a matriz: "))

matrizMultiplicada = num * matriz

print(f"A matriz resultante da multiplicação escalar do número {num} é: \n{matrizMultiplicada}")