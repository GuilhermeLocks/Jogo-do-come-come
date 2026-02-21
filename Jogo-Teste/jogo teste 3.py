from random import randint

numero_a_ser_adivinhado = randint(1, 100)
numero_chute = randint(1, 100)
numero_para_adicionar = numero_para_diminuir = 0
tentativas = 0

while True:
    if numero_chute == numero_a_ser_adivinhado:
        if tentativas == 0:
            print('Acertou de primeira!')
            break
        else:
            print(f'Voce a certou na {tentativas} tentativa! {numero_chute} {numero_a_ser_adivinhado}')
            break
    elif numero_chute < numero_a_ser_adivinhado:
        print(f'Muito baixo tente novamente! {numero_chute:<5} {numero_a_ser_adivinhado:<5}')
        while True:
            print(numero_chute, numero_a_ser_adivinhado, numero_para_adicionar, numero_para_diminuir)
            numero_para_adicionar = randint(1, 100)
            if numero_chute + numero_para_adicionar <= 100:
                numero_chute += numero_para_adicionar
                tentativas += 1
                break
    elif numero_chute > numero_a_ser_adivinhado:
        print(f'Muito alto  tente novamente! {numero_chute:<5} {numero_a_ser_adivinhado:<5}')
        while True:
            numero_para_diminuir = randint(1,100)
            if numero_chute - numero_para_diminuir >=0:
                numero_chute -= numero_para_diminuir
                tentativas +=1
                break