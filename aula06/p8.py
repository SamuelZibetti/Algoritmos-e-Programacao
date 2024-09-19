saltos = []
total = 0

atleta = input("Informe o nome do atleta (deixe em branco para encerrar o programa): ")

while atleta != "":
    for i in range(1, 6):
        salto = float(input(f"{i}º salto: "))
        total = total + salto
        saltos.append(salto)
        
    media = total / 5
        
    print("Resultado Final:")
    print(f"Atleta: {atleta}")
    print(f"Saltos: {' - '.join(map(str, saltos))}")
    print(f"Média dos saltos: {media:.1f} m")

    saltos = []
    total = 0
    atleta = input("Informe o nome do atleta (deixe em branco para encerrar o programa): ")