import pygame
pygame.init()
from pygame import mixer
mixer.init()
import os
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


    
    

    #opcoes: iniciar novo jogo, carregar jogo, manual, opcoes ou sair
    #se escolher iniciar jogo, pergunta posicao, nome do save e dificuldade
        #volta pra main e chama a funcao criar generico (depende dif.), assim salvando num arquivo naquela posicao e com aquele nome

    
    #aqui vai ficar a musica tocando

    soundtrack =  pygame.mixer.Sound(path.join('sons','menu.wav'))
    pygame.mixer.Sound.play(soundtrack)

    fundo = pygame.image.load(path.join('menu', 'menu.png'))
    carro = pygame.image.load(path.join('menu', 'carro.png'))
    roda = pygame.image.load(path.join('menu', '1roda.png'))
    caminho = pygame.image.load(path.join('menu', 'caminho.png'))

    iniciar = pygame.image.load(path.join('menu', 'iniciarjogo.png'))
    if os.stat("save.json").st_size == 0: 
        carregar = pygame.image.load(path.join('menu', 'Falsecarregar.png'))
        save = False
    else: 
        carregar = pygame.image.load(path.join('menu', 'Truecarregar.png'))
        save = True
    manual = pygame.image.load(path.join('menu', 'manual.png'))
    sair = pygame.image.load(path.join('menu', 'sair.png'))

    coordenadas = [-281,574]
    roda1 = [14,85]
    roda2 = [55,87]
    roda3 = [208,83]
    tempo = 45
    angulo = 1.0   #melhor ser float?

    jogo.janela.blit(fundo, (0,0))
    jogo.janela.blit(iniciar, (408,186))
    jogo.janela.blit(carregar, (408,279))
    jogo.janela.blit(manual, (408,372))
    jogo.janela.blit(sair, (408,465))

    load = False

    #while tempo == 2.0:
    while True:

        jogo.janela.blit(caminho, (0,575))
        jogo.janela.blit(carro, coordenadas)
        jogo.janela.blit(roda, (roda1[0]+coordenadas[0],659))
        jogo.janela.blit(roda, (roda2[0]+coordenadas[0],661))
        jogo.janela.blit(roda, (roda3[0]+coordenadas[0],657))

        #jogo.janela.blit(roda, (0,0))

        if angulo == 30.0: angulo = 1.0
        else: angulo += 0.5
        roda = pygame.image.load(path.join('menu', str(int(angulo)) + 'roda.png'))

        if coordenadas[0] == 1071:
            coordenadas[0] = -281
            angulo = 1.0
        else: coordenadas[0] += 2

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                position = pos_x, pos_y = pygame.mouse.get_pos()
                pos_vetor = funcoes.achar_celula(position)
                #print(pos_vetor)

                if pos_vetor >= 50 and pos_vetor <= 54:
                    dificuldade = "facil"
                    jogo.dinheiro = 5000
                    jogo.sobresalas.lucrodia = 20
                    jogo.lotacao = 12
                    jogo.dados = dados(dificuldade,load,None,None)
                    return
                elif pos_vetor >= 71 and pos_vetor <= 75:
                    if save == True:
                        load = True
                        jogo.dados = dados(None,load,None,None)
                        return
                elif pos_vetor >= 92 and pos_vetor <= 96:
                    pag_manual()
                elif pos_vetor >= 113 and pos_vetor <= 117:
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    dificuldade = "dificil"
                    jogo.dinheiro = 2500
                    jogo.sobresalas.lucrodia = 10
                    jogo.lotacao = 6
                    jogo.dados = dados(dificuldade,load,None,None)
                    return

        jogo.clock.tick(tempo)


    #return


#fazer aqui todo e qualquer menu, qualquer icone verdinho que representar uma função era bom ficar aqui



def pag_manual():
    pass



def sistema(jogo, lista, registro):

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



