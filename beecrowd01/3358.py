n = int(input())

for i in range(n):
    sobrenome = input()
    dificil = False
    per = len(sobrenome) - 2
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for j in range(per):
        if sobrenome[j] not in vogais:
            if sobrenome [j+1] not in vogais:
                if sobrenome [j+2] not in vogais:
                    dificil = True
    if dificil:
        print(f'{sobrenome} nao eh facil')
    else:
        print(f'{sobrenome} eh facil')