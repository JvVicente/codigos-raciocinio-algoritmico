x = 10
def teste():
    x = 5
    print(x)
teste()
print(x)

# A variável x de dentro da função, não altera a variável x de fora, mesmo tendo o mesmo nome
# Saída:
# 5
# 10