notas = {"João": 8, "Hillary": 10, "Pedro": 8.5, "Vinicius": 9.9}

nome = str(input("Digite o nome do aluno que deseja ver a nota: ")).strip()

if nome in notas:
    print(f"A nota do(a) aluno(a) {nome} é: {notas.get(nome)}")
else:
    print("Aluno não encontrado no sistema!")