dados = {"Nome": "João", "Idade": 18, "Faculdade": "PUC", "Início": 2026}

dadosAtualizados = dados.copy()

dadosAtualizados["Nome"] = "Hillary"
dadosAtualizados["Faculdade"] = "UTFPR"

print(dados)
print(dadosAtualizados)