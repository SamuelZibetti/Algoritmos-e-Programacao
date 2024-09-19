def converterHorario(hora, minutos):
    if hora < 0 or hora > 23 or minutos < 0 or minutos > 59:
        return "Horário inválido!"
    
    if hora < 12:
        periodo = "A.M."
        if hora == 0:
            hora = 12
    else:
        periodo = "P.M."
        if hora > 12:
            hora -= 12
            
    return f"{hora}:{minutos:02d} {periodo}"
            
hora = int(input("Informe a hora: "))
minutos = int(input("Informe os minutos: "))
resultado = converterHorario(hora, minutos)
print(resultado)