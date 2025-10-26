jogo = [

['x', 5, 1], ['x', 5, 2], ['x', 5, 3], ['x', 5, 4], ['x', 5, 5], ['x', 5, 6], ['x', 5, 7], ['x', 5, 8], ['x', 5, 9], ['x', 5, 10], ['x', 5, 11],
['x', 4, 1], ['x', 4, 2], ['x', 4, 3], ['x', 4, 4], ['x', 4, 5], ['x', 4, 6], ['x', 4, 7], ['x', 4, 8], ['x', 4, 9], ['x', 4, 10], ['x', 4, 11],
['x', 3, 1], ['x', 3, 2], ['x', 3, 3], ['x', 3, 4], ['x', 3, 5], ['x', 3, 6], ['x', 3, 7], ['x', 3, 8], ['x', 3, 9], ['x', 3, 10], ['x', 3, 11],
['x', 2, 1], ['x', 2, 2], ['x', 2, 3], ['x', 2, 4], ['x', 2, 5], ['x', 2, 6], ['x', 2, 7], ['x', 2, 8], ['x', 2, 9], ['x', 2, 10], ['x', 2, 11],
['x', 1, 1], ['x', 1, 2], ['x', 1, 3], ['x', 1, 4], ['x', 1, 5], ['x', 1, 6], ['x', 1, 7], ['x', 1, 8], ['x', 1, 9], ['x', 1, 10], ['x', 1, 11],
]

POSIÇÃO_ANTIGA = 0
for c in jogo:
    if c[1] != POSIÇÃO_ANTIGA:
        print()
        POSIÇÃO_ANTIGA = c[1]
    if c[0] == 'o':
        print('\033[34m', end='')
    if c[0] == 'x':
        print('\033[35m', end='')
    print(c[0], end='')
print('')

largura = 3
altura = 8
fundo = 'k'
jogo = list()
parte = list()
for c in range(largura, 0, -1):
    for v in range(1, altura+1):
        parte.append(fundo)
        parte.append(c)
        parte.append(v)
        jogo.append(parte[:])
        parte.clear()
for c in jogo:
    if c[1] != POSIÇÃO_ANTIGA:
        print()
        POSIÇÃO_ANTIGA = c[1]
    if c[0] == 'o':
        print('\033[34m', end='')
    if c[0] == 'x':
        print('\033[35m', end='')
    print(c, end='')
print('')
print(jogo[altura*(largura-1)])