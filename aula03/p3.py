a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))

if a % b == 0 or b % a == 0:
    print("São múltiplos!")
else:
    print("Não são múltiplos!")