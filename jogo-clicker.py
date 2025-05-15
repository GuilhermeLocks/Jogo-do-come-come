print('Digite L para loja ou enter para moeda.')
moeda = 0
valor = 1
compra = ''
while True:
    acao = input('{}'.format(moeda)).upper()

    if acao == '':
        moeda += valor

    if acao == 'L':
        compra = input('''
[1] +2 moeda=10
[2] +5 moeda=1000
[3] s para sair''')

    if compra == '1' and moeda>=10:
        moeda -= 10
        valor += 1
        compra = ''

    if compra == '2' and moeda>=1000:
        moeda -= 1000
        valor += 5
        compra = ''
