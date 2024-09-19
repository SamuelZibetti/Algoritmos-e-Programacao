codigo = int(input("Informe o código do pedido: "))
quantidade = int(input("Informe a quantidade do pedido: "))

count = 0

if codigo == 10:
    preco = quantidade * 1.10
    count = quantidade
    lanche = "Cachorro-quente"
elif codigo == 11:
    preco = quantidade * 1.30
    count = quantidade
    lanche = "Bauru simples"
elif codigo == 12:
    preco = quantidade * 1.50
    count = quantidade
    lanche = "Bauru com ovo"
elif codigo == 13:
    preco = quantidade * 1.10
    count = quantidade
    lanche = "Hamburguer"
elif codigo == 14:
    preco = quantidade * 1.30
    count = quantidade
    lanche = "Cheeseburger"
else:
    preco = quantidade * 1.50
    count = quantidade
    lanche = "Refrigerante"

print(f"O cliente pediu {count} {lanche} pelo valor de R${preco:.2f}")