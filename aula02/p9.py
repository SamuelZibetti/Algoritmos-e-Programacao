valorAnual = float(input("Informe o valor anual recebido: R$"))

if valorAnual <= 17989.80:
    print("Alíquota: Isento")
    print("Parcela a deduzir: R$0,00")
elif valorAnual >= 17989.81 and valorAnual <= 26961.00:
    IR = valorAnual * 0.075
    desconto = valorAnual - IR
    print("Alíquota: 7,5%")
    print(f"Parcela a deduzir: R${IR:.2f}")
    print(f"R${valorAnual:.2f} - R${IR:.2f} = R${desconto:.2f}")
elif valorAnual >= 26961.01 and valorAnual <= 35948.40:
    IR = valorAnual * 0.15
    desconto = valorAnual - IR
    print("Alíquota: 15%")
    print(f"Parcela a deduzir: R${IR:.2f}")
    print(f"R${valorAnual:.2f} - R${IR:.2f} = R${desconto:.2f}")
elif valorAnual >= 35948.41 and valorAnual <= 44918.28:
    IR = valorAnual * 0.225
    desconto = valorAnual - IR
    print("Alíquota: 22,5%")
    print(f"Parcela a deduzir: R${IR:.2f}")
    print(f"R${valorAnual:.2f} - R${IR:.2f} = R${desconto:.2f}")
else:
    IR = valorAnual * 0.275
    desconto = valorAnual - IR
    print("Alíquota: 27,5%")
    print(f"Parcela a deduzir: R${IR:.2f}")
    print(f"R${valorAnual:.2f} - R${IR:.2f} = R${desconto:.2f}")