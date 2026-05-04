def executar(funcao, valor):
    return funcao(valor)

quadrado = lambda x: x ** 2

resultado = executar(quadrado, 5)

print(resultado)