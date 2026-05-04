a = []

for i in range(10):
    num = int(input(f"Digite um número inteiro: {i + 1} - "))
    a.append(num)

print(f"O menor valor é: {min(a)}")
print(f"O maior valor é: {max(a)}")
