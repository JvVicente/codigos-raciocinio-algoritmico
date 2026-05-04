dados = {"Carro": "Celta", "Monster": 12, "Dia": "Domingo", "Gasolina": 6.99}
dadosNovos = {}
print(dados)
chave = str(input("Digite uma chave para remover: ").strip())

dados.pop(chave, None)
dados.popitem()

qntd = int(input("Digite quantos novos dados deseja adicionar ao dicionário: "))

for i in range(qntd):
    chaveNova = str(input(f"Digite a chave do novo dado {i + 1}: ")).strip()
    valorNovo = str(input(f"Digite o valor do novo dado {i + 1}: ")).strip()
    dadosNovos[chaveNova] = valorNovo

dados.update(dadosNovos)
print(dados)
