import pygame
from os import path
import sys
import funcoes

class dados:
    def __init__(self, dificuldade, carregar, posicao, nome):
        self.carregar = carregar
        self.posicao = posicao
        self.dificuldade = dificuldade
        self.nome = nome

    def zerar(self):
        self.carregar = None
        self.posicao = None
        self.dificuldade = None
        self.nome = None




def animacao():
    pass




def menu(jogo):


    #dados.zerar(self)
    animacao()

    #opcoes: iniciar novo jogo, carregar jogo, manual, opcoes ou sair
    #se escolher iniciar jogo, pergunta posicao, nome do save e dificuldade
        #volta pra main e chama a funcao criar generico (depende dif.), assim salvando num arquivo naquela posicao e com aquele nome

    #criar aqui o objeto da classe dados
    
    posicao = "1"
    nome = "erick"
    dificuldade = "facil"
    carregar = False

    if dificuldade == "facil": jogo.dinheiro = 2000     #quanto seria bom?
    else: jogo.dinheiro = 2000

    jogo.dados = dados(dificuldade,carregar,posicao,nome)
    
    #return


#fazer aqui todo e qualquer menu, qualquer icone verdinho que representar uma função era bom ficar aqui


def sistema(jogo, lista):

    #licensa = pygame.image.load(path.join('sistema', 'sistemaaberto.png'))
    #subsistemas = pygame.image.load(path.join('sistema', 'subsistemas.png'))
    #jogo.janela.blit(licensa, (0,0))
    #jogo.janela.blit(subsistemas, (0,0))
    #pygame.display.flip()

    #TESTANDOOOOOOOOOOO

    testebosta = jogo.janela

    licensa = pygame.image.load(path.join('sistema', 'sistemaaberto.png'))
    subsistemas = pygame.image.load(path.join('sistema', 'subsistemas.png'))




    testebosta.blit(licensa, (0,0))
    testebosta.blit(subsistemas, (0,0))
    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                position = pos_x, pos_y = pygame.mouse.get_pos()
                if pos_x <= 51:
                    if pos_y < 93: return
                    elif pos_y >= 93 and pos_y <= 372:
                        if pos_y >= 93 and pos_y < 186:


                            selecionarsala(jogo)
                            #jogo.modo = "construir"             #aqui vai pra funcao de escolher qual sala, e ai retorna total
                            return


                        if pos_y >= 186 and pos_y < 279:
                            pass #abrir os moradores
                        if pos_y >= 279 and pos_y <= 372:
                            pass #abrir as configuracoes
                    else: return

                else: return



def selecionarsala(jogo):

    licensa = pygame.image.load(path.join('sistema', 'sistemaaberto.png'))
    jogo.janela.blit(licensa, (0,0))
    pygame.display.flip()



    while True:
        print('ei')
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                pos_vetor = funcoes.achar_celula(position)

                jogo.construirtipo = "elevador"
                jogo.modo = "construir"
                return