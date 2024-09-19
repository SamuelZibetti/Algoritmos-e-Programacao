lista = []
alunos = 0

for i in range(10):
    nota1 = float(input("Informe a 1º nota do aluno: "))
    nota2 = float(input("Informe a 2º nota do aluno: "))
    nota3 = float(input("Informe a 3º nota do aluno: "))
    nota4 = float(input("Informe a 4º nota do aluno: "))
    
    media = (nota1 + nota2 + nota3+ nota4) / 4
    if media >= 7:
        alunos += 1
    lista.append(media)
    
print(f"{alunos} alunos ficaram na média.")
print(lista)