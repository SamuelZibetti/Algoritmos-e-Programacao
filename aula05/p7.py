count = 0

while count < 10:
    numero = int(input(f"Informe o {count + 1}º número: "))
    
    if numero == 0:
        print("Número inválido, tente novamente!")
    elif numero > 0:
        print(f"O número {numero} é positivo.")
        count += 1
    else:
        print(f"O número {numero} é negativo.")
        count += 1