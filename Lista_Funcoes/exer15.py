def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
listaDados = {}

qntd = int(input("Digite qunatos dados (chave: valor) deseja digitar: "))

for i in range(qntd):
    chave = str(input(f"Digite a chave do dado {i + 1}: "))
    valor = str(input(f"Digite o valor do dado {i + 1}: "))
    listaDados[chave] = valor

    
mostrar_dados(**listaDados)