lista ={
11 : 'x',
12 : 'o',
13 : 'x',
21 : 'x',
22 : 'x',
23 : 'x',
31 : 'x',
32 : 'x',
33 : 'x',
}
jogada_antiga = jogada_nova =12
print('''
{}{}{}
{}{}{}
{}{}{}'''.format(lista[31], lista[32], lista[33], lista[21], lista[22], lista[23], lista[11], lista[12],
                     lista[13], ))
while True:
    joga = input('Jogada: ')
    if joga == 'a' and jogada_antiga - 1 != 10 and jogada_antiga - 1 != 20 and jogada_antiga - 1 != 30:
        if jogada_antiga - 1 >= 11:
            jogada_antiga -= 1
        elif jogada_antiga - 1 >= 21:
            jogada_antiga -= 1
        elif jogada_antiga - 1 >= 31:
            jogada_antiga -= 1
    if joga == 'd' and jogada_antiga + 1 != 14 and jogada_antiga + 1 != 24 and jogada_antiga + 1 != 34:
        if jogada_antiga +1 <= 13:
            jogada_antiga += 1
        elif jogada_antiga +1 <= 23:
            jogada_antiga += 1
        elif jogada_antiga +1 <= 33:
            jogada_antiga += 1
    if joga == 's':
        jogada_antiga -= 10
    if joga == 'w':
        jogada_antiga += 10

    for c in lista:
        lista[c] = 'x'
    for c in lista:
        if c == jogada_antiga:
            lista[c] = 'o'
    print('''
{}{}{}
{}{}{}
{}{}{}'''.format(lista[31], lista[32], lista[33], lista[21], lista[22], lista[23], lista[11], lista[12], lista[13], ))