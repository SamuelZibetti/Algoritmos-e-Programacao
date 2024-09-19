x = int(input("Informe um valor: "))
y = int(input("Informe outro valor: "))

for i in range(x, y+1):
    if i % 2 == 0:
        print(f"O número {i} é par!")
    else:
        print(f"O número {i} é ímpar!")