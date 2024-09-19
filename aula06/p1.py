lista = []
count = 0

for i in range(5):
    adiciona = int(input(f"Informe o {count + 1}º número: "))
    lista.append(adiciona)
    count += 1
    
print(lista)