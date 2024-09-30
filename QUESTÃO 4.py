while True:
    def primo(valor):
    
        if valor <= 1:
            
            return False
        
        for i in range(2, valor):
            
            if valor % i== 0:
                return False
            
        return True
    
    print('1 - Unico Valor')
    print('2 - Intervalo de Valores')
    print('3 - Sair')

    op = int(input('Informe a opção desejada: '))

    if(op == 1):
        print('Você optou por ver um unico valor.')

        valor = int(input("Informe um valor: "))

        if primo(valor):
            print(f"{valor} é primo.")

        else:
            print(f"{valor} não é primo.")

    elif(op == 2):
        print('Você optou por ver intervalo de valores.')

        a = int(input("Informe o primeiro valor: "))
        b = int(input("Informe o segundo valor: "))

        for valor in range(a, b + 1):

            if valor > 1:  
                eh_primo = True

                for i in range(2, valor): 

                    if valor % i == 0:
                        eh_primo = False
                        break

                if eh_primo:
                    print(valor)

    elif(op == 3):
        print('Até Breve...')

        break

    else:
        print('Escolha uma opção valida.')