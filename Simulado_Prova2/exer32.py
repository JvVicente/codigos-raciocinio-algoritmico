lista = [10, 15, 20, 25, 30]
contador = 0

for i in range(len(lista)):
    if i % 2 == 0:
        contador += 1

print(f"Existem {contador} números pares na lista")