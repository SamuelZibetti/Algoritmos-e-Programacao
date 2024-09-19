positivo = 0
negativo = 0

for i in range(10):
    numero = int(input(f"Informe o {i + 1}º número: "))
    if numero > 0:
        positivo += 1
    else:
        negativo += 1

print(f"Desses números {positivo} são positivos e {negativo} são negativos.")