import pygame
pygame.init()
import sys
from os import path

import celulas
import funcoes
import menu
import blueprint

class geral:
    def __init__(self):

        self.janela = pygame.display.set_mode((1071,651))
        self.dificuldade = None
        self.carregar = None
        self.dados = None
        self.dinheiro = None
        self.modo = None
        self.clock = pygame.time.Clock()

        self.construirtipo = None

        self.iconesistema = pygame.image.load(path.join('sistema', 'sistema.png'))
        self.fundo = pygame.image.load(path.join('cenario', 'dia.png'))

    def menu(self):
        pass

    def ciclonoitedia(self):
        pass


jogo = geral()
menu.menu(jogo)

if jogo.dados.carregar == False:
    blueprint.iniciar_generico(celulas.lista,jogo.dados)
    blueprint.salvar(celulas.lista,jogo)
else: blueprint.carregar(celulas.lista,jogo)

#iconesistema = pygame.image.load(path.join('sistema', 'sistema.png'))
#fundo = pygame.image.load(path.join('cenario', 'dia.png'))
#fundo_noite = pygame.image.load(path.join('cenario', 'noite.png'))
#configuracoes = pygame.image.load("configuracoes.png")   #pode ficar "alocado" na celula 1 (0,0), e assim se sabe se foi aberta. 

#sera se compensava eu ter os dados do jogo numa classe?
#preto = 0, 0, 0
horario = 1
jogo.modo = "espectador"
#modos: espectador - visualizar o bunker, construir - visualizar onde construir, espiar - assistir uma sala individualmente
#clock tick

while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:

            position = pos_x, pos_y = pygame.mouse.get_pos()
            pos_vetor = funcoes.achar_celula(position)

            if jogo.modo == "espectador":

                
                #print(pos_vetor)
                if pos_vetor == 0:
                    menu.sistema(jogo,celulas.lista)

                elif celulas.lista[pos_vetor].pedra == True:
                    funcoes.minerar(jogo, celulas.lista[pos_vetor])
                    funcoes.pretendencia(celulas.lista,pos_vetor,True)



            elif jogo.modo == "construir":       
                

                if pos_vetor == 0: menu.selecionarsala(jogo,celulas.lista)
                   #so da pra construir clicando, mas as exibicoes nao podem esperar o clique
                pos_vetor = funcoes.achar_celula(position)
                if celulas.lista[pos_vetor].pretendente == "vertical" or celulas.lista[pos_vetor].pretendente == "total":
                    funcoes.erguer(celulas.lista[pos_vetor],jogo.construirtipo)
                    jogo.modo = "espectador"
                    funcoes.pretendencia(celulas.lista,pos_vetor,False)
                #talvez essa parte seria bom ser nada mais doq a hora que vc escolhe o lugar pra construir, so isso
                #o resto acontece em outras funcoes
                #funcoes.construir(jogo,celulas.lista)
                

    funcoes.animacao(jogo, celulas.lista)
    jogo.clock.tick(60)