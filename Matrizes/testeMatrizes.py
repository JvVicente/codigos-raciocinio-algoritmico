import numpy as np

matrizZero = np.zeros((2, 3))
matrizOne = np.ones((3, 2))
matrizEye = np.eye(3)

print(matrizZero)
print(matrizOne)
print(matrizEye)


matriz = [
    [1, 2, 3], 
    [4, 5, 6]
]

elemento = matriz[1][2]
print(f"Elemento: {elemento}")

matriz[0][1] = 9
print(f"Matriz modificada: {matriz}")

A = np.array([[1, 2 ],
             [3, 4 ]])

B = np.array([[5, 6 ],
             [7, 8 ]])

C = A + B
D = A - B
E = np.dot(A, B)
A_transposta = A.T

print(f"A soma das matrizes é: {C}")
print(f"A subtração das matrizes é: {D}")
print(f"A multiplicação das matrizes é: {E}")
print(f"A matriz A transposta é: {A_transposta}")

