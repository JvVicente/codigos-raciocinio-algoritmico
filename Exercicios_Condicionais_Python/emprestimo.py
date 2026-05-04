precoCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
ano = int(input("Digite em quantos anos você deseja pagar: "))

if precoCasa / (12 * ano) > 0.30 *salario:
    print("Empréstimo negado!")
else: 
    print("Empréstimo aprovado!")