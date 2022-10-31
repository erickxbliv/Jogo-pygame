import pygame
import sys
import celulas
from os import path
import funcoes

pygame.init()

def animacao():
    pass

#compensa mais não mostrar a pretendencia quando se tem pedra, do que ter uma função pra atualizar as pedras quebradas e outra pra 

tamanho = largura, altura = 1071, 651
janela = pygame.display.set_mode(tamanho)

fundo = pygame.image.load(path.join('cenario', 'dia.png'))
#fundo_noite = pygame.image.load(path.join('cenario', 'noite.png'))
#configuracoes = pygame.image.load("configuracoes.png")   #pode ficar "alocado" na celula 1 (0,0), e assim se sabe se foi aberta. 

#sera se compensava eu ter os dados do jogo numa classe?
coordenadas = w, z = 0, 0
preto = 0, 0, 0
dinheiro = 999999
horario = 1
sistema_atual = "espectador"        #modos: espectador - visualizar o bunker, construir - visualizar onde construir, espiar - assistir uma sala individualmente
achei = False
#clock tick

matriz_grid = []
lista = []

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            position = pos_x, pos_y = pygame.mouse.get_pos()
            #se clicar numa sala, tem que abrir ela
            
            if sistema_atual == "espectador":
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

                #print(pos_vetor)

                if celulas.lista[pos_vetor].pedra == True:
                    #remocao = tirar_pedra()
                    remocao = True
                    if remocao == True:
                        y = (y // 21) * 93  #pegando o y de volta, pois quanto mais embaixo mais caro
                        dinheiro = dinheiro - ((y * 50) + 50)
                        celulas.lista[pos_vetor].pedra = False
                        #atualizar_pretendencia_d1_celula(pos_vetor,lista)

                        #print(celulas.lista[pos_vetor].pedra)

                        #verificar_pretendencia
            elif sistema_atual == "construir":
                #selecionar qual comprar atraves de um menu, sera se isso tambem deveria ser uma classe?
                funcoes.construir()


    janela.fill(preto)
    janela.blit(fundo, (0,0))
    #janela.blit(configuracoes,(0,0))

    contagem = 0
    while contagem < 147:
        celulas.lista[contagem].imagem()    #sera se tem problema atualizar toda santa vez as imagens?
        if celulas.lista[contagem].obj != None:
            janela.blit(celulas.lista[contagem].obj,celulas.lista[contagem].coordenadas)

        contagem += 1

    pygame.display.flip()
    #pygame.time.delay(60)
