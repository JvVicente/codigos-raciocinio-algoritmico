lista1 = [2, 54, 12, 34, 77]
lista2 = [55, 10, 77, 2, 99]
numIguais = []

for num in lista1:
    if num in lista2 and num not in numIguais:
        numIguais.append(num)

print(numIguais)