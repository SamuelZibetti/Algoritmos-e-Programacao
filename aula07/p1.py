listaCompras = set()

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir todos os itens")
    print("4. Ordenar a lista alfabeticamente")
    print("5. Gravar lista de compras em arquivo")
    print("6. Ler lista de compras de arquivo")
    print("7. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")
        if item in listaCompras:
            print(f"O item '{item}' já está na lista.")
        else:
            listaCompras.add(item)
            print(f"Item '{item}' adicionado à lista.")
        
    elif opcao == "2":
        item = input("Digite o item a ser removido: ")
        if item in listaCompras:
            listaCompras.remove(item)
            print(f"Item '{item}' removido da lista.")
        else:
            print(f"O item '{item}' não está na lista.")
            
    elif opcao == "3":
        if listaCompras:
            print("Itens na lista de compras:")
            for item in listaCompras:
                print(item)
        else:
            print("A lista de compras está vazia.")
            
    elif opcao == "4":
        listaOrdenada = sorted(listaCompras)
        print("Lista de compras ordenada alfabeticamente:")
        if listaCompras:
            print("Itens na lista de compras:")
            for item in listaOrdenada:
                print(item)
        else:
            print("A lista de compras está vazia.")
            
    elif opcao == "5":
        with open("lista.txt", "w") as file:
            for item in listaCompras:
                file.write(item + "\n")
        print("Lista de compras gravada em 'lista.txt'.")
                
    elif opcao == "6":
        listaCompras.clear()
        try:
            with open("lista.txt", "r") as file:
                for line in file:
                    listaCompras.add(line.strip())
            print("Lista de compras lida de 'lista.txt'.")
        except FileNotFoundError:
            print("O arquivo 'lista.txt' não foi encontrado.")
            
    elif opcao == "7":
        break
    else:
        print("Opção inválida. Tente novamente.")