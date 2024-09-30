custo = float(200.00)
v_ingresso = float(5.00)
ingressos = 120
lucro_maximo = 0


while v_ingresso > 1.00:

    lucro = (v_ingresso * ingressos) - custo

    if(lucro > lucro_maximo):

        lucro_maximo = lucro
        valor = v_ingresso
        quantidade = ingressos

    print(f'Preço Ingresso: {v_ingresso:.2f}, Quantidade: {ingressos}, Lucro: {lucro:.2f}')

    ingressos = ingressos + 26

    v_ingresso = v_ingresso - 0.5

print(f'\nLucro máximo: {lucro_maximo:.2f}')
print(f'Preço de ingresso: {valor:.2f}')
print('Quantidade vendida: ', quantidade)

