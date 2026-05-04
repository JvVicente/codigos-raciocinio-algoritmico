import numpy as np

salarios = np.array([
    [3000, 1600, 5000],
    [8000, 6500, 2300],
    [4600, 3400, 7000]
])

print(f"Os salários sem o aumento são:\n{salarios}")
print(f"Os salários com o aumento são:\n{salarios * 1.10}")