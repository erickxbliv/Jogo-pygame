from random import seed
from random import randint
from funcoes import empregar_Dw_Cl

from os import path
from pygame import mixer
mixer.init()

class morador:   
    def __init__(self):
        self.id = None
        self.sexo = None
        self.nome = None
        self.sobrenome = None
        self.nomecompleto = None

        self.xp = 0             #quando vc clica no personagem ele sobe de nivel
        self.nivel = 1  
        self.vida = 100
        self.radiacao = 0
        self.trabalho = None
        self.celula = None          #eles nao precisam de coordenada, e so tem um padrao acima das da celula

        self.crianca = None
        self.cabelo = None
        self.rosto = None
        self.gravida = None

        self.forca = 1      #pra agua
        self.agilidade = 1      #pra comida
        self.resistencia = 1    #eletricidade
        self.carisma = 1       #radio e quarto
        self.inteligencia = 1   #pro laboratorio                #SIGLA: CIFRA


    def Mnome(self):
        seed()

        nomeM = ["erick","emanuel","jorge","joao","vitor","marcos","daniel","luan","edson","leandro","alexandre","carlos","samuel","assis",#14
            "franklin","henrique","gabriel","juliano","diogo","josafa","junior","igor","luiz","raimundo"]

        nomeF = ["mariana","julia","clara","flavia","marta","maura","laura","maria","anna","livia","lavinia","jane","estefani","ysis", #14
            "elisa","monica","lurdes","lara","nayara","isabel","rosa","marisol","adriana","sofia","solange","elizabeth","helena","alice",
            "yasmin","milena"] #16

        if self.sexo == "M":
            max = 23
            valor = randint(1,max)
            self.nome = nomeM[valor-1]
        elif self.sexo == "F":
            max = 28
            valor = randint(1,max)
            self.nome = nomeF[valor-1]

    def Msobrenome(self):
        seed()

        sobrenomes = ["pontes","assis","ribeiro","pinheiro","brito","sousa","lima","xenofonte","freitas","martins","oliveira","sales",
            "torres","almeida","azevedo","braga","queiroz","rocha","siqueira","teixeira","magalhaes","matos","silva","castro",
            "siebra","gonçalvez","macedo","ferreira","fonseca","gomes","santos","cardoso","saraiva","velozo","carvalho","duarte",
            "alvez","lopez","dias","costa","brasil","santana","mendes","andrade","soares","barbosa","amaral","feitosa","tavares","reis", #50
            "aguiar","mendonça","leal","novaes","cabral","araujo","correia","barros","bezerra","viana","aquino","peixoto","pires","borges"] #14

        valor = randint(1,60)
        self.sobrenome = sobrenomes[valor-1]
        

    def Mnomecompleto(self):
        self.nomecompleto = (self.nome + " " + self.sobrenome)
        



def atribuir(dweller,points):

    if points == None: points = 13
    CIFRA = [0,0,0,0,0]
    for _ in range(points):
        pos = randint(0,4)
        CIFRA[pos] += 1

    dweller.forca += CIFRA[2]
    dweller.agilidade += CIFRA[4]
    dweller.resistencia += CIFRA[3]
    dweller.carisma += CIFRA[0]
    dweller.inteligencia += CIFRA[1]


def qt_pts(dweller):
    total = 0
    total += dweller.forca
    total += dweller.agilidade
    total += dweller.resistencia
    total += dweller.carisma
    total += dweller.inteligencia
    return total


def inicializar(celulas):

    novo_fila = morador()
    #aumentar total
    #colocar nas primeiras celulas

    novo_fila.id = 2
    novo_fila.sexo = "M"
    novo_fila.Mnome()
    #print(novo_fila.nome)
    novo_fila.Msobrenome()

    #print(vars(novo_fila))
    novo_fila.Mnomecompleto()
    #print(vars(novo_fila))

    atribuir(novo_fila,None)
    empregar_Dw_Cl(novo_fila,celulas[21])

    novo_fila = morador()
    novo_fila.id = 3
    novo_fila.sexo = "F"
    novo_fila.Mnome()
    novo_fila.Msobrenome()

    novo_fila.Mnomecompleto()
    atribuir(novo_fila,None)
    empregar_Dw_Cl(novo_fila,celulas[22])

    novo_fila = morador()
    novo_fila.id = 4
    novo_fila.sexo = "M"
    novo_fila.Mnome()
    novo_fila.Msobrenome()

    novo_fila.Mnomecompleto()
    atribuir(novo_fila,None)
    empregar_Dw_Cl(novo_fila,celulas[23])

    novo_fila = morador()
    novo_fila.id = 5
    novo_fila.sexo = "F"
    novo_fila.Mnome()
    novo_fila.Msobrenome()

    novo_fila.Mnomecompleto()
    atribuir(novo_fila,None)
    empregar_Dw_Cl(novo_fila,celulas[24])

    novo_fila = morador()
    novo_fila.id = 6
    novo_fila.sexo = "F"
    novo_fila.Mnome()
    novo_fila.Msobrenome()

    novo_fila.Mnomecompleto()
    atribuir(novo_fila,None)
    empregar_Dw_Cl(novo_fila,celulas[25])



def nasceu(jogo,registro,pai,mae):

    seed()
    novo_fila = morador()
    novo_fila.id = registro[jogo.moradores-1] + 1
    teste = randint(1,2)
    if teste == 1: novo_fila.sexo = "F"
    else: novo_fila.sexo = "M"
    novo_fila.Mnome()
    novo_fila.Msobrenome()

    novo_fila.Mnomecompleto()

    total = qt_pts(pai)
    total += qt_pts(mae)
    total = total //2

    atribuir(novo_fila,total)
    registro.append(novo_fila)
    jogo.moradores += 1

    nasceu =  mixer.Sound(path.join('sons','nascimento.wav'))
    mixer.Sound.play(nasceu)





