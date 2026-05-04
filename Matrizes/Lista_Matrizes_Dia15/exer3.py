import numpy as np

matriz = np.array([
    [10, 5, 3, 12],    
    [9, 6, 7, 17],
    [15, 8, 22, 30],
    [75, 19, 84, 92]
])

num = int(input("Digite um número para busca-lo na matriz: "))

if num in matriz:
    print(f"O número {num} está na matriz!")
else: 
    print(f"o número {num} não está na matriz!")