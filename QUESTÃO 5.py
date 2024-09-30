def binarios(valor):

    if(valor == 0):
        
        return '0'

    restos = ''

    while valor > 0:

        resto = valor % 2

        restos = str(resto) + restos

        valor = valor // 2

    return restos

valor = int(input('Informe o valor decimal: '))

v_binario = binarios(valor)

print(f'O valor binario de {valor}, é {v_binario}')