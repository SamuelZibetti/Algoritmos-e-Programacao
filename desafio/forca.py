# Desafio de Desenvolvimento da Forca

import random

def buscarPalavras():
    with open("palavras.txt", "r") as file:
        palavras = file.readlines()
        return random.choice(palavras).strip()

def jogarForca():
    palavra = buscarPalavras()
    palavraEscondida = ['_ '] * len(palavra)
    tentativas = 1 
    letrasCorretas = []
    
    while True:
        print("A palavra é: ","".join(palavraEscondida))
        
        if tentativas == 6:
            print("Você foi enforcado! A palavra era:", palavra)
            break
        
        if '_ ' not in palavraEscondida:
            print("Parabéns! Você acertou a palavra:", palavra)
            break
            
        letra = input("Digite uma letra: ").lower()
        if letra in letrasCorretas:
            print("Você já tentou essa letra! Tente outra")
            continue
        if letra in palavra:
            print("Letra correta!")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavraEscondida[i] = letra
                    letrasCorretas.append(letra)
        else:
            tentativas += 1
            print(f"Você errou pela {tentativas - 1}ª vez. Tente de novo! ")
                                
jogarForca()