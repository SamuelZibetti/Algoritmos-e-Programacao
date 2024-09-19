# Error: Time limit exceeded
# Descrição: Foi sugerido a implementação de um EOF para resolver o problema, mas o mesmo persistiu.

uni = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dez = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
cen = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa", "cem"]
cen2 = ["cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

while True:
    try:
        n = int(input())
        flag = 0
        
        if n == 0:
            print("zero")
        else:
            if n >= 10000:
                flag = 1
            
            if n >= 100000:
                if n <= 100999:
                    print("cem", end=" ")
                    n -= 100000
                else:
                    print(cen2[n // 100000 - 1], end=" ")
                n %= 100000
                if n == 0:
                    print("mil")
                    continue
                elif n < 1000:
                    if n % 100 and n > 100:
                        print("mil", end=" ")
                    else:
                        print("mil e ", end="")
                else:
                    print("e ", end="")
            
            if n >= 20000:
                print(cen[n // 10000 - 2], end=" ")
                n %= 10000
                if n == 0:
                    print("mil")
                    continue
                elif n < 1000:
                    if n % 100 and n > 100:
                        print("mil", end=" ")
                    else:
                        print("mil e ", end="")
                else:
                    print("e ", end="")
            
            if n >= 10000:
                print(dez[(n // 1000) % 10], end=" ")
                n %= 1000
                if n == 0:
                    print("mil")
                    continue
                elif n < 1000 and n:
                    if n % 100 and n > 100:
                        print("mil", end=" ")
                    else:
                        print("mil e ", end="")
                else:
                    print("e ", end="")
            
            if n >= 1000:
                if n >= 2000 or flag:
                    print(uni[n // 1000], end=" ")
                if n % 1000 == 0:
                    print("mil")
                n %= 1000
                if n == 0:
                    print()
                elif n < 100 or (n < 1000 and n % 100 == 0):
                    print("mil e ", end="")
                else:
                    print("mil ", end="")
            
            if n >= 100:
                if n == 100:
                    print("cem", end=" ")
                else:
                    print(cen2[n // 100 - 1], end=" ")
                n %= 100
                if n == 0:
                    print()
                else:
                    print("e ", end="")
            
            if n >= 20:
                print(cen[n // 10 - 2], end=" ")
                n %= 10
                if n == 0:
                    print()
                else:
                    print("e ", end="")
            
            if n >= 10:
                print(dez[n % 10])
                n = 0
            
            if 0 < n < 10:
                print(uni[n])
        print()
    
    except EOFError:
        break