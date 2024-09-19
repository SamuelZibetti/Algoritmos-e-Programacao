def testePrimo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

valor = int(input("Informe um número: "))
resultado = testePrimo(valor)
if resultado:
    print(f"{valor} é primo.")
else:
    print(f"{valor} não é primo.")