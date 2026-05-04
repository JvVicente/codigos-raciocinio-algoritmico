numeros = [33, 10, 2, 40, 12, 8]

tamanho = 1

while tamanho < len(numeros):
    for i in range(0, len(numeros), 2 * tamanho):
        esquerda = numeros[i:i + tamanho]   
        direita = numeros[i + tamanho:i + 2 * tamanho]

        resultado = []
        a = b = 0


        while a < len(esquerda) and b < len(direita):
            if esquerda[a] < direita[b]:
                resultado.append(esquerda[a])
                a += 1
            else:
                resultado.append(direita[b])
                b += 1

        resultado.extend(esquerda[a:])
        resultado.extend(direita[b:])

        numeros[i:i + 2 * tamanho] = resultado

    tamanho *= 2

print("Lista ordenada:", numeros)