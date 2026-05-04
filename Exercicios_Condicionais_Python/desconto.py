preco = float(input("Digite o preço do produto: $"))

if preco > 100:
    print("Você tem direito a 10% de desconto!")
    print("O valor final do produto é: $", preco * 0.9)
else:
    print("O preço do produto é: $", preco)
    print("Nas Nas compras acima de R$ 100, você ganha 10% de desconto!")