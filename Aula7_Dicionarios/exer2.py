tabela = {"bolo": 9.99, "doritos": 5, "oreo": 3.99}

produto = str(input("Digite o produto que deseja alterar: "))
precoNovo = float(input("Digite o novo preço do produto: $"))

tabelaNova = {produto: precoNovo}
tabela.update(tabelaNova)

print(tabela)
