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


    
    

    #opcoes: iniciar novo jogo, carregar jogo, manual, opcoes ou sair
    #se escolher iniciar jogo, pergunta posicao, nome do save e dificuldade
        #volta pra main e chama a funcao criar generico (depende dif.), assim salvando num arquivo naquela posicao e com aquele nome

    
    #aqui vai ficar a musica tocando

    fundo = pygame.image.load(path.join('menu', 'menu.png'))
    carro = pygame.image.load(path.join('menu', 'carro.png'))
    roda = pygame.image.load(path.join('menu', '1roda.png'))


    coordenadas = [-281,574]
    roda1 = [14,85]
    roda2 = [55,87]
    roda3 = [208,83]
    tempo = 45
    angulo = 1

    while True:

        jogo.janela.blit(fundo, (0,0))
        jogo.janela.blit(carro, coordenadas)
        jogo.janela.blit(roda, (roda1[0]+coordenadas[0],659))
        jogo.janela.blit(roda, (roda2[0]+coordenadas[0],661))
        jogo.janela.blit(roda, (roda3[0]+coordenadas[0],657))

        if angulo == 30: angulo = 1
        else: angulo += 1
        roda = pygame.image.load(path.join('menu', str(angulo) + 'roda.png'))

        if coordenadas[0] == 1071:
            coordenadas[0] = -281
            angulo = 1
        else: coordenadas[0] += 2

        pygame.display.flip()



        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                position = pos_x, pos_y = pygame.mouse.get_pos()
                return
            
        jogo.clock.tick(tempo)







    
    posicao = "1"
    nome = "erick"
    dificuldade = "facil"
    carregar = False

    if dificuldade == "facil": 
        jogo.dinheiro = 5000     #quanto seria bom?
        jogo.sobresalas.lucrodia = 20
        jogo.lotacao = 12
    else: 
        jogo.dinheiro = 2500
        jogo.sobresalas.lucrodia = 10
        jogo.lotacao = 6

    jogo.dados = dados(dificuldade,carregar,posicao,nome)
    
    #return


#fazer aqui todo e qualquer menu, qualquer icone verdinho que representar uma função era bom ficar aqui


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

        if (pos_vetor + 1) > 84: coordenadas = (357,186)
        else: coordenadas = (357,372)

        jogo.janela.blit(contorno,lista[pos_vetor].coordenadas)
        jogo.janela.blit(menu,coordenadas)
        jogo.janela.blit(voltar,(0,0))

        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                pos_vetor2 = funcoes.achar_celula(position)

                if pos_vetor2 == 0:
                    jogo.modo = "espectador"
                    return

                if pos_vetor2 >= pos_vetor and pos_vetor2 <= maximo:
                    jogo.modo = "espectador"
                    return




        

