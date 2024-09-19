def tipoTriangulo(a, b, c):
    if (a + b) < c or (a + c) < b or (b + c) < a:
        return "Os valores não formam um triângulo!"
    elif a == b and b == c:
        return "Equilátero"
    elif a != b and b != c and a != c:
        return "Escaleno"
    else:
        return "Isósceles"

a = int(input("Informe lado A do triângulo: "))
b = int(input("Informe lado B do triângulo: "))
c = int(input("Informe lado C do triângulo: "))

triangulo = tipoTriangulo(a, b, c)
print(triangulo)