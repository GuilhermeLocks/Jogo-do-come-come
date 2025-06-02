import random
jogo = [
['x', 5, 1], ['x', 5, 2], ['x', 5, 3], ['x', 5, 4], ['x', 5, 5], ['x', 5, 6], ['x', 5, 7], ['x', 5, 8], ['x', 5, 9], ['x', 5, 10], ['x', 5, 11],
['x', 4, 1], ['x', 4, 2], ['x', 4, 3], ['x', 4, 4], ['x', 4, 5], ['x', 4, 6], ['x', 4, 7], ['x', 4, 8], ['x', 4, 9], ['x', 4, 10], ['x', 4, 11],
['x', 3, 1], ['x', 3, 2], ['x', 3, 3], ['x', 3, 4], ['x', 3, 5], ['x', 3, 6], ['x', 3, 7], ['x', 3, 8], ['x', 3, 9], ['x', 3, 10], ['x', 3, 11],
['x', 2, 1], ['x', 2, 2], ['x', 2, 3], ['x', 2, 4], ['x', 2, 5], ['x', 2, 6], ['x', 2, 7], ['x', 2, 8], ['x', 2, 9], ['x', 2, 10], ['x', 2, 11],
['x', 1, 1], ['x', 1, 2], ['x', 1, 3], ['x', 1, 4], ['x', 1, 5], ['x', 1, 6], ['x', 1, 7], ['x', 1, 8], ['x', 1, 9], ['x', 1, 10], ['x', 1, 11],
]
premio = ['*', random.randint(1, 5), random.randint(1, 11)]
for c in jogo:
    if premio[1] == c[1] and premio[2] == c[2]:
        c[0] = premio[0]
maximo = ['o', 5, 11]
minimo = ['o', 1, 1]
POSIÇÃO_ANTIGA = 0
pontos = 0
POSIÇÃO_ATUAL = ['o', 1, 1]
jogo[44][0] = 'o'

for c in jogo:
    if c[1] != POSIÇÃO_ANTIGA:
        print('OI')
        POSIÇÃO_ANTIGA = c[1]
    print(c[0], end='')
print()




while True:
    if POSIÇÃO_ATUAL[1] == premio[1] and POSIÇÃO_ATUAL[2] == premio[2]:
        pontos +=1
    for c in jogo:
        if premio[1] == c[1] and premio[2] == c[2]:
            if c[0] == 'x':
                premio = ['*', random.randint(1, 5), random.randint(1, 11)]
                for c in jogo:
                    if premio[1] == c[1] and premio[2] == c[2]:
                        c[0] = premio[0]
    jogada = input('\nPontuação: {} Jogada: '.format(pontos)).upper()


    if jogada == 'W' and POSIÇÃO_ATUAL[1]+1 <= maximo[1]:
        POSIÇÃO_ATUAL[1] += 1
        for c in jogo:
            if c[0] == 'o':
                c[0] = 'x'
    if jogada == 'S' and POSIÇÃO_ATUAL[1]-1 >= minimo[1]:
        POSIÇÃO_ATUAL[1] -= 1
        for c in jogo:
            if c[0] == 'o':
                c[0] = 'x'
    if jogada == 'D' and POSIÇÃO_ATUAL[2]+1 <= maximo[2]:
        POSIÇÃO_ATUAL[2] += 1
        for c in jogo:
            if c[0] == 'o':
                c[0] = 'x'
    if jogada == 'A' and POSIÇÃO_ATUAL[2]-1 >= minimo[2]:
        POSIÇÃO_ATUAL[2] -= 1
        for c in jogo:
            if c[0] == 'o':
                c[0] = 'x'

    for c in jogo:
        if c[1] == POSIÇÃO_ATUAL[1] and c[2] == POSIÇÃO_ATUAL[2]:
            c[0] = 'o'

    for c in jogo:
        if c[1] != POSIÇÃO_ANTIGA:
            print()
            POSIÇÃO_ANTIGA = c[1]
        print(c[0], end='')