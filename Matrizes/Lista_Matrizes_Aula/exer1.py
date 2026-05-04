import numpy as np

manha = np.array([
    [10, 5, 3],    
    [9, 6, 7],
    [15, 8, 22]
])

tarde = np.array([
    [8, 9, 2],
    [11, 11, 5],
    [6, 7, 2]
])

print(f"A quantidade de chuva pela manhã foi:\n{manha}")
print(f"A quantidade de chuva pela tarde foi:\n{tarde}")
print(f"A quantidade de chuva total por região foi:\n{manha + tarde}")

