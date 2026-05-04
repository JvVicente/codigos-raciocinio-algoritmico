import numpy as np

matriz = np.array([
    [10, 5, 3, 43, 21],  
    [9, 5, 7, 83, 32],
    [15, 8, 22, 96, 37],
    [74, 54, 120, 432, 90],
    [986, 734, 12, 45, 342]
])

diagonal = np.fliplr(matriz).diagonal()

print(diagonal)