nota = float(input("Digite uma nota: "))

if nota > 9.0:
    print("Parabéns!! Você foi aprovado!")
elif nota > 7.0 and nota < 8.9:
    print("Aprovado.")
elif nota > 4.0 and nota < 6.9:
    print("Você está de recuperação.")
else:
    print("Você está reprovado")