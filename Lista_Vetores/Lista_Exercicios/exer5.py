numeros = []
par = []
impar = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

if len(par) != 0:
    print(f"O maior número da lista par é: {max(par)}")
else:
    print("Não existe número par!")

if len(impar) != 0:
    print(f"O menor número da lista impar é: {min(impar)}")
else:
    print("Não existe número impar!")

print(f"O somatório de todos os elementos da lista é: {sum(numeros)} ")
print(f"a média de todos os elementos da lista é: {sum(numeros) / len(numeros)} ")
