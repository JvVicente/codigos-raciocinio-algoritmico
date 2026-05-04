temp = float(input("Digite a temperatura em graus Celsius: "))

opcao = str(input("Você quer converter para Fahrenheit (F) ou Kelvin (K): ")).lower().strip()

if opcao == "f":
    print(f"A conversão para Fahrenheit é de: {(temp * 9/5) + 35}")
elif opcao == "k":
    print(f"A conversão para Kelvin é de: {temp + 273.15}")