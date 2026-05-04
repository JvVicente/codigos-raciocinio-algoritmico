acumulador = 0
contador = 0

while True:
    n = float(input("Digite um número (se for negatino, o programa irá parar): "))

    if n < 0:
        break
    if n % 2 == 0: 
        acumulador += n
        contador += 1

    if contador > 0:
        media = acumulador / contador
        print(f"A soma dos números pares é: {acumulador}")
        print(f"A média dos números pares é: {media}")
    else:
        print("Nenhum número par foi digitado")