class celulas:
    def __init__(self, id, bloqueada, coordenadas, vazio, tipo, situacao, consumo, pedra, pretendente):

        #misturar a classe grid e a classe da propria sala? Fazer em ordem de prioridade

        self.id = id     #'nome' da celula na grid, vai de 1 a 147, mas 12 são bloqueadas
        self.bloqueada = bloqueada  #essa indica se a celula se encontra totalmente dentro da terra
        self.pedra = pedra  #avisa se deve aparecer uma pedra no meio da celula
        self.vazio = vazio  #indica se atualmente esta construido algo nela
        self.pretendente = pretendente    #indica se ela esta liberada pra ser construida
        self.tipo = tipo   #indica qual a sala que esta construida
        #level?
        self.situacao = situacao   #indica qual a imagem deve ser usada, ex: se é da ponta esquerda, ou tem duas ao redor

        self.coordenadas = coordenadas    #indica quais as coordenadas seriam o (0,0) dessa celula
        self.consumo = consumo    #indica qual o consumo de energia dessa celula
        #vizinhos? ajudaria a demarcar os pretendentes
        #direções de passagem
        #indicar que esta fundido


        #situacao, poderia ser ja o nome da imagem a ser usada como string, pra enviar no blip inves de fazer varios ifs


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
    
    aleatorios.append(value)

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

while parar == False:
    
    if (ide >=1 and ide <= 7) or (ide >=22 and ide <= 26):
        bloqueada = True
    else:
        bloqueada = False
        vazio = True
        consumo = 0
        pretendente = False
        a = ide // (21+1) #representa o i na matriz
        b = (ide-1) % 21 #representa o j na matriz
        b = b * 51 #o j na matriz representa a largura
        a = a * 93 #o i na matriz representa a altura
        coordenadas = b, a
    
    if ide in aleatorios:
        pedra = True
    else:
        pedra = False
    
    lista.append(celulas(ide,bloqueada,coordenadas,vazio,tipo,situacao,consumo,pedra,pretendente))

    ide += 1
    if ide > 147:
        parar = True

#essa parte é a que muda dependendo da dificuldade

dificil = 26
while dificil >= 26 and dificil <= 30:

    lista[dificil].pedra = False
    lista[dificil].vazio = False
    lista[dificil].tipo = "porta"   #lembrando que a porta e indestrutivel
    lista[dificil].consumo = 100 #ainda em testes esse valor
    dificil += 1

lista[26].situacao = "PE" #ponta esquerda
lista[27].situacao = "M1" #meio 1
lista[28].situacao = "M2"
lista[29].situacao = "PD"

lista[30].tipo = "elevador"
lista[30].consumo = 20
lista[30].situacao = "ND" #ele nao tem imagens diferentes pra celulas diferentes

if lista[30-21].pedra == False:     #quando quebra uma pedra é preciso checar se se torna pretendente
    lista[30-21].pretendente = True
if lista[30+21].pedra == False:
    lista[30+21].pretendente = True

dificil = 31
while dificil >= 31 and dificil <= 36:
    lista[dificil].pedra = False
    lista[dificil].vazio = False
    lista[dificil].tipo = "quarto"
    lista[dificil].consumo = 150
    dificil += 1

lista[31].situacao = "PE"
lista[32].situacao = "M1"
lista[33].situacao = "M2"
lista[34].situacao = "M3"
lista[35].situacao = "M4"
lista[36].situacao = "PD"

if lista[37].pedra == False:
    lista[37].pretendente = True



#testando
contagem = 0
while contagem < 147:
    print(vars(lista[contagem]))
    contagem += 1