distancia = float(input("Digite a distância que deseja percorrer em km: "))

if distancia <= 200:
    print(f"O preço da passagem é: {distancia * 0.50}")
else:
    print(f"O preço da passagem é: {distancia * 0.45}")