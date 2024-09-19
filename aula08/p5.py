def ordemCrescente(vetor):
    if len(vetor) <= 1:
        return True
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True

entrada = input("Informe os números separados por espaço: ")
vetor = [int(numero) for numero in entrada.split()]

if ordemCrescente(vetor):
    print("O vetor está ordenado em ordem crescente.")
else:
    print("O vetor não está ordenado em ordem crescente.")