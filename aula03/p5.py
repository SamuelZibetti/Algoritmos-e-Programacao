pessoas = []

for i in range(3):
    nome = input(f"Informe o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Informe a idade da {i+1}ª pessoa: "))
    pessoas.append((nome, idade))

maisVelha = pessoas[0]
maisNova = pessoas[0]

for pessoa in pessoas:
    if pessoa[1] > maisVelha[1]:
        maisVelha = pessoa
    elif pessoa[1] < maisNova[1]:
        maisNova = pessoa

print(f"A pessoa mais velha é {maisVelha[0]} com {maisVelha[1]} anos.")
print(f"A pessoa mais nova é {maisNova[0]} com {maisNova[1]} anos.")