def espiar(jogo,lista,registro,pos_vetor):
    
    jogo.modo = "espiar"

    evoluir = None
    demolir = None
    trabalhadores = None
    producao = None

    podeevoluir = True
    erro =  pygame.mixer.Sound(path.join('sons','erro.wav'))

    produzir = True
    if lista[pos_vetor].tipo == "cozinha":
        prod = pygame.image.load(path.join('sistema', 'tipoproducaoA.png'))
    elif lista[pos_vetor].tipo == "gerador":
        prod = pygame.image.load(path.join('sistema', 'tipoproducaoF.png'))
    elif lista[pos_vetor].tipo == "tratamento":
        prod = pygame.image.load(path.join('sistema', 'tipoproducaoR.png'))
    elif lista[pos_vetor].tipo == "renda":
        prod = pygame.image.load(path.join('sistema', 'tipoproducaoI.png'))
    elif lista[pos_vetor].tipo == "laboratorio":
        prod = pygame.image.load(path.join('sistema', 'tipoproducaoI.png'))
    else: produzir = False

    

    jogo.sobresalas.preco_evoluir()
    while True:




        funcoes.animacao(jogo,lista,False)
        menu = pygame.image.load(path.join('sistema', 'espiarnormal.png'))

        voltar = pygame.image.load(path.join('sistema', 'voltar.png'))
        if lista[pos_vetor].situacao[3] == "1":
            contorno = pygame.image.load(path.join('sistema', 'contorno1.png'))
            menu = pygame.image.load(path.join('sistema', 'espiarsimples.png'))
            maximo = pos_vetor
        elif lista[pos_vetor].situacao[3] == "2":
            contorno = pygame.image.load(path.join('sistema', 'contorno2.png'))
            if lista[pos_vetor].situacao[1] == "2": pos_vetor -= 1
            maximo = pos_vetor + 1
        elif lista[pos_vetor].situacao[3] == "4":
            contorno = pygame.image.load(path.join('sistema', 'contorno4.png'))
            valor = int(lista[pos_vetor].situacao[1]) - 1
            pos_vetor = pos_vetor - valor
            maximo = pos_vetor + 3
        elif lista[pos_vetor].situacao[3] == "6":
            contorno = pygame.image.load(path.join('sistema', 'contorno6.png'))
            valor = int(lista[pos_vetor].situacao[1]) - 1
            pos_vetor = pos_vetor - valor
            maximo = pos_vetor + 5

        else: print("erro") #TESTE

        if jogo.dinheiro < jogo.sobresalas.precoevoluir:
            menu = pygame.image.load(path.join('sistema', 'insuficienteespiarnormal.png'))
            podeevoluir = False
        elif lista[pos_vetor].lvl == "3":
            menu = pygame.image.load(path.join('sistema', 'maxespiarnormal.png'))
            podeevoluir = False

        if (pos_vetor + 1) > 84: 
            coordenadas = (410,186)
            y = 186
        else: 
            coordenadas = (410,372)
            y = 372

       

        jogo.janela.blit(contorno,lista[pos_vetor].coordenadas)
        jogo.janela.blit(menu,coordenadas)
        jogo.janela.blit(voltar,(0,0))
        funcoes.texto(lista[pos_vetor].tipo,(255,255,255),521,y+30)

        if produzir:
            jogo.janela.blit(prod,(521,y+48))
            funcoes.texto(lista[pos_vetor].lvl,(255,255,255),521+55,y+62)


        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                pos_vetor2 = funcoes.achar_celula(position)
                print(pos_vetor2)
                if pos_vetor2 == 0:
                    jogo.modo = "espectador"
                    return

                elif pos_vetor2 >= pos_vetor and pos_vetor2 <= maximo:
                    jogo.modo = "espectador"
                    return

                elif pos_vetor2 >= 50 and pos_vetor2 <= 54:
                    if pos_vetor2 == 50:
                        if podeevoluir: funcoes.evoluir(jogo,lista,pos_vetor)
                        else: pygame.mixer.Sound.play(erro)
                    if pos_vetor2 == 51:
                        pass
                    if pos_vetor2 == 54:
                        pass

                elif pos_vetor2 >= 92 and pos_vetor2 <= 96:
                    #print("ola")
                    if pos_vetor2 == 92:
                        if podeevoluir: funcoes.evoluir(jogo,lista,pos_vetor)
                        else: pygame.mixer.Sound.play(erro)
                    if pos_vetor2 == 93:
                        pass
                    if pos_vetor2 == 96:
                        pass


def gameover(jogo):
    pass