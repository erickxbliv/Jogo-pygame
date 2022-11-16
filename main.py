import pygame
from pygame import mixer

pygame.init()
mixer.init()
import sys
from os import path

import celulas
import funcoes
import menu
import blueprint

import testedados
import dwellers

class geral:
    def __init__(self):

        self.janela = pygame.display.set_mode((1071,701))
        self.clock = pygame.time.Clock()
        self.iconesistema = pygame.image.load(path.join('sistema', 'sistema.png'))
        self.fundo = pygame.image.load(path.join('cenario', 'fundo.png'))
        self.fuso = pygame.image.load(path.join('fundo', '12horas.png'))

        self.dificuldade = None
        self.carregar = None
        self.dados = None
        self.modo = "espectador"
        
        self.construirtipo = None
        self.sobresalas = None

        self.dinheiro = 0
        self.energia = 1000         #se chegar a zero acaba
        self.comida = 1000
        self.agua = 1000

        self.moradores = None       #se chegar a zero, game over
        self.lotacao = None

    def menu(self):
        pass

    def ciclonoitedia(self, x):
        self.fuso = pygame.image.load(path.join('fundo', str(x) + 'horas.png'))


jogo = geral()
jogo.sobresalas = testedados.dados()
menu.menu(jogo)

if jogo.dados.carregar == False:
    blueprint.iniciar_generico(celulas.lista,jogo.dados)
    blueprint.salvar(celulas.lista,jogo)

    dwellers.inicializar(celulas.lista)
    funcoes.empregar_Dw_Cl(dwellers.lista[0],celulas.lista[27])
    jogo.moradores = 1
else:
    blueprint.carregar(celulas.lista,jogo)
    dwellers.lista.clear()     #tem q zerar pois se n ja comecaria com 1
    
jogo.sobresalas.calcconsumo()
horario = ponteiro = 12.0
#modos: espectador - visualizar o bunker, construir - visualizar onde construir, espiar - assistir uma sala individualmente

while True:

#verificar como estao os dados, pra dar game over ou continuar. aqui tambem e consumida a vida e saude quando abaixo do minimo
    #print(jogo.energia, jogo.sobresalas.consumo,(jogo.sobresalas.producao[4] * jogo.sobresalas.qtd_EQCAEDRT[4]))
    #print(jogo.agua,(jogo.moradores * jogo.sobresalas.minimo))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:

            position = pos_x, pos_y = pygame.mouse.get_pos()
            pos_vetor = funcoes.achar_celula(position)

            if jogo.modo == "espectador":

                #print("###################\n",vars(celulas.lista[pos_vetor]),"\n----------------------")   #teste

                #print(pos_vetor)
                if pos_vetor == 0:
                    menu.sistema(jogo,celulas.lista,dwellers.lista)

                elif celulas.lista[pos_vetor].morador != None and pos_vetor >= 21 and pos_vetor <= 25:
                    dwellers.lista.append(celulas.lista[pos_vetor].morador)
                    jogo.moradores += 1
                    celulas.lista[pos_vetor].morador.celula = "intervalo"     #sera se isso da erro?
                    celulas.lista[pos_vetor].morador = None

                elif celulas.lista[pos_vetor].vazio != None and not celulas.lista[pos_vetor].vazio:
                    if celulas.lista[pos_vetor].idle == True:
                        pass #aqui acontece quando vai coletar a producao da celula
                    else: menu.espiar(jogo,celulas.lista,dwellers.lista,pos_vetor)
                        
                elif celulas.lista[pos_vetor].pedra == True:
                    #print("ola")
                    funcoes.minerar(jogo, celulas.lista[pos_vetor])
                    funcoes.pretendencia(celulas.lista,pos_vetor,True)

                

    funcoes.animacao(jogo, celulas.lista,True)


    if int(ponteiro) != int(horario):                       #isso aq devia acontecer dentro de animacao
        jogo.ciclonoitedia(int(horario))
        ponteiro = horario

        if jogo.agua < ((jogo.sobresalas.gastoagua * jogo.moradores) // 24): jogo.agua = 0
        else: jogo.agua = jogo.agua - ((jogo.sobresalas.gastoagua * jogo.moradores) // 24)
        if jogo.comida < ((jogo.sobresalas.gastocomida * jogo.moradores) // 24): jogo.comida = 0
        else: jogo.comida = jogo.comida - ((jogo.sobresalas.gastocomida * jogo.moradores) // 24)
        if jogo.energia < (jogo.sobresalas.consumo // 24): jogo.energia = 0
        else: jogo.energia = jogo.energia - (jogo.sobresalas.consumo // 24)

    horario += 0.01
    if horario > 24.0:    #24 = max de imagens
        horario = 1.0
        jogo.dinheiro += jogo.sobresalas.lucrodia
    
        #aqui tambem acontecem os consumos, na vdd nao melhor q seja ao passar das horas mesmo
    jogo.clock.tick(60)