import pygame
from pygame import mixer
mixer.init()
pygame.init()

from os import path
import sys


def animacao(jogo, lista, flipar):

    #jogo.sobresalas.testeduplas = []

    preto = 0, 0, 0
    jogo.janela.fill(preto)
    jogo.janela.blit(jogo.fundo, (0,0))
    jogo.janela.blit(jogo.iconesistema, (0,0))

    if jogo.modo == "construir":
        contorno1 = pygame.image.load(path.join('sistema', 'constrorno1.png'))
        contorno2 = pygame.image.load(path.join('sistema', 'constrorno2.png'))
        contorno3 = pygame.image.load(path.join('sistema', 'constrorno3.png'))

    contagem = 0
    while contagem < 147:
        lista[contagem].imagem()    #sera se tem problema atualizar toda santa vez as imagens?
        if lista[contagem].obj != None:
            jogo.janela.blit(lista[contagem].obj,lista[contagem].coordenadas)

        if jogo.modo == "construir":
            if jogo.construirtipo == "elevador":
                if lista[contagem].pretendente == "total" or lista[contagem].pretendente == "vertical":
                    jogo.janela.blit(contorno1,lista[contagem].coordenadas)

                    #------- n sei
            elif jogo.construirtipo == "treinamento":
                b = (contagem) % 21

                if lista[contagem].pretendente == "total":
                    ctg = contagem
                    if lista[ctg-1].vazio and not lista[ctg-1].pedra and lista[ctg-2].vazio and not lista[ctg-2].pedra and b > 1:
                        jogo.janela.blit(contorno3,lista[contagem-2].coordenadas)

                    elif lista[ctg+1].vazio and not lista[ctg+1].pedra and lista[ctg+2].vazio and not lista[ctg+2].pedra and b < 19:
                        jogo.janela.blit(contorno3,lista[contagem].coordenadas)
                    #-------- n sei

            else:
                b = (contagem) % 21
                if lista[contagem].pretendente == "total":
                    if lista[contagem-1].vazio and not lista[contagem-1].pedra and b != 0:
                        jogo.janela.blit(contorno2,lista[contagem-1].coordenadas)

                        #jogo.sobresalas.testduplas.append(ctg)      #TESTEEEEEEEEE
                        #jogo.sobresalas.testduplas.append(ctg-1)

                    elif lista[contagem+1].vazio and not lista[contagem+1].pedra and b != 20:
                        jogo.janela.blit(contorno2,lista[contagem].coordenadas)

                        #jogo.sobresalas.testduplas.append(ctg)      #TESTEEEEEEEEE
                        #jogo.sobresalas.testduplas.append(ctg+1)

        contagem += 1

    if flipar == True: pygame.display.flip()


