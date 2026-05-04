qntd_alunos = int(input("Digite a quantidade de alunos da turma: "))
notas_alunos = []

aprovados = 0
reprovados = 0

for i in range(qntd_alunos):
    nota_indiv = int(input("Digite a nota do aluno: "))
    notas_alunos.append(nota_indiv)

    if nota_indiv >= 60:
        aprovados += 1
    else:
        reprovados += 1

print(f"Quantidade de alunos acima de média: {aprovados}")
print(f"Quantidade de alunos abaixo de média: {reprovados}")