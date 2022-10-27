import pygame
import sys
import celulas
from os import path
import menu

pygame.init()

def animacao():
    pass

tamanho = largura, altura = 1071, 651
janela = pygame.display.set_mode(tamanho)

fundo = pygame.image.load(path.join('cenario', 'dia.png'))
#fundo_noite = pygame.image.load(path.join('cenario', 'noite.png'))
configuracoes = pygame.image.load("configuracoes.png")

coordenadas = w, z = 0, 0
preto = 0, 0, 0
dinheiro = 999999
horario = 1
sistema_atual = "espectador"
achei = False
#clock tick


matriz_grid = []
lista = []

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            position = pos_x, pos_y = pygame.mouse.get_pos()
            
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


                print(pos_vetor)

                if celulas.lista[pos_vetor].pedra == True:
                    #remocao = tirar_pedra()
                    remocao = True
                    if remocao == True:
                        y = (y // 21) * 93
                        dinheiro = dinheiro - ((y * 50) + 50)
                        celulas.lista[pos_vetor].pedra = False


                        print(celulas.lista[pos_vetor].pedra)#dando um erro aqui, havia uma pedra no ide 66 ou posv 65, mas so foi no 86

                        #verificar_pretendencia




    janela.fill(preto)
    janela.blit(fundo, (0,0))
    janela.blit(configuracoes,(0,0))

    contagem = 0
    while contagem < 147:
        celulas.lista[contagem].imagem()    #sera se tem problema atualizar toda santa vez as imagens?
        if celulas.lista[contagem].obj != None:
            janela.blit(celulas.lista[contagem].obj,celulas.lista[contagem].coordenadas)

        contagem += 1

    pygame.display.flip()
    