def verificar_gravidez(jogo,lista,registro,pos_vetor):

    melhor_cara = None
    melhor_muie = None

    if jogo.moradores >= jogo.lotacao: return

    if lista[pos_vetor].morador != None:  #se tem um morador
        if lista[pos_vetor].morador.sexo == "M": melhor_cara = lista[pos_vetor].morador   #se for cara, e melhor q nada
        elif lista[pos_vetor].morador.sexo == "F": melhor_muie = lista[pos_vetor].morador #se for muie, e melhor q nada

    if lista[pos_vetor+1].morador != None:          #se na segunda tbm tem
        if lista[pos_vetor+1].morador.sexo == "M":   #e for homem
            if melhor_cara != None:             #se o melhor ja foi encontrado
                if melhor_cara.carisma < lista[pos_vetor+1].morador.carisma: melhor_cara = lista[pos_vetor+1].morador.carisma#foi superado?
            else: melhor_cara = lista[pos_vetor+1].morador  #se n foi encontrado, melhor q nada
        elif lista[pos_vetor+1].morador.sexo == "F":  #ou for mulher
            if melhor_muie != None:
                if melhor_muie.carisma < lista[pos_vetor+1].morador.carisma: melhor_muie = lista[pos_vetor+1].morador.carisma
            else: melhor_muie = lista[pos_vetor+1].morador

    if int(lista[pos_vetor].situacao[3]) >= 4:
        if lista[pos_vetor+2].morador != None:          #se na segunda tbm tem
            if lista[pos_vetor+2].morador.sexo == "M":   #e for homem
                if melhor_cara != None:             #se o melhor ja foi encontrado
                    if melhor_cara.carisma < lista[pos_vetor+2].morador.carisma: melhor_cara = lista[pos_vetor+2].morador.carisma
                else: melhor_cara = lista[pos_vetor+2].morador  #se n foi encontrado, melhor q nada
            elif lista[pos_vetor+2].morador.sexo == "F":  #ou for mulher
                if melhor_muie != None:
                    if melhor_muie.carisma < lista[pos_vetor+2].morador.carisma: melhor_muie = lista[pos_vetor+2].morador.carisma
                else: melhor_muie = lista[pos_vetor+2].morador


        if lista[pos_vetor+3].morador != None:          #se na segunda tbm tem
            if lista[pos_vetor+3].morador.sexo == "M":   #e for homem
                if melhor_cara != None:             #se o melhor ja foi encontrado
                    if melhor_cara.carisma < lista[pos_vetor+3].morador.carisma: melhor_cara = lista[pos_vetor+3].morador.carisma
                else: melhor_cara = lista[pos_vetor+3].morador  #se n foi encontrado, melhor q nada
            elif lista[pos_vetor+3].morador.sexo == "F":  #ou for mulher
                if melhor_muie != None:
                    if melhor_muie.carisma < lista[pos_vetor+3].morador.carisma: melhor_muie = lista[pos_vetor+3].morador.carisma
                else: melhor_muie = lista[pos_vetor+3].morador

        if int(lista[pos_vetor].situacao[3]) >= 6:

            if lista[pos_vetor+4].morador != None:          #se na segunda tbm tem
                if lista[pos_vetor+4].morador.sexo == "M":   #e for homem
                    if melhor_cara != None:             #se o melhor ja foi encontrado
                        if melhor_cara.carisma < lista[pos_vetor+4].morador.carisma: melhor_cara = lista[pos_vetor+4].morador.carisma
                    else: melhor_cara = lista[pos_vetor+4].morador  #se n foi encontrado, melhor q nada
                elif lista[pos_vetor+4].morador.sexo == "F":  #ou for mulher
                    if melhor_muie != None:
                        if melhor_muie.carisma < lista[pos_vetor+4].morador.carisma: melhor_muie = lista[pos_vetor+4].morador.carisma
                    else: melhor_muie = lista[pos_vetor+4].morador


            if lista[pos_vetor+5].morador != None:          #se na segunda tbm tem
                if lista[pos_vetor+5].morador.sexo == "M":   #e for homem
                    if melhor_cara != None:             #se o melhor ja foi encontrado
                        if melhor_cara.carisma < lista[pos_vetor+5].morador.carisma: melhor_cara = lista[pos_vetor+5].morador.carisma
                    else: melhor_cara = lista[pos_vetor+5].morador  #se n foi encontrado, melhor q nada
                elif lista[pos_vetor+5].morador.sexo == "F":  #ou for mulher
                    if melhor_muie != None:
                        if melhor_muie.carisma < lista[pos_vetor+5].morador.carisma: melhor_muie = lista[pos_vetor+5].morador.carisma
                    else: melhor_muie = lista[pos_vetor+5].morador

    if melhor_cara != None and melhor_muie != None:
        seed()
        max = (melhor_cara.carisma + melhor_muie.carisma) // 2
        valor = randint(1,50)
        if valor >= 1 and valor <= max: nasceu(jogo,registro,melhor_cara,melhor_muie)




lista = []

dono = morador()

dono.id = 1
dono.sexo = "M"
dono.nome = "erick"
dono.sobrenome = "brito"
dono.Mnomecompleto()
dono.xp = 500
dono.nivel = 6

dono.carisma = 7
dono.inteligencia = 6
dono.forca = 4
dono.resistencia = 3
dono.agilidade = 5

lista.append(dono)      #agora a lista de moradores no main tem 1 pessoa, atualizar isso la