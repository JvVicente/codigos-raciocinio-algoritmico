dados = {"Lego": 200, "Carrinho": 50, "Loja": "BeHappy", "Idade": 10}

print(dados)
excluir = str(input("Deseja apagar todos os dados: ")).strip().lower()

if excluir == "sim":
    dados.clear()
    print(f"Dicionário apagado: {dados}")
else: 
    print(dados)