import os
import time

def clear_console():
    command = "clear"
    if os.name in("nt", "dos"):
        command = "cls"
    os.system(command)

dados = {"João": 18, "Vinicios": 20, "James": 53}

def menuPrincipal():
    clear_console()
    print("Escolha umas das seguintes opções: ")
    print("1 - Exibir os usuários cadastrados")
    print("2 - Buscar usuário pelo nome")
    print("3 - Adicionar novo usuário")
    print("4 - Atualizar idade de um usuário")
    print("5 - Remover usuário específico")
    print("6 - Remover último elemento")
    print("7 - Criar uma cópia e alterar dados")
    print("8 - Inicializar um novo dicionário")
    print("9 - Atualizar dicionário principal a partir de outro dicionário")
    print("10 - Limpar todos os dados do sistema")
    print("11 - Criar novo dicionário")
    print("0 - Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        exibirUsuarios()
    elif opcao == 2:
        buscarUsuario()
    elif opcao == 3:
        adicionarUsuario()
    elif opcao == 4:
        atualizarIdade()
    elif opcao == 5:
        removerUsuario()
    elif opcao == 6:
        removerUltimoElemento()
    elif opcao == 7:
        criarCopia()
    elif opcao == 8:
        novoDicionario()
    elif opcao == 9:
        atualizarDicionarioPrincipal()
    elif opcao == 10:
        limparDados()
    elif opcao == 11:
        criarNovoDicionario()

def exibirUsuarios():
    clear_console()
    print("1 - Mostrar apenas os nomes dos usuários")
    print("2 - Mostrar apenas as idades dos usuários")
    print("3 - Mostrar nome e idade dos usuários")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        print(dados.keys())
    elif opcao == 2:
        print(dados.values())
    elif opcao == 3:
        print(dados.items())
    else:   
        print("Está opção não existe!")

    time.sleep(2)
    menuPrincipal()

def buscarUsuario():
    clear_console()
    print(dados)
    nome = str(input("Digite o nome do usuário que deseja buscar: ")).strip()
    validacao = dados.get(nome)

    if validacao is None:
        clear_console()
        print(f"O usuário {nome} não existe!")
    else:
        clear_console()
        print(f"Usuário {nome} encontrado!")

    time.sleep(2)
    menuPrincipal()

def adicionarUsuario():
    clear_console()
    print(dados)
    qntd = int(input("Digite quantos usuários deseja adicionar: "))

    for i in range(qntd):
        clear_console()
        print(dados)
        nome = str(input(f"{i + 1} - Digite o nome do usuário que deseja: ")).strip()
        idade = int(input(f"{i + 1} - Digite a idade do usuário: "))
        dados[nome] = idade
        print("Usuário adicionado com sucesso!")
        time.sleep(2)
        clear_console()
    
    print(dados)
    print("Todos os usuários foram adiconado com sucesso!")
    input("Aperte enter para voltar ao menu principal: ")
    menuPrincipal()

def atualizarIdade():
    clear_console()
    print(dados)
    nome = str(input("Digite o nome do usuário que deseja alterar a idade: "))
    idadeNova = int(input("Digite a nova idade do usuário: "))

    atualizarTabela = {nome: idadeNova}
    dados.update(atualizarTabela)
    clear_console()
    
    print("Idade do usuário atualizada com sucesso!")
    print(dados)

    time.sleep(2)
    menuPrincipal()

def removerUsuario():
    clear_console()
    print(dados)
    nome = str(input("Digite o nome do usuário que deseja excluir: "))
    dados.pop(nome)
    clear_console()

    print("Usuário deletado com sucesso!")
    print(dados)

    time.sleep(2)
    menuPrincipal()

def removerUltimoElemento():
    clear_console()
    print(dados)
    dados.popitem()
    print("Removendo...")
    time.sleep(2)
    clear_console()
    print("Último elemento removido com sucesso!")
    print(dados)
    time.sleep(3)
    menuPrincipal()

def criarCopia():
    clear_console()
    print(dados)
    dadosCopia = dados.copy()
    nome = str(input("Digite o nome do usuário que deseja alterar o valor: "))
    novoValor = int(input("Digite o novo valor: "))
    dadosCopia[nome] = novoValor
    clear_console()

    print("Dados atualizados com sucesso!")
    print(dados)
    print(dadosCopia)
    time.sleep(5)
    menuPrincipal()

def novoDicionario():
    clear_console()
    nomes = str(input("Digite novos nomes para o dicionário novo (separado por vírgula): "))
    idades = int(input("Digite uma idade padrão para todos os usuários: "))
    listaNomes = [nome.strip() for nome in nomes.split(",")]
    novosDados = dict.fromkeys(listaNomes, idades)
    print("Criando...")
    time.sleep(2)
    clear_console()

    print("Novo dicionário criado")
    print(novosDados)
    time.sleep(3)
    menuPrincipal()

def atualizarDicionarioPrincipal():
    clear_console()
    print(dados)
    dicionariaNovo = {}
    qntd = int(input("Digite quantos usuários deseja adicionar no novo dicionário: "))
    for i in range(qntd):
        nome = str(input(f"Digite o nome do usuário {i + 1}: "))
        idade = str(input(f"Digite a idade do usuário {i + 1}: "))
        dicionariaNovo[nome] = idade
        clear_console()

    dados.update(dicionariaNovo)
    print("O dicionário principal com os novos dados é: ")
    print(dados)
    time.sleep(5)
    menuPrincipal()

def limparDados():
    clear_console()
    print(dados)
    confirmacao = str(input("Deseja realmente apagar todos os dados? ")).strip().lower()

    if confirmacao == "sim":
        clear_console()
        dados.clear()
        print("Dicionário apagado com sucesso!")
        print(dados)
    else: 
        clear_console()
        print("Opção cancelada!")
        print(dados)

    time.sleep(2)
    menuPrincipal()

def criarNovoDicionario():
    clear_console()
    dadosNovoDicionario = dict()

    qntd = int(input("Digite quantos usuários deseja adiconar no novo dicionário: "))

    for i in range(qntd):
        nome = str(input(f"Digite o nome do novo usuário {i + 1}: "))
        idade = int(input(f"Digite a idade do novo usuário {i + 1}: "))

        dadosNovoDicionario[nome] = idade

    print(dadosNovoDicionario)
    time.sleep(3)
    menuPrincipal()
menuPrincipal()