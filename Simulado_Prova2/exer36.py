estoque = {"Refrigerante": 10, "Salgadinho": 5.99, "Chocolate": 7.99}

print(estoque)
produto = str(input("Digite o nome do produto que deseja alterar o valor: "))
novoValor = float(input("Digite o novo valor: "))

estoque[produto] = novoValor

print(f"Estoque atualizado: \n{estoque}")