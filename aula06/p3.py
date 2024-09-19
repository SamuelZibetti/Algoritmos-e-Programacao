lista = []
novaLista = []
vogais = ["a", "e", "i", "o", "u"]
consoantesConta = 0
count = 0

for i in range(10):
    adiciona = input(f"Informe o {count + 1}º caractere: ")
    lista.append(adiciona)
    count += 1
    
for adiciona in lista:
    if adiciona not in vogais:
        novaLista.append(adiciona)
        consoantesConta += 1

print(f"Foram lidas {consoantesConta} consoantes.")
print(novaLista)