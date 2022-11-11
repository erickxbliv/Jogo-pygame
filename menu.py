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

    if dificuldade == "facil": 
        jogo.dinheiro = 5000     #quanto seria bom?
        jogo.sobresalas.lucrodia = 20
    else: 
        jogo.dinheiro = 2500
        jogo.sobresalas.lucrodia = 10

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

    #jogo.modo = "construir"

    desfocar = pygame.image.load(path.join('sistema', 'sistemaaberto.png'))
    voltar = pygame.image.load(path.join('sistema', 'voltar.png'))

    pagina1 = ["elevador","quarto","cozinha","tratamento"]
    pagina2 = ["gerador","renda","laboratorio","treinamento"]
    livreto = [pagina1, pagina2]
    paginaatual = 0
    min = 0
    max = 1

    coord0 = [66,67,68,69,87,88,89,90]      #as celulas onde estao cada opcao
    coord1 = [70,71,72,73,91,92,93,94]
    coord2 = [74,75,76,77,95,96,97,98]
    coord3 = [78,79,80,81,99,100,101,102]

    while True:
        if paginaatual == min:
            ant = "naopaginaanterior"
        else:
            ant = "paginaanterior"
        if paginaatual == max:
            prox = "naopaginaproxima"
        else:
            prox = "paginaproxima"

        funcoes.catalogo(jogo, lista, desfocar, voltar, ant, prox,livreto[paginaatual], False)

        if jogo.dinheiro >= jogo.sobresalas.preco[paginaatual][0]: cor = "White"
        else: cor = "Red"
        funcoes.texto(str(jogo.sobresalas.preco[paginaatual][0]), cor,231,419)
        if jogo.dinheiro >= jogo.sobresalas.preco[paginaatual][1]: cor = "White"
        else: cor = "Red"
        funcoes.texto(str(jogo.sobresalas.preco[paginaatual][1]), cor,433,419)
        if jogo.dinheiro >= jogo.sobresalas.preco[paginaatual][2]: cor = "White"
        else: cor = "Red"
        funcoes.texto(str(jogo.sobresalas.preco[paginaatual][2]), cor,635,419)
        if jogo.dinheiro >= jogo.sobresalas.preco[paginaatual][3]: cor = "White"
        else: cor = "Red"
        funcoes.texto(str(jogo.sobresalas.preco[paginaatual][3]), cor,837,419)

        pygame.display.flip()



        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                pos_vetor = funcoes.achar_celula(position)

                if pos_vetor == 0: 
                    #aqui e pra voltar pros subsistemas
                    return True

                elif pos_vetor == 64 or pos_vetor == 65 or pos_vetor == 85 or pos_vetor == 86:
                    if paginaatual > min: paginaatual -= 1
                elif pos_vetor == 82 or pos_vetor == 83 or pos_vetor == 103 or pos_vetor == 104:
                    if paginaatual < max: paginaatual += 1

                elif pos_vetor in coord0:
                    if jogo.dinheiro >= jogo.sobresalas.preco[paginaatual][0]: 
                        jogo.construirtipo = livreto[paginaatual][0]
                        jogo.sobresalas.precoatual = jogo.sobresalas.preco[paginaatual][0]
                    else: jogo.construirtipo = None

                elif pos_vetor in coord1:
                    if jogo.dinheiro >= jogo.sobresalas.preco[paginaatual][1]: 
                        jogo.construirtipo = livreto[paginaatual][1]
                        jogo.sobresalas.precoatual = jogo.sobresalas.preco[paginaatual][1]
                    else: jogo.construirtipo = None

                elif pos_vetor in coord2:
                    if jogo.dinheiro >= jogo.sobresalas.preco[paginaatual][2]: 
                        jogo.construirtipo = livreto[paginaatual][2]
                        jogo.sobresalas.precoatual = jogo.sobresalas.preco[paginaatual][2]
                    else: jogo.construirtipo = None

                elif pos_vetor in coord3:
                    if jogo.dinheiro >= jogo.sobresalas.preco[paginaatual][3]: 
                        jogo.construirtipo = livreto[paginaatual][3]
                        jogo.sobresalas.precoatual = jogo.sobresalas.preco[paginaatual][3]
                    else: jogo.construirtipo = None
                else: return True

                if jogo.construirtipo != None:
                    voltou = funcoes.preparar_obra(jogo,lista) #se voltar for falso, e pra sair. Verdade, e pra ficar
                    if voltou == False:
                        return False
                    else: jogo.construirtipo = None

        jogo.clock.tick(60)