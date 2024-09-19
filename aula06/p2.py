lista = []
count = 0

for i in range(10):
    adiciona = float(input(f"Informe o {count + 1}º número: "))
    lista.append(adiciona)
    count += 1

lista.reverse()
print(lista)