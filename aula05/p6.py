count = 0
valor = 0

while valor <= 100:
    count += 1
    valorNovo = int(input(f"Informe o {count}º valor: "))
    valor += valorNovo
    
print(f"Para alcançar uma soma maior que 100 foram precisos {count} números.")  