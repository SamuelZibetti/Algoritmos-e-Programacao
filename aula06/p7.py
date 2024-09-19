respostas = []

pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

respostas.extend([pergunta1, pergunta2, pergunta3, pergunta4, pergunta5])

positivas = respostas.count("sim")

if positivas == 2:
    print("Você é suspeito.")
elif positivas >= 3 and positivas <= 4:
    print("Você é cúmplice.")
elif positivas == 5:
    print("Você é o assassino.")
else:
    print("Você é inocente.")