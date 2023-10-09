nome = input ("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de xp do herói: "))

if (xp <= 1000):
    print (f"O Herói de nome {nome} está no nível de Ferro")
elif (xp >= 1001 and xp <= 2000):
    print (f"O Herói de nome {nome} está no nível de Bronze")
elif (xp >= 2001 and xp <= 5000):
    print (f"O Herói de nome {nome} está no nível de Prata")
elif (xp >= 5001 and xp <= 7000):
    print (f"O Herói de nome {nome} está no nível de Ouro")   
elif (xp >= 7001 and xp <= 8000):
    print (f"O Herói de nome {nome} está no nível de Platina")
elif (xp >= 8001 and xp <= 9000):
    print (f"O Herói de nome {nome} está no nível de Bronze")
elif (xp >= 9001 and xp <= 10000):
    print (f"O Herói de nome {nome} está no nível de Bronze")
else:
    print (f"O Herói de nome {nome} está no nível de Radiante")   




