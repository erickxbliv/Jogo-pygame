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
        self.stimpack = 0
        self.radaway = 0

        self.moradores = None       #se chegar a zero, game over
        self.lotacao = None
        self.scoredias = 1

    def menu(self):
        pass

    def ciclonoitedia(self, x):
        self.fuso = pygame.image.load(path.join('fundo', str(x) + 'horas.png'))


jogo = geral()
jogo.sobresalas = testedados.dados()
menu.menu(jogo)
pygame.mixer.stop()

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
prod = ["cozinha","gerador","tratamento","renda","laboratorio"]
virouodia =  pygame.mixer.Sound(path.join('sons','bomdia.wav'))
    
#modos: espectador - visualizar o bunker, construir - visualizar onde construir, espiar - assistir uma sala individualmente

while True:

    #if jogo.energia == 0 or not dwellers.lista:
    #print(jogo.moradores)
    if not dwellers.lista or jogo.moradores == 0:
        menu.gameover(jogo)
#verificar como estao os dados, pra dar game over ou continuar. aqui tambem e consumida a vida e saude quando abaixo do minimo
#game over deleta o save
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
                    celulas.lista[pos_vetor].morador.celula = None     #sera se isso da erro?
                    celulas.lista[pos_vetor].morador = None

                elif celulas.lista[pos_vetor].vazio != None and not celulas.lista[pos_vetor].vazio:
                    if celulas.lista[pos_vetor].idle and celulas.lista[pos_vetor].morador != None:
                        if celulas.lista[contagem].tipo == "cozinha":
                            jogo.comida += jogo.sobresalas.producao[2] * celulas.lista[pos_vetor].morador.agilidade
                            #aumentar xp
                        elif celulas.lista[contagem].tipo == "gerador":
                            jogo.energia += jogo.sobresalas.producao[4] * celulas.lista[pos_vetor].morador.força
                        elif celulas.lista[contagem].tipo == "tratamento":
                            jogo.agua += jogo.sobresalas.producao[3] * celulas.lista[pos_vetor].morador.resistencia
                        elif celulas.lista[contagem].tipo == "renda":
                            jogo.dinheiro += jogo.sobresalas.producao[5] * celulas.lista[pos_vetor].morador.inteligencia
                        elif celulas.lista[contagem].tipo == "laboratorio":
                            jogo.stimpack += jogo.sobresalas.producao[6] * celulas.lista[pos_vetor].morador.inteligencia
                        #aqui acontece quando vai coletar a producao da celula
                        celulas.lista[pos_vetor].idle = False
                    else: menu.espiar(jogo,celulas.lista,dwellers.lista,pos_vetor)
                        
                elif celulas.lista[pos_vetor].pedra == True:
                    #print("ola")
                    funcoes.minerar(jogo, celulas.lista[pos_vetor])
                    funcoes.pretendencia(celulas.lista,pos_vetor,True)

                

    funcoes.animacao(jogo, celulas.lista,True)


    if int(ponteiro) != int(horario):                  
        jogo.ciclonoitedia(int(horario))
        ponteiro = horario
        
        contagem = 0
        while contagem < 147:

            if celulas.lista[contagem].tipo == "quarto" and horario == 24.0:
                if celulas.lista[contagem].situacao[1] == "1": dwellers.verificar_gravidez(jogo,celulas.lista,dwellers.lista,contagem)

            elif celulas.lista[contagem].tipo in prod and celulas.lista[contagem].morador != None:

                if celulas.lista[contagem].lvl == "1":
                    if horario == 24.0 or horario == 12.0: celulas.lista[contagem].idle = True
                elif celulas.lista[contagem].lvl == "2":
                    if horario == 24.0 or horario == 8.0 or horario == 16.0: celulas.lista[contagem].idle = True
                elif celulas.lista[contagem].lvl == "3":
                    if horario == 24.0 or horario == 12.0 or horario == 6.0 or horario == 18.0: celulas.lista[contagem].idle = True

            contagem += 1
        
        if jogo.agua < ((jogo.sobresalas.gastoagua * jogo.moradores) // 24): jogo.agua = 0
        else: jogo.agua = jogo.agua - ((jogo.sobresalas.gastoagua * jogo.moradores) // 24)
        if jogo.comida < ((jogo.sobresalas.gastocomida * jogo.moradores) // 24): jogo.comida = 0
        else: jogo.comida = jogo.comida - ((jogo.sobresalas.gastocomida * jogo.moradores) // 24)
        if jogo.energia < (jogo.sobresalas.consumo // 24): jogo.energia = 0
        else: jogo.energia = jogo.energia - (jogo.sobresalas.consumo // 24)

        #print("vou entrar")
        funcoes.sobrevivencia(jogo,celulas.lista,dwellers.lista)
        #print("consegui.. agora:")

    horario += 0.01
    if horario > 24.0:    #24 = max de imagens
        horario = 1.0
        jogo.dinheiro += jogo.sobresalas.lucrodia
        pygame.mixer.Sound.play(virouodia)
        jogo.scoredias += 1


        #aqui tambem acontecem os consumos, na vdd nao melhor q seja ao passar das horas mesmo
    jogo.clock.tick(60)