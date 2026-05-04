nome_alunos = []
qntd = int(input("Quantos alunos você quer cadastrar: "))

for i in range(qntd):
    nome = input(f"Digite o nome dos alunos: {i + 1} - ")
    nome_alunos.append(nome)

print("Nome dos alunos registrados: ")
for nome in nome_alunos:
    print(nome)