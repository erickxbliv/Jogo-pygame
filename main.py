import pygame
import sys
import celulas
pygame.init()

tamanho = largura, altura = 1071, 651
janela = pygame.display.set_mode(tamanho)

foto = pygame.image.load("dia.png")

coordenadas = w, z = 0, 0
preto = 0, 0, 0

matriz_grid = []
lista = []
matriz_grid.append = (lista)



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    janela.fill(preto)
    janela.blit(foto, (0,0))
    pygame.display.flip()

    #janela.blit(celula, coordenadas)
    pygame.display.flip()
    