class celulas:
    def __init__(self, id, bloqueada, coordenadas, vazio, tipo, situacao, consumo, pedra, pretendente):

        #misturar a classe grid e a classe da propria sala? Fazer em ordem de prioridade

        self.id     #'nome' da celula na grid, vai de 1 a 147, mas 12 são bloqueadas
        self.bloqueada  #essa indica se a celula se encontra totalmente dentro da terra
        self.pedra  #avisa se deve aparecer uma pedra no meio da celula
        self.vazio  #indica se atualmente esta construido algo nela
        self.pretendente    #indica se ela esta liberada pra ser construida
        self.tipo   #indica qual a sala que esta construida
        self.situacao   #indica qual a imagem deve ser usada, ex: se é da ponta esquerda, ou tem duas ao redor
        self.coordenadas    #indica quais as coordenadas seriam o (0,0) dessa celula
        self.consumo    #indica qual o consumo de energia dessa celula




#import random
from random import seed
from random import randint

aleatorios = []
lista = []

seed(1)

for _ in range(15):
    parar = False

    while parar == False:
        value = randint(1, 147)
        if (value >=1 and value <= 7) or (value >=22 and value <= 26):
            parar = False
        else:
            parar = True
    
    aleatorios.append = (value)

parar = False

id = 1
bloqueada = False
pedra = False
coordenadas = None
vazio = None
tipo = None
situacao = None
consumo = None
pretendente = None

while parar == False:

    if (value >=1 and value <= 7) or (value >=22 and value <= 26):
        bloqueada = True
    else:
        bloqueada = False
        vazio = True
        consumo = 0
        pretendente = False
        a = id // 21 #a coordenada no eixo y
        b = id % 21 #a coordenada no eixo x
        a = (a-1) * 51
        b = b * 93
        coordenadas = a, b
    
    if id in aleatorios:
        pedra = True
    else:
        pedra = False

    lista.append(celulas(id,bloqueada,coordenadas,vazio,tipo,situacao,consumo,pedra,pretendente))

    id += 1
    if id > 147:
        parar = True