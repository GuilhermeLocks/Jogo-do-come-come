tabuleiro = []
posicao = []
for c in range(1, 9):
    for v in range(1, 9):
        posicao.append('x')
        posicao.append(c)
        posicao.append(v)
        tabuleiro.append(posicao[:])
        posicao.clear()
for c in tabuleiro:
    print(c)

