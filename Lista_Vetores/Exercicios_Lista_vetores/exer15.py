numeros = [12, 30, 10, 4, 5, 95, 33]
print(numeros)
qntd = int(input("Digite a quantidade de vezes que os elementos da lista rotacionem para a direita: "))
qntd = qntd % len(numeros)
rotacionada = numeros[-qntd:] + numeros[:-qntd]

print(rotacionada)