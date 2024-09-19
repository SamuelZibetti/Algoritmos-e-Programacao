alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())

for i in range(n):
    palavra = input().upper()
    pulos = int(input())
    resultado = ""
    
    for letra in palavra:
        inicio = alfabeto.index(letra)
        resultado += alfabeto[inicio - pulos]
        
    print(resultado)