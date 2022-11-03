import pygame
from os import path
import sys

def construir(jogo, lista):
    print("ola")
    contorno = pygame.image.load(path.join('sistema', 'contorno1.png'))
    #teste so pra colocar elevadores fingindo brincadeira
    #while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    contagem = 0
    while contagem < 147:
        if lista[contagem].pretendente == "total" or lista[contagem].pretendente == "vertical": jogo.janela.blit(contorno,lista[contagem].coordenadas)
        contagem += 1

    #pygame.display.flip()

#animacao ficar aqui?


def minerar(jogo, celula):        #n seria bom mandar so o objeto?

    confirmacao = pygame.image.load(path.join('sistema', 'removerpedra.png'))
    contorno = pygame.image.load(path.join('sistema', 'contorno1.png'))
    erro  = pygame.image.load(path.join('sistema', 'naopode.png'))

    jogo.janela.blit(contorno, celula.coordenadas)
    jogo.janela.blit(confirmacao,(459,186))
    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                if pos_y >= 372 and pos_y <= 465:
                    if pos_x >= 510 and pos_x <= 560:
                        return
                    elif pos_x >= 612 and pos_x <= 663:
                        preco = (((celula.id-1) // 21) * 50) + 50
                        if jogo.dinheiro < preco:
                            jogo.janela.blit(erro,(459,186))
                            pygame.display.flip()
                        else:
                            celula.pedra = False
                            jogo.dinheiro = jogo.dinheiro - preco
                            return
            

        

def achar_celula(position):

    pos_x, pos_y = position
    x = 1020
    y = 558
    achei = False
    while achei == False:
        if pos_y < y: y -= 93
        else: achei = True
    achei = False
    while achei == False:
        if pos_x < x: x -= 51
        else: achei = True
    y = (y // 93) * 21
    x = (x//51) + 1
    pos_vetor = (x + y) - 1
    return pos_vetor




def pretendencia(lista, pos_vetor, demolicao):

    if demolicao == True:   #se isso for verdade, quer dizer que uma celula foi demolida

        #se vier ide, so diminuir 1 pra ter o pos_vetor
        if lista[pos_vetor].pedra == True or lista[pos_vetor].vazio == False: return
        a = ((pos_vetor) // 21) #representa o i na matriz
        b = (pos_vetor) % 21 #representa o j na matriz
        

        lista[pos_vetor].pretendente = None
        if a != 0:
            if lista[pos_vetor-21].vazio == False: lista[pos_vetor].pretendente = "elevador"
        if a != 6:
            if lista[pos_vetor+21].vazio == False: lista[pos_vetor].pretendente = "elevador"
        if b != 0:
            if lista[pos_vetor-1].vazio == False: lista[pos_vetor].pretendente = "total"
        if b != 20:
            if lista[pos_vetor+1].vazio == False: lista[pos_vetor].pretendente = "total"
    

    else:
        print("plim")
        if lista[pos_vetor].vazio == False:
            a = ((pos_vetor) // 21) #representa o i na matriz
            b = (pos_vetor) % 21 #representa o j na matriz

            if a != 0:
                if lista[pos_vetor-21].vazio == True and lista[pos_vetor-21].pedra == False:
                    if lista[pos_vetor].tipo == "elevador": lista[pos_vetor-21].pretendente == "vertical"
            if a != 6:
                if lista[pos_vetor+21].vazio == True and lista[pos_vetor+21].pedra == False:
                    if lista[pos_vetor].tipo == "elevador": lista[pos_vetor+21].pretendente == "vertical"
            if b != 0:
                if lista[pos_vetor-1].vazio == True and lista[pos_vetor-1].pedra == False: lista[pos_vetor-1].pretendente == "total"
            if b != 20:
                if lista[pos_vetor+1].vazio == True and lista[pos_vetor+1].pedra == False: lista[pos_vetor+1].pretendente == "total"


def buildar(celula,tipo):

    if tipo == "elevador":
        celula.vazio = False
        celula.pretendente = False
        celula.tipo = "elevador"
        celula.lvl = "0"
        celula.situacao = "_1-1"
        celula.consumo = 20
