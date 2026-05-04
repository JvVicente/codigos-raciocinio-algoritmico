def processar_dados(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

processar_dados(1, 2, 3, nome="Ana", idade=20)