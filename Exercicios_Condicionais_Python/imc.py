peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))


if peso / (altura ** 2) > 25:
    print("Acima do peso ideal")
else:
    print("Peso dentro da normalidade")