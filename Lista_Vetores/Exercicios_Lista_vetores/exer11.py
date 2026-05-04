numeros = [1, 3, 7, 2, 3, 9, 1]
vistos = set()
resultado = []

for item in numeros:
    if item not in vistos:
        vistos.add(item)
        resultado.append(item)

print(resultado)