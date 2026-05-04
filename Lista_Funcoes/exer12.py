def saudacao(nome, periodo = "dia"):
    print(f"Bom {periodo}, {nome}")

def saudacaoPadrao(nome="Visitante", periodo="dia"):
    print(f"Bom {periodo}, {nome}")


nome = str(input("Digite seu nome: "))
saudacao(nome)
saudacaoPadrao()