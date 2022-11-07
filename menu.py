import pygame
pygame.init()
from os import path
import sys
import funcoes

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




def cutscene():
    pass




def menu(jogo):


    #dados.zerar(self)
    cutscene()

    #opcoes: iniciar novo jogo, carregar jogo, manual, opcoes ou sair
    #se escolher iniciar jogo, pergunta posicao, nome do save e dificuldade
        #volta pra main e chama a funcao criar generico (depende dif.), assim salvando num arquivo naquela posicao e com aquele nome

    #criar aqui o objeto da classe dados
    
    posicao = "1"
    nome = "erick"
    dificuldade = "facil"
    carregar = False

    if dificuldade == "facil": jogo.dinheiro = 2000     #quanto seria bom?
    else: jogo.dinheiro = 2000

    jogo.dados = dados(dificuldade,carregar,posicao,nome)
    
    #return


#fazer aqui todo e qualquer menu, qualquer icone verdinho que representar uma função era bom ficar aqui


def sistema(jogo, lista):

    desfocar = pygame.image.load(path.join('sistema', 'sistemaaberto.png'))
    subsistemas = pygame.image.load(path.join('sistema', 'subsistemas.png'))
    jogo.janela.blit(desfocar, (0,0))
    jogo.janela.blit(subsistemas, (0,0))
    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                position = pos_x, pos_y = pygame.mouse.get_pos()
                if pos_x <= 51:
                    if pos_y < 93: 
                        jogo.modo = "espectador"        #garantir
                        return
                    elif pos_y >= 93 and pos_y <= 372:
                        if pos_y >= 93 and pos_y < 186:


                            
                            #jogo.modo = "construir"             #aqui vai pra funcao de escolher qual sala, e ai retorna total
                            #return
                            voltou = selecionarsala(jogo,lista)#se voltar for falso, e pra sair. Verdade, e pra ficar
                            if voltou == False:
                                jogo.modo = "espectador"
                                return
                            else:
                                funcoes.animacao(jogo,lista,False)
                                jogo.janela.blit(desfocar, (0,0))
                                jogo.janela.blit(subsistemas, (0,0))
                                pygame.display.flip()


                        if pos_y >= 186 and pos_y < 279:
                            pass #abrir os moradores
                        if pos_y >= 279 and pos_y <= 372:
                            pass #abrir as configuracoes
                    else: return

                else: return


        jogo.clock.tick(60)


def selecionarsala(jogo,lista):

    funcoes.animacao(jogo,lista, False)
    #jogo.modo = "construir"


    desfocar = pygame.image.load(path.join('sistema', 'sistemaaberto.png'))
    voltar = pygame.image.load(path.join('sistema', 'voltar.png'))
    jogo.janela.blit(desfocar, (0,0))
    jogo.janela.blit(voltar, (0,0))
    pygame.display.flip()

    while True:
        #print('ei')
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                pos_vetor = funcoes.achar_celula(position)

                if pos_vetor == 0: 
                    #aqui e pra voltar pros subsistemas
                    return True

                else:         #aqui acontece a selecao da sala
                    #aqui tambem acontece a probicao de construir caso dinheiro insuficiente
                    if jogo.dinheiro < 200:
                        #aq mostrar erro
                        pass
                    else:
                        jogo.construirtipo = "elevador"
                        voltou = funcoes.preparar_obra(jogo,lista)#se voltar for falso, e pra sair. Verdade, e pra ficar
                        if voltou == False:
                            return False
                        else:
                            funcoes.animacao(jogo,lista, False)
                            jogo.janela.blit(desfocar, (0,0))
                            jogo.janela.blit(voltar, (0,0))
                            pygame.display.flip()
        jogo.clock.tick(60)