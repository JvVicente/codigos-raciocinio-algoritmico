import conversor
import texto


conversor.conversorMetros()
conversor.conversorCelsius()

frase = input("Digite um texto: ")

print("Quantidade de letras:", texto.contar_letras(frase))
print("Texto em maiúsculo:", texto.para_maiusculo(frase))