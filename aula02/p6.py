salario = float(input("Informe o salário do funcionário: "))
cargo = int(input("Informe o código do cargo: "))

if cargo ==  101:
    salarioNovo = salario * 1.10
    diferenca = salarioNovo - salario
    print(f"Salário antigo: R${salario}")
    print(f"Salário novo: R${salarioNovo}")
    print(f"Diferença entre salários: R${diferenca}")
elif cargo == 102:
    salarioNovo = salario * 1.20
    diferenca = salarioNovo - salario
    print(f"Salário antigo: R${salario}")
    print(f"Salário novo: R${salarioNovo}")
    print(f"Diferença entre salários: R${diferenca}")
elif cargo == 103:
    salarioNovo = salario * 1.30
    diferenca = salarioNovo - salario
    print(f"Salário antigo: R${salario}")
    print(f"Salário novo: R${salarioNovo}")
    print(f"Diferença entre salários: R${diferenca}")
else:
    salarioNovo = salario * 1.40
    diferenca = salarioNovo - salario
    print(f"Salário antigo: R${salario}")
    print(f"Salário novo: R${salarioNovo}")
    print(f"Diferença entre salários: R${diferenca}")