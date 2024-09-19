idade = int(input("Idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("O nadador se encaixa na categoria Infantil A")
elif idade >= 8 and idade <= 10:
    print("O nadador se encaixa na categoria Infantil B")
elif idade >= 11 and idade <= 13:
    print("O nadador se encaixa na categoria Juvenil A")
elif idade >= 14 and idade <= 17:
    print("O nadador se encaixa na categoria Juvenil B")
else:
    print("O nadador se encaixa na categoria Adulto")