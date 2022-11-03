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

    def menu(self):
        pass


jogo = geral()
menu.menu(jogo)

if jogo.dados.carregar == False:
    blueprint.iniciar_generico(celulas.lista,jogo.dados)
    blueprint.salvar(celulas.lista,jogo)
else: blueprint.carregar(celulas.lista,jogo)

iconesistema = pygame.image.load(path.join('sistema', 'sistema.png'))
fundo = pygame.image.load(path.join('cenario', 'dia.png'))
#fundo_noite = pygame.image.load(path.join('cenario', 'noite.png'))
#configuracoes = pygame.image.load("configuracoes.png")   #pode ficar "alocado" na celula 1 (0,0), e assim se sabe se foi aberta. 

#sera se compensava eu ter os dados do jogo numa classe?
preto = 0, 0, 0
horario = 1
jogo.modo = "espectador"
#modos: espectador - visualizar o bunker, construir - visualizar onde construir, espiar - assistir uma sala individualmente
#clock tick

while True:

    if jogo.modo == "construir": funcoes.construir(jogo,celulas.lista)  #testando lugar


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            position = pos_x, pos_y = pygame.mouse.get_pos()
            #se clicar numa sala, tem que abrir ela
            
            if jogo.modo == "espectador":
                pos_vetor = funcoes.achar_celula(position)
                print(pos_vetor)
                if pos_vetor == 0: 
                    menu.sistema(jogo,celulas.lista)
                    

                if celulas.lista[pos_vetor].pedra == True:
                    funcoes.minerar(jogo, celulas.lista[pos_vetor])
                    funcoes.pretendencia(celulas.lista,pos_vetor)



            elif jogo.modo == "construir":          #so da pra construir clicando, mas as exibicoes nao podem esperar o clique
                #talvez essa parte seria bom ser nada mais doq a hora que vc escolhe o lugar pra construir, so isso
                #o resto acontece em outras funcoes
                #funcoes.construir(jogo,celulas.lista)
                pass


    jogo.janela.fill(preto)
    jogo.janela.blit(fundo, (0,0))
    jogo.janela.blit(iconesistema, (0,0))
    contagem = 0
    while contagem < 147:
        celulas.lista[contagem].imagem()    #sera se tem problema atualizar toda santa vez as imagens?
        if celulas.lista[contagem].obj != None:
            jogo.janela.blit(celulas.lista[contagem].obj,celulas.lista[contagem].coordenadas)

        contagem += 1

    pygame.display.flip()
    jogo.clock.tick(60)
