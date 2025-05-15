import pygame
from pygame.locals import *
from sys import exit
pygame.init()

altura  = 480
largura = 640
moeda = 0
valor = 1
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo Clicker')

while True:
    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (0,255,0), (200, 300, 40, 50))
    pygame.display.update()

    acao = input('{}'.format(moeda)).upper()

    if acao == '':
        moeda += valor

    if acao == 'L':
        compra = input('''
    [1] +2 moeda=10
    [2] +5 moeda=1000
    [3] s para sair''')

    if compra == '1' and moeda >= 10:
        moeda -= 10
        valor += 1
        compra = ''

    if compra == '2' and moeda >= 1000:
        moeda -= 1000
        valor += 5
        compra = ''
