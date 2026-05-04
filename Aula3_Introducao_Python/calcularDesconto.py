preco = float(input("Digite o preço do produto: $"))
desconto = int(input("Digite quantos porcento de desconto: "))

valorDesconto = preco * (desconto/100)

valorFinal = preco - valorDesconto

print(f"O valor do produto sem desconto é ${preco} e com {desconto}% é {valorFinal}")