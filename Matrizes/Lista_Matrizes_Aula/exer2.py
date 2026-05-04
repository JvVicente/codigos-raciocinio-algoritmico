import numpy as np

estoque_inicial = np.array([
    [300, 400, 800],
    [500, 900, 200],
    [100, 600, 700]
])

vendidos = np.array([
    [200, 100, 700],
    [350, 600, 100],
    [50, 400, 350]
])

estoque_final = estoque_inicial - vendidos

print(f"O estoque inicial era de:\n{estoque_inicial}")
print(f"A quantidade vendida foi de:\n{vendidos}")
print(f"O estoque final é de:\n{estoque_final}")