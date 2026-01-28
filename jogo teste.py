import msvcrt
import os

ouro = 0
vezes = 1

while True:

    if msvcrt.kbhit():  # Verifica se uma tecla foi pressionada
        key = msvcrt.getch().decode('utf-8')  # Lê a tecla e decodificaqqq

        if key == 'q':
            ouro += vezes
            os.system('cls')
            print(ouro)

        if key == '2' and ouro >= 20:
            vezes *= 2
            ouro -= 20
            os.system('cls')
            print(ouro)

        if key == '3' and ouro >= 30:
            vezes *= 3
            ouro -= 30
            os.system('cls')
            print(ouro)

        if key == '4' and ouro >= 40:
            vezes *= 400
            ouro -= 40
            os.system('cls')
            print(ouro)

        if key == '0':
            ouro = 0
            os.system('cls')
            print(ouro)


