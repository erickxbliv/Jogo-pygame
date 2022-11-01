import pygame

class dados:
    def __init__(self, dificuldade, carregar, posicao, nome):
        self.carregar = carregar
        self.posicao = posicao
        self.dificuldade = dificuldade
        self.nome = nome

    def zerar(self):
        self.carregar = None
        self.posicao = None
        self.dificuldade = None
        self.nome = None




def animacao():
    pass




def menu():

    tamanho = largura, altura = 1071, 651
    janela = pygame.display.set_mode(tamanho)

    #dados.zerar() ?????
    animacao()

    #opcoes: iniciar novo jogo, carregar jogo, manual, opcoes ou sair
    #se escolher iniciar jogo, pergunta posicao, nome do save e dificuldade
        #volta pra main e chama a funcao criar generico (depende dif.), assim salvando num arquivo naquela posicao e com aquele nome

    #criar aqui o objeto da classe dados
    
    posicao = "1"
    nome = "erick"
    dificuldade = "facil"
    carregar = False

    global teste

    teste = dados(dificuldade,carregar,posicao,nome)
    
    #return


#fazer aqui todo e qualquer menu, qualquer icone verdinho que representar uma função era bom ficar aqui
