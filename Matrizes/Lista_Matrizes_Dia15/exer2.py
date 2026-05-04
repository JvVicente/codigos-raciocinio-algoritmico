import numpy as np

num = int(input("Digite um número para criar uma matriz identidade: "))

matriz = np.eye(num)

print(f"Sua matriz identidade do número {num} é: \n{matriz}")