import random
largura = 8
altura = 4
fundo = 'x'
objetivo = '*'
jogador = '!'
jogo = list()
parte = list()

for c in range(altura, 0, -1):
    for v in range(1, largura+1):
        parte.append(fundo)
        parte.append(c)
        parte.append(v)
        jogo.append(parte[:])
        parte.clear()

premio = [f'\033[34m{objetivo}\033[35m', random.randint(1, altura), random.randint(1, largura)]

for c in jogo:
    if premio[1] == c[1] and premio[2] == c[2]:
        c[0] = premio[0]

maximo = ['x', altura, largura]
minimo = ['x', 1, 1]
POSIÇÃO_ANTIGA = 0
pontos = 0
jogo[largura*(altura-1)][0] = jogador
POSIÇÃO_ATUAL = ['x', 1, 1]

while pontos != 10:
    '\033[m'
    if POSIÇÃO_ATUAL[1] == premio[1] and POSIÇÃO_ATUAL[2] == premio[2]:
        pontos += 1
    '\033[34m'

    for c in jogo:
        if premio[1] == c[1] and premio[2] == c[2]:
            if c[0] == 'x':
                premio = [f'\033[34m{objetivo}\033[35m', random.randint(1, altura), random.randint(1, largura)]
                for c in jogo:
                    if premio[1] == c[1] and premio[2] == c[2]:
                        c[0] = premio[0]
    for c in jogo:
        if c[1] == POSIÇÃO_ATUAL[1] and c[2] == POSIÇÃO_ATUAL[2]:
            c[0] = jogador

    for c in jogo:
        if c[1] != POSIÇÃO_ANTIGA:
            print()
            POSIÇÃO_ANTIGA = c[1]
        if c[0] == jogador:
            print('\033[34m', end='')
        if c[0] == 'x':
            print('\033[35m', end='')
        print(c[0], end='')

    print('')

    jogada = input('\n\033[34mMoedas: {}\nJogada: \033[m'.format(pontos)).upper()

    if jogada == 'W' and POSIÇÃO_ATUAL[1]+1 <= maximo[1]:
        POSIÇÃO_ATUAL[1] += 1
        for c in jogo:
            if c[0] == jogador:
                c[0] = 'x'

    if jogada == 'S' and POSIÇÃO_ATUAL[1]-1 >= minimo[1]:
        POSIÇÃO_ATUAL[1] -= 1
        for c in jogo:
            if c[0] == jogador:
                c[0] = 'x'

    if jogada == 'D' and POSIÇÃO_ATUAL[2]+1 <= maximo[2]:
        POSIÇÃO_ATUAL[2] += 1
        for c in jogo:
            if c[0] == jogador:
                c[0] = 'x'

    if jogada == 'A' and POSIÇÃO_ATUAL[2]-1 >= minimo[2]:
        POSIÇÃO_ATUAL[2] -= 1
        for c in jogo:
            if c[0] == jogador:
                c[0] = 'x'