x = int(input("Informe o primeiro valor: "))
y = int(input("Informe o segundo valor: "))

if x == y:
    print("Erro: valores são iguais!")
elif x > y:
    print("Primeiro valor é o MAIOR")
    print("Segundo valor é o MENOR")
else:
    print("Primeiro valor é o MENOR")
    print("Segundo valor é o MAIOR")