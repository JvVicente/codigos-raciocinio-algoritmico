numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

somaAtual = numeros[0]
maiorValor = numeros[0]

for i in range(1, len(numeros)):
    somaAtual = max(numeros[i], somaAtual + numeros[i])
    
    if somaAtual > maiorValor:
        maiorValor = somaAtual

print("Maior soma:", maiorValor)