a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))
c = int(input("Informe o terceiro valor: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b and a == c:
        print("Triângulo Equilátero")
    else:
        if a == b or a == c or b == c:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
else:
    print("Os valores não formam um triângulo!")