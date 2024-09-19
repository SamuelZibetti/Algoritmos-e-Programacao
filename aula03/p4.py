nome = input("Informe seu nome: ")
dia = int(input("Informe o dia do seu nascimento: "))
mes = int(input("Informe o mês do seu nascimento: "))

if (mes == 1 and 21 <= dia <= 31) or (mes == 2 and 1 <= dia <= 18):
    signo = "Aquário"
elif (mes == 2 and 19 <= dia <= 29) or (mes == 3 and 1 <= dia <= 20):
    signo = "Peixes"
elif (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 20):
    signo = "Áries"
elif (mes == 4 and 21 <= dia <= 30) or (mes == 5 and 1 <= dia <= 21):
    signo = "Touro"
elif (mes == 5 and 22 <= dia <= 31) or (mes == 6 and 1 <= dia <= 21):
    signo = "Gêmeos"
elif (mes == 6 and 22 <= dia <= 30) or (mes == 7 and 1 <= dia <= 22):
    signo = "Câncer"
elif (mes == 7 and 23 <= dia <= 31) or (mes == 8 and 1 <= dia <= 23):
    signo = "Leão"
elif (mes == 8 and 24 <= dia <= 31) or (mes == 9 and 1 <= dia <= 22):
    signo = "Virgem"
elif (mes == 9 and 23 <= dia <= 30) or (mes == 10 and 1 <= dia <= 23):
    signo = "Libra"
elif (mes == 10 and 24 <= dia <= 31) or (mes == 11 and 1 <= dia <= 22):
    signo = "Escorpião"
elif (mes == 11 and 23 <= dia <= 30) or (mes == 12 and 1 <= dia <= 21):
    signo = "Sagitário"
elif (mes == 12 and 22 <= dia <= 31) or (mes == 1 and 1 <= dia <= 20):
    signo = "Capricórnio"
else:
    signo = "Data inválida"

print(f"O signo de {nome} é {signo}.")