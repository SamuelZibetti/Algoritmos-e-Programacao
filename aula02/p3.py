nota1 = float(input("Informe a primera nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("A média do aluno foi", media)
    print("O aluno foi APROVADO!")
else:
    print("A média do aluno foi", media)
    print("O aluno foi REPROVADO!")