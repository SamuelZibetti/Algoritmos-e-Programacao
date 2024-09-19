temperaturas = []
total = 0.0

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

for mes in range(1, 13):
    temperatura = float(input(f"Informe a temperatura média de {meses[mes]}: "))
    total = total + temperatura
    temperaturas.append(temperatura)
    
mediaAnual = total / 12

print(f"Meses com a temperatura acima da média anual {mediaAnual:.2f} °C")

for mes, temperatura in enumerate (temperaturas, start = 1):
    if temperatura > mediaAnual:
        print(f"{meses[mes]} - {temperatura:.2f} °C")  