numeros = [32, 23, 95, 12, 74, 62]
encontrado = False

num = int(input("Digite um número para verificar se está na lista: "))

for i in numeros:
    if num == i:
        encontrado = True

if encontrado:
    print(f"O número {num} está na lista")
else:
    print(f"O número {num} não está na lista")