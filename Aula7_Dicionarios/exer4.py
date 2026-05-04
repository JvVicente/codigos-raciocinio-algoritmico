dados = dict()

for i in range(3):
    chave = str(input(f"Digite a chave do item {i + 1}: "))
    valor = str(input(f"Digite o valor do item {i + 1}: "))
    dados[chave] = valor

print("Os dados adicionados são: ", str(dados))