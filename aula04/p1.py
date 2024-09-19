string = input("Digite uma string: ")
posicaoInicio = int(input("Digite a posição a partir do início da string: "))
posicaoFinal = int(input("Digite a posição a partir do final da string: "))
caractereOriginal = input("Digite o caractere a ser substituído: ")
caractereSubstituto = input("Digite o caractere substituto: ")
sequencia = input("Digite a sequência de caracteres a ser verificada: ")
concatenar = input("Digite os caracteres que você queira concatenar: ")
caractereContar = input("Digite o caractere a ser contado: ")
caractereProcurar = input("Digite o caractere a ser encontrado: ")

caracteres = len(string)

primeiroCaractere = string[0]
ultimoCaractere = string[-1]

caractereInicio = string[posicaoInicio]
caractereFinal = string[-posicaoFinal]

maiusculas = string.upper()
minusculas = string.lower()

stringSubstituida = string.replace(caractereOriginal, caractereSubstituto)

palavras = string.split()
quantidadePalavras = len(palavras)

concatenacao = concatenar + string + concatenar

count = 0
for caractere in string:
    if caractere == caractereContar:
        count += 1

titulo = string.title()

#1
print("A quantidade de caracteres na string é:", caracteres)

#2
print("O primeiro caractere é:", primeiroCaractere)
print("O último caractere é:", ultimoCaractere)

#3
print(f"O caractere na posição {posicaoInicio} a partir do início da string é:", caractereInicio)

#4
print(f"O caractere na posição {posicaoFinal} a partir do final da string é:", caractereFinal)

#5
print("A string em maiúsculas é:", maiusculas)

#6
print("A string em minúsculas é:", minusculas)

#7
print("A string com os caracteres substituídos é:", stringSubstituida)

#8
print(f"A frase contém {quantidadePalavras} palavras.")

#9
if sequencia in string:
    print(f"A sequência '{sequencia}' foi encontrada na string.")
else:
    print(f"A sequência '{sequencia}' não foi encontrada na string.")
    
#10
print(f"String concatenada: {concatenacao}")

#11
print(f'O caractere "{caractereContar}" ocorre {count} vezes na string.')

#12
try:
    posicao = string.index(caractereProcurar)
    print(f'O caractere "{caractereProcurar}" está na posição {posicao} na string.')
except ValueError:
    print(f'O caractere "{caractereProcurar}" não foi encontrado na string.')

#13
if string.isalpha():
    print("A string é composta unicamente de caracteres alfabéticos.")
else:
    print("A string não é composta unicamente de caracteres alfabéticos.")
    
#14
if string.isdigit():
    print("A string é composta unicamente de caracteres numéricos.")
else:
    print("A string não é composta unicamente de caracteres numéricos.")

#15
print("String formatada como título:", titulo)