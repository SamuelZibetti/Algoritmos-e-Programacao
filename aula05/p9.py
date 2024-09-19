soma = 0
count = 0

while True:
    numero = float(input("Informe um número (ou digite 0 para encerrar): "))
    
    if numero == 0:
        break
    
    soma += numero
    count += 1

if count > 0:
    media = soma / count
    print(f"Foram informados {count} números.")
    print(f"A média aritmética dos números é {media:.2f}")
else:
    print("Nenhum número foi informado.")