numeros = [2, 4, 6]

permutacoes = [[]]

for num in numeros:
    novas = []
    for p in permutacoes:
        for i in range(len(p) + 1):
            novas.append(p[:i] + [num] + p[i:])
    permutacoes = novas

for result in permutacoes:
    print(result)