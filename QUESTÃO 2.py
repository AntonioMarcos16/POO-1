while True:   

    def iterativo(valor):

        count = valor - 1

        while count >= 1:

            valor = valor * count
            count = count - 1

        return valor

    def recursivo(valor):

        if(valor == 0):
            
            return 1
        
        return valor * recursivo(valor - 1)

    
    print('1 - Iterativo.')
    print('2 - Recursivo.')
    print('3 - Sair.')
    op = int(input('Informe a forma que deseja calcular: '))

    if(op == 1):
        print('Você escolheu a forma iterativa.')

        valor = int(input('Informe um numero: '))

        fator = iterativo(valor)

        break

    elif(op == 2):
        print('Você escolheu a forma recursiva.')

        valor = int(input('Informe um numero: '))

        fator = recursivo(valor)

        break

    elif(op == 3):

        print('Saindo do programa...')

        break

    else:
        print('Informe uma opção valida.')

print('Essa e a fatorial desse valor: ', fator)