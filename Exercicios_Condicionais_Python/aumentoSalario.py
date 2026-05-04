salario = float(input("Digite o salário: "))

if salario > 1621:
    print(f"O seu salário agora é de: R${salario * 1.1}")
else:
    print(f"O seu salário agora é de: R${salario * 1.15}")