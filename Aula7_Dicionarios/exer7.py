nomes = str(input("Digite uma lista de nomes (separado por vírgula): "))
listaNomes = [nome.strip() for nome in nomes.split(",")]


dicNomes = dict.fromkeys(listaNomes, 0)

print(dicNomes)