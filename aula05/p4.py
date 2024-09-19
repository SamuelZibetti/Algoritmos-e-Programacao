primos = []

for num in range(2, 1001):
    conclusao = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            conclusao = False
            break
    if conclusao:
        primos.append(num)

print(primos)