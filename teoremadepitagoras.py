def conta():
    resposta = input('Você tem o valor dos dois catetos? (s para sim e n para não) (s/n)')
    if resposta == 's':
        def conta2():
            try:
                cateto1 = int(input('Informe qual o valor do primeiro cateto: '))
                cateto2 = int(input('Informe qual o valor do segundo cateto: '))
                print(f'O valor da hipotenusa é: {((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5}')
            except Exception:
                print('Valor inválido!(Opss, parece que você não digitou números inteiros, tente outra vez)')
                conta2()
        conta2()
    elif resposta == 'n':
        def conta3():
            try:
                cateto1 = int(input('Informe qual o valor do cateto: '))
                hipotenusa = int(input('Informe qual o valor da hipotenusa: '))
                print(f'O valor do cateto é de: {((hipotenusa ** 2) - (cateto1 ** 2)) ** 0.5}')
            except Exception:
                print('Valor inválido!(Escreva apenas números inteiros)')
                conta3()
        conta3()
    else:
        print('Resposta inválida!')
        conta()

conta()
while True:
    resposta2 = input('Deseja recomeçar a conta?? ')
    if resposta2 == 's':
        conta()
    elif resposta2 == 'n':
        print('Fim! :)')
        break
    else:
        print('Resposta inválida!')