lista1 = []
lista2 = []
novaLista3 = []
count = 0

for i in range(10):
    conteudo1 = input(f"Informe o {count + 1}º elemento da lista 1: ")
    lista1.append(conteudo1)
    conteudo2 = input(f"Informe o {count + 1}º elemento da lista 2: ")
    lista2.append(conteudo2)
    count += 1
    
for i in range(10):
    novaLista3.append(lista1[i])
    novaLista3.append(lista2[i])
    
print(f"Terceiro vetor intercalado: ")
print(novaLista3)