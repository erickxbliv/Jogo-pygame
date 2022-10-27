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
        self.consumo = consumo    #indica qual o consumo de energia dessa celula
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
        
#agora vai haver essa funcao pra formar o nome da imagem, pra poder carrega-la

aleatorios = []
lista = []
seed()

#aleatorizar quais celulas terao pedras

for _ in range(15):
    parar = False

    while parar == False:
        value = randint(1, 147)
        if (value >=1 and value <= 7) or (value >=22 and value <= 26):
            parar = False
        else:
            parar = True
    
    aleatorios.append(value)

#preencher celulas com dados genericos

parar = False

ide = 1
bloqueada = False
pedra = False
coordenadas = None
vazio = None
tipo = None
situacao = None
consumo = None
pretendente = None
lvl = None

while parar == False:
    
    if (ide >=1 and ide <= 7) or (ide >=22 and ide <= 26):
        bloqueada = True
    else:
        bloqueada = False
        vazio = True
        consumo = 0
        pretendente = False
        a = ((ide-1) // 21) #representa o i na matriz
        b = (ide-1) % 21 #representa o j na matriz
        b = b * 51 #o j na matriz representa a largura
        a = a * 93 #o i na matriz representa a altura
        coordenadas = b, a
    
    if ide in aleatorios and bloqueada == False:
        pedra = True
    else:
        pedra = False
    
    lista.append(celulas(ide,bloqueada,coordenadas,vazio,tipo,situacao,consumo,pedra,pretendente,lvl))

    ide += 1
    if ide > 147: parar = True

#a partir aqui vamos preencher os dados corretos pra porta, quarto e elevador que vem de padrão

entrada = 26
while entrada >= 26 and entrada <= 30:

    lista[entrada].pedra = False
    lista[entrada].vazio = False
    lista[entrada].tipo = "porta"   #lembrando que a porta e indestrutivel
    lista[entrada].consumo = 25 #ainda em testes esse valor, mas lembrando que aqui corresponde a uma celula sozinha
    lista[entrada].lvl = '1'
    entrada += 1

lista[26].situacao = "_1"   #nao ha o denominador porque so existe uma maneira de organizar a porta
lista[27].situacao = "_2"
lista[28].situacao = "_3"
lista[29].situacao = "_4"

lista[30].tipo = "elevador"
lista[30].consumo = 20
lista[30].situacao = "_0" #ele nao tem imagens diferentes
lista[30].lvl = '0'

if lista[30-21].pedra == False:     #quando quebra uma pedra é preciso checar se se torna pretendente
    lista[30-21].pretendente = True
if lista[30+21].pedra == False:
    lista[30+21].pretendente = True

quartos = 31
while quartos >= 31 and quartos <= 36:
    lista[quartos].pedra = False
    lista[quartos].vazio = False
    lista[quartos].tipo = "quarto"
    lista[quartos].consumo = 150
    lista[quartos].lvl = '2'
    quartos += 1

lista[31].situacao = "_1-6" #esse quarto esja junto a outros 5
lista[32].situacao = "_2-6"
lista[33].situacao = "_3-6"
lista[34].situacao = "_4-6"
lista[35].situacao = "_5-6"
lista[36].situacao = "_6-6"

if lista[37].pedra == False:
    lista[37].pretendente = True

#teste pra visualizar o que ha na lista dos objetos (lista de todas as celulas) e criar seus objetos
contagem = 0
while contagem < 147:

    lista[contagem].imagem()
    print(vars(lista[contagem])) #teste
    contagem += 1
