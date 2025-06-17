tabuleiro = [['x', 3, 1], ['x', 3, 2], ['x', 3, 3],
             ['x', 2, 1], ['x', 2, 2], ['x', 2, 3],
             ['x', 1, 1], ['x', 1, 2], ['x', 1, 3],]
velho = 3
for c in tabuleiro:
    if velho < c[1]:
        print('\n')
    velho = c[1]
    print(c, end='')
    print('velho = ', velho)

