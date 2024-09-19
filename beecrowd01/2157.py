c = int(input())

for i in range(c):
    a, b = map(int, input().split())
    resposta = ""
    for j in range(a, b+1):
        resposta += str(j)
    resposta += resposta[::-1]
    
    print(resposta)