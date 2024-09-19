def formatarData(data):
    if len(data) != 10:
        return None
    dia, mes, ano = map(int, data.split('/'))
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril',
        'maio', 'junho', 'julho', 'agosto',
        'setembro', 'outubro', 'novembro', 'dezembro'  
    ]
    
    if dia < 1 or dia > 31 or mes < 1 or mes > 12:
        return None
    dataFormatada = f"{dia} de {meses[mes-1]} de {ano}"
    return dataFormatada

data = input("Informe uma data: ")
dataFormatada = formatarData(data)
if dataFormatada != None:
    print(dataFormatada)
else:
    print("Data inválida!")