def minerar(jogo, celula):

    confirmacao = pygame.image.load(path.join('sistema', 'removerpedra.png'))
    contorno = pygame.image.load(path.join('sistema', 'contorno1.png'))
    erro  = pygame.image.load(path.join('sistema', 'naopode.png'))

    jogo.janela.blit(contorno, celula.coordenadas)
    jogo.janela.blit(confirmacao,(459,186))
    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                if pos_y >= 372 and pos_y <= 465:
                    if pos_x >= 510 and pos_x <= 560:
                        return
                    elif pos_x >= 612 and pos_x <= 663:
                        preco = (((celula.id-1) // 21) * 50) + 50
                        if jogo.dinheiro < preco:
                            jogo.janela.blit(erro,(459,186))
                            pygame.display.flip()
                        else:
                            celula.pedra = False
                            jogo.dinheiro = jogo.dinheiro - preco
                            sucesso =  pygame.mixer.Sound(path.join('sons','minerar.wav'))
                            pygame.mixer.Sound.play(sucesso)
                            return
            
        
def achar_celula(position):

    pos_x, pos_y = position
    x = 1020
    y = 558
    achei = False
    while achei == False:
        if pos_y < y: y -= 93
        else: achei = True
    achei = False
    while achei == False:
        if pos_x < x: x -= 51
        else: achei = True
    y = (y // 93) * 21
    x = (x//51) + 1
    pos_vetor = (x + y) - 1
    return pos_vetor


def pretendencia(lista, pos_vetor, demolicao):

    if demolicao == True:   #se isso for verdade, quer dizer que uma celula foi demolida

        #se vier ide, so diminuir 1 pra ter o pos_vetor
        if lista[pos_vetor].pedra or not lista[pos_vetor].vazio: return
        a = ((pos_vetor) // 21) #representa o i na matriz
        b = (pos_vetor) % 21 #representa o j na matriz
        

        lista[pos_vetor].pretendente = None
        if a != 0:
            if not lista[pos_vetor-21].vazio and lista[pos_vetor-21].tipo == "elevador": lista[pos_vetor].pretendente = "vertical"
        if a != 6:
            if not lista[pos_vetor+21].vazio and lista[pos_vetor+21].tipo == "elevador": lista[pos_vetor].pretendente = "vertical"
        if b != 0:
            if lista[pos_vetor-1].vazio == False: lista[pos_vetor].pretendente = "total"
        if b != 20:
            if lista[pos_vetor+1].vazio == False: lista[pos_vetor].pretendente = "total"
    

    else:                                       #era bom q aqui tambem removesse, qnd destroi uma sala
        #print("plim")
        if lista[pos_vetor].vazio == False:
            a = ((pos_vetor) // 21) #representa o i na matriz
            b = (pos_vetor) % 21 #representa o j na matriz

            if a != 0:
                if lista[pos_vetor-21].vazio == True and lista[pos_vetor-21].pedra == False:
                    if lista[pos_vetor].tipo == "elevador": lista[pos_vetor-21].pretendente = "vertical"
            if a != 6:
                if lista[pos_vetor+21].vazio == True and lista[pos_vetor+21].pedra == False:
                    if lista[pos_vetor].tipo == "elevador": lista[pos_vetor+21].pretendente = "vertical"
            if b != 0:
                if lista[pos_vetor-1].vazio == True and lista[pos_vetor-1].pedra == False: lista[pos_vetor-1].pretendente = "total"
            if b != 20:
                if lista[pos_vetor+1].vazio == True and lista[pos_vetor+1].pedra == False: lista[pos_vetor+1].pretendente = "total"



def erguer(lista, pos_vetor, jogo):

    #essa funcao tbm tem obrigacao de fundir salas

    if jogo.construirtipo == "elevador":
        lista[pos_vetor].vazio = False
        lista[pos_vetor].pretendente = False
        lista[pos_vetor].tipo = "elevador"
        lista[pos_vetor].lvl = "0"
        lista[pos_vetor].situacao = "_1-1"
        lista[pos_vetor].consumo = 20
        jogo.dinheiro -= jogo.sobresalas.preco[0][0]
        jogo.sobresalas.aumentar_qtd(0)

    elif jogo.construirtipo == "quarto":

        lista[pos_vetor].vazio = False
        lista[pos_vetor].pretendente = False
        lista[pos_vetor].tipo = "quarto"
        lista[pos_vetor].lvl = "1"
        lista[pos_vetor].situacao = "_1-2"
        lista[pos_vetor].consumo = jogo.sobresalas.cnsm_EQCAEDRT[1]
        jogo.dinheiro -= jogo.sobresalas.preco[0][1]
        jogo.sobresalas.aumentar_qtd(1)

        lista[pos_vetor+1].vazio = False
        lista[pos_vetor+1].pretendente = False
        lista[pos_vetor+1].tipo = "quarto"
        lista[pos_vetor+1].lvl = "1"
        lista[pos_vetor+1].situacao = "_2-2"
        lista[pos_vetor+1].consumo = jogo.sobresalas.cnsm_EQCAEDRT[1]
        jogo.sobresalas.aumentar_qtd(1)

    sucesso =  pygame.mixer.Sound(path.join('sons','obrafinalizada.wav'))
    pygame.mixer.Sound.play(sucesso)





def preparar_obra(jogo, lista):

    voltar = pygame.image.load(path.join('sistema', 'voltar.png'))

    jogo.modo = "construir"
    while True:

        animacao(jogo, lista, False)
        jogo.janela.blit(voltar, (0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:

                position = pos_x, pos_y = pygame.mouse.get_pos()
                pos_vetor = achar_celula(position)

                if pos_vetor == 0:
                    jogo.modo = "espectador"
                    return True

                if jogo.construirtipo == "elevador":
                    if lista[pos_vetor].pretendente == "vertical" or lista[pos_vetor].pretendente == "total":
                        erguer(lista,pos_vetor,jogo)
                        jogo.modo = "espectador"
                        pretendencia(lista,pos_vetor,False)
                        jogo.construirtipo = None
                        return False

                    else: print("ai pode nao")




                elif jogo.construirtipo == "treinamento": pass




                else:
                    b = (pos_vetor) % 21
                    l = lista
                    p = pos_vetor
                    t = "total"
                    executar = True

                    if l[p].pretendente == t and b == 0 and not l[p+1].vazio:
                        executar = False        #caso onde tem 1 celula sozinha na margem esquerda sendo amassada
                        print("AAAAAAAA")
                    elif l[p].pretendente == t and b == 20 and not l[p-1].vazio:
                        executar = False        #caso onde tem 1 celula sozinha na margem direita sendo amassada
                        print("BBBBBBB")
                        
                    elif l[p].pretendente == t and b > 0 and b < 18 and not l[p-1].vazio and l[p+1].pretendente == t and not l[p+2].vazio:
                        pass    #uma construcao entre 2 salas, uma intersseccao, onde a clicada tem uma esquerda ocupada
                        #if l[p].tipo == l[p-1].tipo: l[p-1].situacao[3] < 6
                        print("CCCCCCCC")
                    elif l[p].pretendente == t and b > 1 and b < 19 and not l[p+1].vazio and l[p-1].pretendente == t and not l[p-2].vazio:
                        pos_vetor = p - 1  #uma construcao entre 2 salas, uma intersseccao, onde a clicada tem uma direita ocupada
                        print("DDDDDDDD")
                    elif l[p].pretendente == t and b > 0 and b < 20:        #aq quando vc clica numa pretendente, 2 casos
                        print("EEEFFF")
                        if l[p-1].pretendente != t and not l[p-1].pedra and not l[p+1].vazio:
                            pos_vetor = p - 1           #vc clicou na celula que tem uma ocupada a direita
                            print("EEEEEEEE")
                        elif l[p+1].pretendente != t and not l[p+1].pedra and not l[p-1].vazio:
                            pass            #vc clicou na celula que tem uma ocupada a esquerda
                            print("FFFFFFFFFF")
                        else: executar = False
                    #a ordem das 2 condicoes a seguir representa oq vai ser escolhido no caso de um diagrama de venn
                    elif l[p].pretendente != t and not l[p].pedra:          #quando vc clica numa nao pretendente de salas normais
                        print("GGGHHH")
                        if l[p-1].pretendente == t and not l[p-2].vazio and b > 1:
                            pos_vetor = p - 1           #se a esquerda dela tem uma sala pretendente, porque a esquerda dela e ocupado
                            print("GGGGGGG")
                        elif l[p+1].pretendente == t and not l[p+2].vazio and b < 19:
                            pass                        #se a direita dela tem uma pretendente porque sua direita esta ocupada
                            print("HHHHHHHH")
                        else: executar = False
                    else: 
                        print("celula vazia, amigo")
                        executar = False
                    
                    if executar:
                        erguer(lista,pos_vetor,jogo)
                        jogo.modo = "espectador"
                        pretendencia(lista,pos_vetor,False)
                        pretendencia(lista,pos_vetor+1,False)
                        jogo.construirtipo = None
                        return False

        jogo.clock.tick(60)




def catalogo(jogo, lista, desfocar, voltar, ant, prox,livrpaginatual, flipar):
    
    anterior = pygame.image.load(path.join('sistema', ant + '.png'))
    proxima = pygame.image.load(path.join('sistema', prox + '.png'))

    opcao1 = pygame.image.load(path.join('sistema', 'comprar' + livrpaginatual[0] + '.png'))
    opcao2 = pygame.image.load(path.join('sistema', 'comprar' + livrpaginatual[1] + '.png'))
    opcao3 = pygame.image.load(path.join('sistema', 'comprar' + livrpaginatual[2] + '.png'))
    opcao4 = pygame.image.load(path.join('sistema', 'comprar' + livrpaginatual[3] + '.png'))
    
    animacao(jogo,lista, False)

    jogo.janela.blit(desfocar, (0,0))
    jogo.janela.blit(voltar, (0,0))
    jogo.janela.blit(anterior, (51,279))
    jogo.janela.blit(proxima, (969,279))

    jogo.janela.blit(opcao1, (153,279))
    jogo.janela.blit(opcao2, (357,279))
    jogo.janela.blit(opcao3, (561,279))
    jogo.janela.blit(opcao4, (765,279))

    if flipar == True: pygame.display.flip()


def texto(frase, cor, x, y):
    font = pygame.font.Font(None,30)
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(frase),True,cor)
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    display_surface.blit(debug_surf,debug_rect)


def fundir(jogo, lista, pos_vetor, duas, esquerda, direita):
    pass