valor = float(input("Informe o valor da passagem: "))
quantidade = int(input("Informe a quantidade de passagens compradas: "))

count = 0

if quantidade <= 50:
    desconto = (valor * quantidade) * 0.60
    valorEscolar = valor * 0.60
    valor = 0
    semDesconto = 0
else:
    count = quantidade - 50
    desconto = (valor * 50) * 0.60
    valorEscolar = valor * 0.60
    semDesconto = valor * count

total = desconto + semDesconto

print(f"Valor da passagem escolar com desconto: R${valorEscolar:.2f}")
print(f"Valor da passagem sem o desconto: R${valor:.2f}")
print(f"Montante a ser pago pelas passagens: R${total:.2f}")