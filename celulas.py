import pygame
from os import path
from random import seed
from random import randint

#a dificuldade deve mudar alguns conceitos aqui
#carregar um save deve mudar muito o que acontece aqui

class celulas:
    def __init__(self, id, bloqueada, coordenadas, vazio, tipo, situacao, consumo, pedra, pretendente,lvl):

        #Fazer em ordem de prioridade
        self.id = id     #'nome' da celula na grid, vai de 1 a 147, mas 12 são bloqueadas
        self.bloqueada = bloqueada  #essa indica se a celula se encontra totalmente dentro da terra
        self.pedra = pedra  #avisa se deve aparecer uma pedra no meio da celula
        self.vazio = vazio  #indica se atualmente esta construido algo nela
        self.pretendente = pretendente    #indica se ela esta liberada pra ser construida
        self.tipo = tipo   #indica qual a sala que esta construida
        self.lvl = lvl
        self.situacao = situacao   #indica qual a imagem deve ser usada, ex: se é da ponta esquerda, ou tem duas ao redor

        self.coordenadas = coordenadas    #indica quais as coordenadas seriam o (0,0) dessa celula
        self.consumo = consumo   #indica qual o consumo de energia dessa celula
        #self.obj = obj

        #vizinhos? ajudaria a demarcar os pretendentes
        #direções de passagem
        #indicar que esta fundido
        #misturar a classe grid e a classe da propria sala? um objeto pra o tipo da sala dentro da celula?
    
    #def imagem(self, obj, tipo, lvl, situacao, pedra, vazio):
    def imagem(self):

        if self.pedra == True:
            self.obj = pygame.image.load(path.join('cenario', 'pedra.png'))
        else:
            if self.vazio == False:
                imagem = (self.tipo + self.lvl + self.situacao + ".png")
                self.obj = pygame.image.load(path.join('cenario', imagem))
            else: self.obj = None

        if self.id == 1: self.obj = pygame.image.load(path.join('sistema', 'configuracoes.png'))   #teste
   
#agora vai haver essa funcao pra formar o nome da imagem, pra poder carrega-la

#menu.menu()

lista = []

ide = None
bloqueada = None
pedra = None
coordenadas = None
vazio = None
tipo = None
situacao = None
consumo = None
pretendente = None
lvl = None

cont = 1
parar = False
while parar == False:

    lista.append(celulas(ide,bloqueada,coordenadas,vazio,tipo,situacao,consumo,pedra,pretendente,lvl))

    cont += 1
    if cont > 147: parar = True