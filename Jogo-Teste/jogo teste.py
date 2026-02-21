import msvcrt
import os

ouro = 0
vezes = 1

def mostrar_ouro():
    os.system('cls')
    print(ouro)

def comprar(v, o):
    global vezes
    global ouro
    vezes *= v
    ouro -= o

while True:

    if msvcrt.kbhit():  # Verifica se uma tecla foi pressionada
        key = msvcrt.getch().decode('utf-8')  # Lê a tecla e decodificaqqq

        if key == 'q':
            ouro += vezes
            mostrar_ouro()

        if key == '2' and ouro >= 20:
            comprar(2, 20)
            mostrar_ouro()

        if key == '3' and ouro >= 30:
            comprar(3, 30)
            mostrar_ouro()

        if key == '4' and ouro >= 40:
            comprar(4, 40)
            mostrar_ouro()

        if key == '0':
            ouro = 0
            vezes = 0
            mostrar_ouro()


