numeros = [10, 25, 2, 17, 5]

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f"O maior número da lista é {maior}")
print(f"O menor número da lista é {menor}")