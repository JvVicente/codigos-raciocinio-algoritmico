def somar_todos(*numeros):
    return sum(numeros)

qntd = int(input("Digite quantos números deseja somar: "))
lista = []

for i in range(qntd):
    num = float(input(f"Digite o {i + 1} número: "))
    lista.append(num)

print("Soma: ", somar_todos(*lista))