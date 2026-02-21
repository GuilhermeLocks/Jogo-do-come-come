from random import randint

tentativa = 0
while True:
    numero = randint(1, 100)
    if numero == 100:
        print(numero)
        break
    else:
        tentativa += 1
        print(numero)