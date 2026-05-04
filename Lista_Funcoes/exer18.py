contador = 0
def incrementar():
    contador += 1   

# O python entende que a variável contador dentro da função, é uma variável local, porém ela foi definida fora da função
# a solução é mostrar que exite um contador global

contador = 0
def incrementar():
    global contador 
    contador += 1   
    print(contador)

incrementar()