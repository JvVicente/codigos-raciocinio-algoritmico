cont = 0
while True:
    num = int(input("Digite um número: "))

    if num < 0:
        break
    if num % 2 == 0:
        cont += 1
print(cont)