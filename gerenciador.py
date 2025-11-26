def adicionar_contato(contatos, nome, telefone, email, favorito):
    erros = []
    if nome.strip() == "":
        erros.append("O nome do contato não pode ser vazio.")
    if not telefone.isdigit():
        erros.append("O telefone do contato deve conter apenas números.")
    if '@' not in email or '.' not in email:
        erros.append("O email do contato deve ser um email válido.")
    if favorito.lower() not in ['s', 'n']:
        erros.append("O campo favorito deve ser 's' para sim ou 'n' para não.")
    
    if erros:
        raise ValueError("\n".join(erros))
    
    contatos[nome] = {
        'telefone': telefone,
        'email': email,
        'favorito': favorito
    }
    return f"O contato de {nome} foi adicionado com sucesso!\n"

def adicionar_favorito(contatos, nome):
    for nomeContato in contatos.keys():
        if nomeContato.lower() == nome.lower():
            if contatos[nomeContato]['favorito'].lower() != 's':
                contatos[nomeContato]['favorito'] = 's'
                return f"O contato de {nome} foi adicionado aos favoritos com sucesso!\n"
            else:
                return f"O contato de {nome} já é um favorito.\n"
    return f"O contato de {nome} não foi encontrado.\n"    

def listar_contatos(contatos):
    if contatos:
        for nome, dados in contatos.items():
            print(f"Nome: {nome}\nTelefone: {dados['telefone']}\nEmail: {dados['email']}\nFavorito: {dados['favorito']}\n") 
    else:
        print("Nenhum contato cadastrado.\n")

def listar_favoritos(contatos):
    encontrou = False
    if contatos:
        for nome, dados in contatos.items():
            if dados['favorito'].lower() == 's':
                print(f"Nome: {nome}\nTelefone: {dados['telefone']}\nEmail: {dados['email']}\nFavorito: {dados['favorito']}\n")
                encontrou = True
        if not encontrou:
            print("Nenhum contato favorito encontrado.\n")
    else:
        print("Nenhum contato favorito encontrado.\n")

def atualizar_contato(contatos, nome):
    try: 
        erros = []
        for nomeContato in contatos.keys(): 
            if nomeContato.lower() == nome.lower():
                nomeNovo = input("Digite o novo nome do contato: ")
                while nomeNovo.strip() == "":
                    print("O nome do contato não pode ser vazio.")
                    nomeNovo = input("Digite o novo nome do contato: ")
                    
                telefone = input("Digite o novo telefone de contato: ")
                email = input("Digite o novo email de contato: ")
                favorito = input("O contato é favorito? (s/n): ").lower()
                
                if not telefone.isdigit():
                    erros.append("O telefone do contato deve conter apenas números.")
                if '@' not in email or '.' not in email:
                    erros.append("O email do contato deve ser um email válido.")
                if favorito.lower() not in ['s', 'n']:
                    erros.append("O campo favorito deve ser 's' para sim ou 'n' para não.")

                if nomeContato != nomeNovo and erros == []:
                    del contatos[nomeContato]
                
                if erros:
                    raise ValueError("\n".join(erros))
                
                
                contatos[nomeNovo] = {
                    'telefone': telefone,
                    'email': email,
                    'favorito': favorito
                }
                return "O contato foi atualizado com sucesso!\n"
        return f"O contato de {nome} não foi encontrado.\n"
    except ValueError as a:
        return f"Erro ao atualizar o contato: {a}\n"
    except Exception as e: 
        return f"Erro inesperado ao atualizar o contato: {e}\n"


def remover_contato(contatos, nome):
    for nomeContato in list(contatos.keys()):
        if nomeContato.lower() == nome.lower():
            del contatos[nomeContato]
            return f"O contato de {nome} foi removido com sucesso!\n"
    return f"O contato de {nome} não foi encontrado.\n"

def remover_favorito(contatos, nome):
    for nomeContato, dados in contatos.items():
        if nomeContato.lower() == nome.lower():
            if dados['favorito'] == 'n':
                return f"O contato de {nome} não é um favorito.\n"
            dados['favorito'] = 'n'
            return f"O contato de {nome} foi removido dos favoritos com sucesso!\n"
    return f"O contato de {nome} não foi encontrado.\n"

contatos = {}       
opcao = -1

print("Bem-vindo ao gerenciador de contatos!\n")

while opcao != 0:
    print("Escolha uma das opções do menu:")
    print("1 - Adicionar contato")
    print("2 - Adicionar contato aos favoritos")
    print("3 - Listar contatos")
    print("4 - Listar contatos favoritos")
    print("5 - Atualizar contato")
    print("6 - Remover contato")
    print("7 - Remover contato dos favoritos")
    print("Digite '0' para encerrar o programa.\n")

    try:
        opcao = int(input("Opção: "))

    except ValueError:
        print("Entrada inválida. Por favor, insira um número correspondente a uma das opções do menu.\n")
        continue

    if opcao == 1: 
        try: 
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            favorito = input("O contato é favorito? (s/n): ").lower()
            resultado = adicionar_contato(contatos, nome, telefone, email, favorito)
            print(resultado)
        except ValueError as a:
            print(f"Erro ao adicionar o contato: {a}\n")
        except Exception as e:
            print(f"Erro inesperado ao adicionar o contato: {e}\n")
    elif opcao == 2:
        nome = input("Digite o nome do contato a ser adicionado aos favoritos: ")
        while nome.strip() == "":
            print("O nome do contato não pode ser vazio.")
            nome = input("Digite o nome do contato a ser adicionado aos favoritos: ")
        resultado = adicionar_favorito(contatos, nome)
        print(resultado)
    elif opcao == 3:
        print("Lista de contatos:\n")
        listar_contatos(contatos)
    elif opcao == 4:
        print("Lista de contatos favoritos:\n")
        listar_favoritos(contatos)
    elif opcao == 5:
        nome = input("Digite o nome do contato a ser atualizado: ")
        while nome.strip() == "":
            print("O nome do contato não pode ser vazio.")
            nome = input("Digite o nome do contato a ser atualizado: ")
        resultado = atualizar_contato(contatos, nome)
        print(resultado)
    elif opcao == 6:
        nome = input("Digite o nome do contato a ser removido: ")
        while nome.strip() == "":
            print("O nome do contato não pode ser vazio.")
            nome = input("Digite o nome do contato a ser removido: ")
        resultado = remover_contato(contatos, nome)
        print(resultado)
    elif opcao == 7:
        nome = input("Digite o nome do contato a ser removido dos favoritos: ")
        while nome.strip() == "":
            print("O nome do contato não pode ser vazio.")
            nome = input("Digite o nome do contato a ser removido dos favoritos: ")
        resultado = remover_favorito(contatos, nome)
        print(resultado)
    elif opcao == 0:
        print("Encerrando o programa.\n")
    else:
        print("Opção inválida. Por favor, tente novamente.\n")
