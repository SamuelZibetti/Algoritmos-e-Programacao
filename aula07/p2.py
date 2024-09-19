contato = {}

contato["nome"] = input("Informe o nome do contato: ")
contato["endereco"] = input("Informe o endereço do contato: ")
contato["telefone"] = input("Informe o telefone do contato: ")
contato["email"] = input("Informe o e-mail do contato: ")

print("\nDados do Contato:")
for chave, valor in contato.items():
    print(chave.capitalize() + ":", valor)