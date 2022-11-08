import pygame
from pygame import mixer
mixer.init()
pygame.init()

from os import path
import sys


def animacao(jogo, lista, flipar):

    preto = 0, 0, 0
    jogo.janela.fill(preto)
    jogo.janela.blit(jogo.fundo, (0,0))
    jogo.janela.blit(jogo.iconesistema, (0,0))

    if jogo.modo == "construir":
        contorno1 = pygame.image.load(path.join('sistema', 'constrorno1.png'))

    contagem = 0
    while contagem < 147:
        lista[contagem].imagem()    #sera se tem problema atualizar toda santa vez as imagens?
        if lista[contagem].obj != None:
            jogo.janela.blit(lista[contagem].obj,lista[contagem].coordenadas)

        if jogo.modo == "construir":
            if jogo.construirtipo == "elevador":
                if lista[contagem].pretendente == "total" or lista[contagem].pretendente == "vertical": 
                    jogo.janela.blit(contorno1,lista[contagem].coordenadas)

        contagem += 1

    if flipar == True: pygame.display.flip()


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
                            sucesso =  pygame.mixer.Sound(path.join('sons','minerar.wav'))
                            pygame.mixer.Sound.play(sucesso)
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
        if lista[pos_vetor].pedra or not lista[pos_vetor].vazio: return
        a = ((pos_vetor) // 21) #representa o i na matriz
        b = (pos_vetor) % 21 #representa o j na matriz
        

        lista[pos_vetor].pretendente = None
        if a != 0:
            if not lista[pos_vetor-21].vazio and lista[pos_vetor-21].tipo == "elevador": lista[pos_vetor].pretendente = "vertical"
        if a != 6:
            if not lista[pos_vetor+21].vazio and lista[pos_vetor+21].tipo == "elevador": lista[pos_vetor].pretendente = "vertical"
        if b != 0:
            if lista[pos_vetor-1].vazio == False: lista[pos_vetor].pretendente = "total"
        if b != 20:
            if lista[pos_vetor+1].vazio == False: lista[pos_vetor].pretendente = "total"
    

    else:
        #print("plim")
        if lista[pos_vetor].vazio == False:
            a = ((pos_vetor) // 21) #representa o i na matriz
            b = (pos_vetor) % 21 #representa o j na matriz

            if a != 0:
                if lista[pos_vetor-21].vazio == True and lista[pos_vetor-21].pedra == False:
                    if lista[pos_vetor].tipo == "elevador": lista[pos_vetor-21].pretendente = "vertical"
            if a != 6:
                if lista[pos_vetor+21].vazio == True and lista[pos_vetor+21].pedra == False:
                    if lista[pos_vetor].tipo == "elevador": lista[pos_vetor+21].pretendente = "vertical"
            if b != 0:
                if lista[pos_vetor-1].vazio == True and lista[pos_vetor-1].pedra == False: lista[pos_vetor-1].pretendente = "total"
            if b != 20:
                if lista[pos_vetor+1].vazio == True and lista[pos_vetor+1].pedra == False: lista[pos_vetor+1].pretendente = "total"



def erguer(lista, pos_vetor, jogo):

    #essa funcao tbm tem obrigacao de fundir salas

    if jogo.construirtipo == "elevador":
        lista[pos_vetor].vazio = False
        lista[pos_vetor].pretendente = False
        lista[pos_vetor].tipo = "elevador"
        lista[pos_vetor].lvl = "0"
        lista[pos_vetor].situacao = "_1-1"
        lista[pos_vetor].consumo = 20
        jogo.dinheiro -= jogo.sobresalas.precoatual

    sucesso =  pygame.mixer.Sound(path.join('sons','obrafinalizada.wav'))
    pygame.mixer.Sound.play(sucesso)





def preparar_obra(jogo, lista):

    voltar = pygame.image.load(path.join('sistema', 'voltar.png'))

    jogo.modo = "construir"
    while True:

        animacao(jogo, lista, False)
        jogo.janela.blit(voltar, (0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                pos_vetor = achar_celula(position)

                if pos_vetor == 0:
                    jogo.modo = "espectador"
                    return True

                if lista[pos_vetor].pretendente == "vertical" or lista[pos_vetor].pretendente == "total":
                    erguer(lista,pos_vetor,jogo)
                    jogo.modo = "espectador"
                    pretendencia(lista,pos_vetor,False)
                    jogo.construirtipo = None
                    return False

        jogo.clock.tick(60)



def catalogo(jogo, lista, desfocar, voltar, ant, prox,livrpaginatual, flipar):
    
    anterior = pygame.image.load(path.join('sistema', ant + '.png'))
    proxima = pygame.image.load(path.join('sistema', prox + '.png'))

    opcao1 = pygame.image.load(path.join('sistema', 'comprar' + livrpaginatual[0] + '.png'))
    opcao2 = pygame.image.load(path.join('sistema', 'comprar' + livrpaginatual[1] + '.png'))
    opcao3 = pygame.image.load(path.join('sistema', 'comprar' + livrpaginatual[2] + '.png'))
    opcao4 = pygame.image.load(path.join('sistema', 'comprar' + livrpaginatual[3] + '.png'))
    
    animacao(jogo,lista, False)

    jogo.janela.blit(desfocar, (0,0))
    jogo.janela.blit(voltar, (0,0))
    jogo.janela.blit(anterior, (51,279))
    jogo.janela.blit(proxima, (969,279))

    jogo.janela.blit(opcao1, (153,279))
    jogo.janela.blit(opcao2, (357,279))
    jogo.janela.blit(opcao3, (561,279))
    jogo.janela.blit(opcao4, (765,279))

    if flipar == True: pygame.display.flip()