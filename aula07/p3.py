estoqueIngredientes = {}

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item")
    print("2. Editar item")
    print("3. Remover item")
    print("4. Listar todos os itens")
    print("5. Contagem de itens")
    print("6. Limpar o dicionário")
    print("7. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do ingrediente: ")
        fabricante = input("Digite o fabricante do ingrediente: ")
        estoque = int(input("Digite a quantidade em estoque: "))
        unidade = input("Digite a unidade de medida (kg, g, etc.): ")
        
        ingrediente = {
            "nome": nome,
            "fabricante": fabricante,
            "estoque": estoque,
            "unidade": unidade
        }
    
        estoqueIngredientes[nome] = ingrediente
        print(f"{nome} foi adicionado ao estoque.")
        
    elif opcao == "2":
        nome = input("Digite o nome do ingrediente que deseja editar: ")
        if nome in estoqueIngredientes:
            novoEstoque = int(input(f"Digite o novo estoque para {nome}: "))
            estoqueIngredientes[nome]["estoque"] = novoEstoque
            print(f"Estoque de {nome} foi atualizado para {novoEstoque}.")
        else:
            print(f"{nome} não encontrado no estoque.")
            
    elif opcao == "3":
        nome = input("Digite o nome do ingrediente que deseja remover: ")
        if nome in estoqueIngredientes:
            del estoqueIngredientes[nome]
            print(f"{nome} foi removido do estoque.")
        else:
            print(f"{nome} não encontrado no estoque.")
            
    elif opcao == "4":
        print("Lista de ingredientes no estoque:")
        for nome, ingrediente in estoqueIngredientes.items():
            print(f"Nome: {nome}, Fabricante: {ingrediente['fabricante']}, Estoque: {ingrediente['estoque']} {ingrediente['unidade']}")
        
    elif opcao == "5":
        print(f"Total de ingredientes em estoque: {len(estoqueIngredientes)}")
        
    elif opcao == "6":
        estoqueIngredientes.clear()
        print("O estoque foi limpo.")
        
    elif opcao == "7":
        break
    
    else:
        print("Opção inválida. Tente novamente.")