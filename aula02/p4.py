x = int(input("Informe o valor X: "))
y = int(input("Informe o valor Y: "))
z = int(input("Informe o valor Z: "))

if x == y == z:
    print("Erro: valores são iguais!")
elif x > y and x > z:
    if y > z:
        print("X é o maior, Y é o intermediário e Z é o menor")
    else:
        print("X é o maior, Z é o intermediário e Y é o menor")     
elif y > x and y > z:
    if x > z:
        print("Y é o maior, X é o intermediário e Z é o menor")
    else:
        print("Y é o maior, Z é o intermediário e X é o menor") 
else:
    if x > y:
        print("Z é o maior, X é o intermediário e Y é o menor")
    else:
        print("Z é o maior, Y é o intermediário e X é o menor")