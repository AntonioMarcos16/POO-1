while True:
    print('1 - Triangulo.')
    print('2 - Circulo.')
    print('3 - Quadrado.')
    print('4 - Sair.')
    objeto = int(input('Informe a forma do objeto: '))

    if(objeto == 1):
        
        base = int(input('Informe a base do triangulo: '))
        altura = int(input('Informe a altura do triangulo: '))

        area = base * altura

        print('Essa é a area do Triangulo: ', area / 2)

    elif(objeto == 2):

        raio = int(input('Informe o raio do circulo: '))

        pi = 3.14

        area = raio * raio

        print('Esta é a area do Circulo: ', area * pi)

    elif(objeto == 3):

        lado = int(input('Informe o valor do lado do quadrado: '))

        area = lado * lado

        print('Esta é a area do Quadrado: ', area)

    elif(objeto == 4):
        break

    else:
        print('Informe uma opção valida.\n')