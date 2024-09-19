count = 0
senha = input("Informe sua senha: ")

while senha != "2023":
    print("SENHA INVÁLIDA!")
    count += 1
    senha = input("Informe novamente sua senha: ")

print("ACESSO PERMITIDO!")
print(f"Foram realizadas {count + 1} tentativas para acessar a conta.")