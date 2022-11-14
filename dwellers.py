from random import seed
from random import randint
from funcoes import empregar_Dw_Cl

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


    def Mnome(self, sexo):
        seed()

        randint(1,20)
        nomeM = ["erick","emanuel","jorge","joao","vitor","marcos","daniel","luan","edson","leandro","alexandre","carlos","samuel","assis"#14
            "franklin","henrique","gabriel","juliano","diogo","josafa","junior"]


    def Msobrenome(self, sexo):
        seed()

        randint(1,20)

    def Mnomecompleto(self):
        self.nomecompleto = (self.nome," ",self.sobrenome)
        



def atribuir(dweller):

    CIFRA = [0,0,0,0,0]
    for _ in range(13):
        pos = randint(0,4)
        CIFRA[pos] += 1

    dweller.forca += CIFRA[2]
    dweller.agilidade += CIFRA[4]
    dweller.resistencia += CIFRA[3]
    dweller.carisma += CIFRA[0]
    dweller.inteligencia += CIFRA[1]



def inicializar(celulas):

    novo_fila = morador()
    #aumentar total
    #colocar nas primeiras celulas

    novo_fila.id = 2
    novo_fila.sexo = "M"
    novo_fila.nome = novo_fila.Mnome(novo_fila.sexo)
    novo_fila.sobrenome = novo_fila.Msobrenome(novo_fila.sexo)

    novo_fila.Mnomecompleto()
    atribuir(novo_fila)
    empregar_Dw_Cl(novo_fila,celulas[21])

    novo_fila.id = 3
    novo_fila.sexo = "F"
    novo_fila.nome = novo_fila.Mnome(novo_fila.sexo)
    novo_fila.sobrenome = novo_fila.Msobrenome(novo_fila.sexo)

    novo_fila.Mnomecompleto()
    atribuir(novo_fila)
    empregar_Dw_Cl(novo_fila,celulas[22])

    novo_fila.id = 4
    novo_fila.sexo = "M"
    novo_fila.nome = novo_fila.Mnome(novo_fila.sexo)
    novo_fila.sobrenome = novo_fila.Msobrenome(novo_fila.sexo)

    novo_fila.Mnomecompleto()
    atribuir(novo_fila)
    empregar_Dw_Cl(novo_fila,celulas[23])

    novo_fila.id = 5
    novo_fila.sexo = "F"
    novo_fila.nome = novo_fila.Mnome(novo_fila.sexo)
    novo_fila.sobrenome = novo_fila.Msobrenome(novo_fila.sexo)

    novo_fila.Mnomecompleto()
    atribuir(novo_fila)
    empregar_Dw_Cl(novo_fila,celulas[24])

    novo_fila.id = 6
    novo_fila.sexo = "F"
    novo_fila.nome = novo_fila.Mnome(novo_fila.sexo)
    novo_fila.sobrenome = novo_fila.Msobrenome(novo_fila.sexo)

    novo_fila.Mnomecompleto()
    atribuir(novo_fila)
    empregar_Dw_Cl(novo_fila,celulas[25])

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