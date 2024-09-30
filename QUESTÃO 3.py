while True:

    def fatorial(a, b):
        valor1 = a
        valor2 = a - b
        
        count = valor1 - 1
        count2 = valor2 - 1

        while count >= 1:

            valor1 = valor1 * count
            count = count - 1

        while count2 >= 1:

            valor2 = valor2 * count2
            count2 = count2 - 1

        arranjo = valor1 / valor2

        return arranjo

    def fatorial2(a, b):
        valor1 = a
        valor2 = a - b
        valor3 = b

        count = valor1 - 1
        count2 = valor2 - 1
        count3 = valor3 - 1

        while count >= 1:

            valor1 = valor1 * count
            count = count - 1

        while count2 >= 1:

            valor2 = valor2 * count2
            count2 = count2 - 1
            

        while count3 > 1:

            valor3 = valor3 * count3
            count3 = count3 - 1

        sub_comb = valor3 * valor2

        combinacao = valor1 / sub_comb

        return combinacao

    print('1 - Arranjo.')
    print('2 - Combinação.')
    print('3 - Todos.')
    print('4 - Sair.')

    op = int(input('Informe a opção desejada: '))

    if(op == 1):
        print('Você optou por ver o arranjo.')

        a = int(input('Informe o valor A para este arranjo: '))
        b = int(input('Informe o valor B para este arranjo: '))

        arranjo = fatorial(a, b)

        print('Esse é o arranjo destes numeros: ', arranjo)

    elif(op == 2):
        print('Você optou por ver a combinação.')

        a = int(input('Informe o valor A para esta combinação: '))
        b = int(input('Informe o valor B para esta combinação: '))

        combinacao = fatorial2(a, b)

        print('Essa é a combinação destes numeros: ', combinacao)

    elif(op == 3):
        print('Você optou por ver arranjo e combinação.')

        a = int(input('Informe o valor de A para Arranjo e Combinação de numeros: '))
        b = int(input('Informe o valor de B para Arranjo e Combinação de numeros: '))

        arranjo = fatorial(a, b)
        combinacao = fatorial2(a, b)

        print('Esse é o arranjo destes numeros: ', arranjo)
        print('Essa é a combinação destes numeros: ', combinacao)

    elif(op == 4):
        print('Saindo, até breve...')

        break

    else:
        print('Informe uma opção valida.')