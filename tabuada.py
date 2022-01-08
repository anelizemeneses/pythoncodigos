tabuada = int(input("digite um numero para exibir a tabuada: "))
print("tabuada do número ", tabuada)
for valor in range(1, 11, 1):
    print(str(tabuada) + ' x ' + str(valor) + ' = ' + str((tabuada * valor)))