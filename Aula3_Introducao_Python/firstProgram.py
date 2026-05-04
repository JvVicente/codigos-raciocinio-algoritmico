# NOME E IDADE
nome = str(input("Digite seu nome: "))
age = int(input("Digite sua idade: "))

if age < 18:
    print(f"Seu nome é {nome} e é menor de idade!")
else: 
    print(f"Seu nome é {nome} e é maior de idade!")


# CALCULADORA
calculator = str(input("Quer usar a calculadora? (s/n) ")).strip().lower()

while (calculator != "n"):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    operator = int(input("Escolha qual operação você quer usar: "))
    if(operator == 1):
        print("O resultado da soma é: ", num1 + num2)
    elif(operator == 2):
        print("O resultado da subtração é: ", num1 - num2)
    elif(operator == 3):
        print("O resultado da  multiplicação é: ", num1 * num2)
    elif(operator == 4):
        print("O resultado da  divisão é: ", num1 / num2)

    repeat = str(input("Deseja fazer outra operação? (s/n)")).strip().lower()
    if(repeat == "n"):
        print("Fechando!")
        break
else:
    print("Não irá utilizar a calculadora")