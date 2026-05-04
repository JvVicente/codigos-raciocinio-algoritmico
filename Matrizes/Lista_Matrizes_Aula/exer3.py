import numpy as np

ingredientes = np.array([
    [5, 7, 70],
    [6, 5, 8]
])

pedidos = np.array([
    [150, 300],
    [60, 674],
    [293, 743]
])

print(f"O resultado é:\n{ingredientes @ pedidos}")