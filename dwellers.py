from random import seed
from random import randint

class moradores:
    def __init__(self):
        self.sexo = None
        self.nome = None
        self.sobrenome = None
        self.nomecompleto = None
        self.xp = None
        self.nivel = None
        self.vida = None
        self.radiacao = None

        self.cabelo = None
        self.rosto = None

        self.forca = None      #pra agua
        self.agilidade = None      #pra comida
        self.resistencia = None    #eletricidade
        self.carisma = None        #radio e quarto
        self.inteligencia = None   #pro laboratorio                #SIGLA: CIFRA



def nome(numAleatorio, sexo):
    seed()
    
    nomeM = ["erick","emanuel","jorge","joao","vitor","marcos","daniel","luan","edson","leandro","alexandre","carlos","samuel","assis"  #14
        "franklin","henrique","gabriel","juliano","diogo","josafa","junior"]